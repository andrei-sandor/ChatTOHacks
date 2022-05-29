# Program that translates text from MP3 File into emojis

text = input("Please enter a message: ")

def emojiMaker():

    text.lower()
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

emojiMaker()
