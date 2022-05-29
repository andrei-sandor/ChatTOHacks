# Program that translates text from MP3 File into emojis

#text = input("Please enter a message: ")

def emojiMaker(text):

    text.lower()
    if "happy" in text:
        print(text + " \U0001f601")      # Method 1 of displaying emoji (through code)
    elif "sad" in text:
        print(text + " 😢")              # Method 2 of displaying emoji (through directly putting the emoji in
    elif "angry" in text:
        print(text + " 😡")
    elif "scared" in text:
        print(text + " 😱")
    elif "worried" in text:
        print(text + " 😳")
    elif "cool" in text:
        print(text + " 😎")
    elif "smart" in text:
        print(text + " 🧠")
    else:
        print(text)

emojiMaker()
