# ChatMoji

## Inspiration
Social media plays a big role in the daily lives of most members of society, due to the coronavirus pandemic the use of social media has increased significantly with more and more users using apps such as Messenger, Instagram and Facebook. Due to the lockdown friends and family haven't been able to meet each others in person making it difficult to express emotions. 

We wanted to bridge the divide that the lockdown has brought by adding user interaction via speech to text and emojis.

## What it does
ChatMoji enables friends and family members to connect over a secure https server that allows them to express their emotions using just their speech. If a user mentions that there are sad while talking, chatmoji automatically generates a sad emoji in realtime! If a user mentions they are both worried and scared in their speech then chatmoji will display both those emotions. 

## How we built it
Throughout our development and design process we investigated many different frameworks and languages, but in the end we determined that the best language to use was Python, HTML5 and CSS using the flask framework. In order to collect the users audio input we used the pyaudio and to process the audio we used the AIservice assembly AI that the sponsers of the TOHackaton so generously provided to us.

## How To Run ChatMoji

To run gitmoji you need to `cd` into the chatmoji directory

### Windows
```bash
pip install pywin && pipwin install pyaudio
export FLASK_APP=main
flask run
```
