import pyttsx3

def add(text):
    f = open('G:\Jarvis\Database\history.txt','r')
    line = f.read()
    f.close()
    if line == '':
        f1 = open('G:\Jarvis\Database\history.txt','w')
        f1.write(text)
        f1.close()
    else:
        f2 = open('G:\Jarvis\Database\history.txt','w')
        f2.write(f"{line}\n{text}")
        f2.close()

def clear():
    f3 = open('G:\Jarvis\Database\history.txt','w')
    f3.write("")
    f3.close()

def speak(text):
    mytext = f"Jarvis : {text}"
    add(text=mytext)
    print(mytext)
    pyttsx3.speak(text=text)   

speak("sonia was the last patient of the day and therefore Dr. bansi sharma could spare time to talk with her")