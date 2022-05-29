# Program that translates text from MP3 File into emojis

text = input("Please enter a message: ")

def emojiMaker():

    text.lower()
    emoji = ""
    if "happy" in text:
        emoji += " 😄"
    if "sad" in text:
        emoji += " 😢"
    if "angry" in text:
        emoji += " 😡"
    if "scared" in text:
        emoji += " 😱"
    if "worried" in text:
        emoji += " 😳"
    if "cool" in text:
        emoji += " 😎"
    if "smart" in text:
        emoji += " 🧠"

    print(text + emoji)

emojiMaker()
