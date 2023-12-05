import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am MINI Sir. Please tell me how may I help you")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open(stackoverflow.com)   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            print(strTime)  
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\VSCode\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sakshamEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
                print("Sorry my friend. I am not able to send this email")    
        
        elif(('good morning' in query) or ('good afternoon' in query) or ('good evening' in query)): 
            speak(wishMe())
        elif(('hello' in query) or ('hi' in query) or ('hey there' in query) or ('hola' in query)):
            speak('Hello sir!')
            print('Hello sir!')
        elif(("What's up" in query) or ('how are you' in query) or ('how is it going' in query) or 
             ('hows it going' in query)):
            speak('It is fantastic in here. what about you?')
            print('It is fantastic in here. what about you?')
        elif(('i am fine' in query) or ("everything's good" in query) or ('everything is good' in query) or 
             ('I am good' in query)): 
            speak('Good to know!')
            print('Good to know!')
        elif(('who created you' in query) or ('who made you' in query)):
            speak('I was created by team CodePro') 
            print('I was created by team CodePro')
        elif(('who are you' in query) or ('what is your identity' in query) or ('introduce yourself' in query)):
            speak('I am MINI. I was created by team CodePro.')
            print('I am MINI. I was created by team CodePro.')
        elif(('what is your name' in query) or ("what's your name" in query)): 
            speak('I am MINI')
            print('I am MINI')
        elif(('thank you' in query) or ('thanks' in query) or ('gratitude' in query) or ('grateful' in query)): 
            speak('Your welcome.') 
            print('Your welcome.')
        elif(('stop' in query) or ('bye' in query) or ('sayonara' in query) or ('see you again' in query)):
            speak('Thank for your time here')
            print('Thank for your time here')
            break