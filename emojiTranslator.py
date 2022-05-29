# Program that translates text from MP3 File into emojis

#text = input("Please enter a message: ")

def emojiMaker(text):

    text.lower()
    emoji = ""
    if "happy" in text:
        emoji += " \U0001f601"      # Method 1 of displaying emoji (through code)
    if "sad" in text:
        emoji += " 😢"              # Method 2 of displaying emoji (through directly putting the emoji in
    if "angry" in text:
        emoji +=  " 😡" 
    if "scared" in text:
        emoji +=  " 😱"
    if "worried" in text:
        emoji +=  " 😳"
    if "cool" in text:
        emoji +=  " 😎"   
    if "smart" in text:
        emoji += " 🧠"

    print(text + emoji)

emojiMaker()
