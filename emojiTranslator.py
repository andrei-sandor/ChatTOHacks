# Program that translates text from MP3 File into emojis

text = input("Please enter a message: ")

def emojiMaker():

    text.lower()
<<<<<<< HEAD
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
        emoji +=  + " 🧠"

    print(text + emoji)
=======
    i = 0

    while (i < len(text)):
        i = i + 1

    if "happy" in text:
            print(text + " 😄")
    if "sad" in text:
        print(text + " 😢")
    if "angry" in text:
        print(text + " 😡")
    if "scared" in text:
        print(text + " 😱")
    if "worried" in text:
        print(text + " 😳")
    if "cool" in text:
        print(text + " 😎")
    if "smart" in text:
        print(text + " 🧠")
>>>>>>> 1aee9a41ac60a96dd25984000ad320e4a6da4ec7

emojiMaker()
