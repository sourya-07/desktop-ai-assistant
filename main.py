import speech_recognition as sr
import os 
import webbrowser
import openai
import datetime

def say(text) :
    os.system(f"say {text}")
    


def take_command() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        r.pause_threshold = 1
        audio = r.listen(source)
        try :
            # print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e :
            return "Some Error Occured. Sorry from "
        
        


say ("Hello I am Souryaa A.I Assistant")

while True :
    print("Listening")
    query = take_command()
    
    sites = [["Youtube", "https://www.youtube.com/"], ['spotify', 'https://open.spotify.com/']]
    for site in sites :
        if f"Open {site[0]}".lower() in query.lower() :
            say(f"Opening {site[0]} Sourya Sir...")
            webbrowser.open(site[1])
    
    if "the time" in query :
        strf_time = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Souryaa Sir, the time is {strf_time}")
    
    # this code will help in opening applications inside the computers
    if "play Perfect song" in query :
        musicPath = "/Users/souryagupta/Downloads/Perfect-(Mr-Jat.in).mp3"
        os.system(f"open '{musicPath}'")

    # say(query)