import audioop
# from distutils.command.upload import upload
import websockets
import asyncio
import base64
import json
# from configure import auth_key
import pyaudio
import time

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

# starts recording

stream = p.open(
   format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER
)

auth_key = "646acad2d1114c38a644e646876a9553"
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
 
async def send_receive():
   
   print(f'Connecting websocket to url ${URL}')
   async with websockets.connect(
       URL,
       extra_headers=(("Authorization", auth_key),),
       ping_interval=5,
       ping_timeout=20
   ) as _ws:
       await asyncio.sleep(0.1)
       print("Receiving SessionBegins ...")
       session_begins = await _ws.recv()
       print(session_begins)
       print("Sending messages ...")
       
       async def send():
           var = True
           start = -1
           while var:
               try:
                   data = stream.read(FRAMES_PER_BUFFER)
                   mx = audioop.rms(data, 2)
                   if mx > 2300:              
                       start = -1
                   elif mx < 2300:             
                        if start < 0:          
                            start = time.time()
                            var = True
                        else:
                            if time.time() - start >= 5: #Wait five seconds
                                var=False
                                return
                   data = base64.b64encode(data).decode("utf-8")
                   json_data = json.dumps({"audio_data":str(data)})
                   await _ws.send(json_data)
               except websockets.exceptions.ConnectionClosedError as e:
                   print(e)
                   assert e.code == 4008
                   break
               except Exception as e:
                   assert False, "Not a websocket 4008 error"
               await asyncio.sleep(0.01)

           return True
      
       async def receive():
           while True:
               try:
                   result_str = await _ws.recv()
                   API_ret = json.loads(result_str)
                   print(API_ret['text'])
                   if (API_ret['message_type'] == "FinalTranscript"): #determines when user has finished speaking
                       break
               except websockets.exceptions.ConnectionClosedError as e:
                   print(e)
                   assert e.code == 4008
                   break
               except Exception as e:
                   assert False, "Not a websocket 4008 error"
      
       send_result, receive_result = await asyncio.gather(send(), receive())





asyncio.run(send_receive())


# # translation to different languages for speech to text
# endpoint = "https://api.assemblyai.com/v2/transcript"
# json = {
#     "audio_url": "https://bit.ly/3JNcp4Y",
#     "language_detection": True
# }
# headers = {
#     "authorization": "YOUR-API-TOKEN",
#     "content-type": "application/json"
# }
# response = requests.post(endpoint, json=json, headers=headers)
# print(response.json())