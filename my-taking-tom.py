import speech_recognition as sr
import os 

def say(text) :
    os.system(f"say {text}")
    


def take_command() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        r.pause_threshold = 1
        audio = r.listen(source)
        try :
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e :
            return "Some Error Occured. Sorry from "
        
        


say ("Hello I am Sourya A.I Assistant")

while True :
    print("Listening")
    query = take_command()
    say(query)