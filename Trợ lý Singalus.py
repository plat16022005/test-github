import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
singalus=pyttsx3.init()
voice=singalus.getProperty('voices')
singalus.setProperty('voice',voice[1].id)

def speak(audio):
    print("Singalus: " + audio)
    singalus.say(audio)
    singalus.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    speak("Hello my boss!")
    speak("What do you want?")
def command():
    rp=0
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=0.5
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='vi')
        print("Tuấn: " + query)
    except sr.UnknownValueError:
        speak("Please write your question!")
        query=str(input('Your question: '))       
    return query
if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Google')
        elif "youtube" in query:
            speak("What should I search boss?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "facebook" in query:
            speak("Here you are!")
            url=f"https://www.facebook.com/"
            wb.get().open(url)
        elif "find somebody" in query:
            speak("Who are you finding?")
            search=command().lower()
            url=f"https://www.facebook.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on facebook')
        elif "my love" in query:
            speak("Here you are!")
            url=f"https://www.facebook.com/profile.php?id=100087964844150"
            wb.get().open(url)            
        elif "time" in query:
            time()
        elif "anime" in query:
            speak("I hope you will have a good time!")
            url=f"https://animevietsub.app/"
            wb.get().open(url)            
        elif "bye" in query:
            speak("Ok! Good bye my boss")
            os.system("cls")
            quit()
        else:
            speak(query)