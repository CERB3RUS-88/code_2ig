import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

    wikipedia.summary(person, 1)
    print(info)
    talk(info)

    def take_command():

        try:
            with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
    except:
        pass
    return command

    def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
        time = datetime.datetime.now().strfttime('%I:%M %p')
    talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
    while True:
        run_alexa()
