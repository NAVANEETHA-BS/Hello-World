'''
import speech_recognition as sp
s = sp.Recognizer()
with sp.Microphone() as source:
    print("SAY SOMETHING")
    audio = s.listen(source)
    print("TIME OVER, THANKS")

try:
    print("TEXT: "+s.recognize_google(audio));
except:
    pass
'''
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak anything :")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
    except:
        print("sorry could not recognize your voice")
            
