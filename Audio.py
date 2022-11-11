import pyttsx3
book = open(r"demo.txt")

book_text = book.readlines()
e = pyttsx3.init()

for i in book_text:
    e.say(i)
    e.runAndWait()
