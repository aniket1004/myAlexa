#Add comments and more options for alexa
import speech_recognition as sr
import  pyttsx3
import pywhatkit
import datetime
import wikipedia
import  pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=2)
            print("Listening..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                talk(command)
    except:
        pass

    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing the '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'good bye' in command:
        talk('good bye')
        exit(0)
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
