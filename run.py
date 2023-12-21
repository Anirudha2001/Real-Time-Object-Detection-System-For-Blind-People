from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import os
import python_weather
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")


def talkToMe(audio):
    # "speaks audio passed as argument"
    print(audio)
    speak.Speak(audio)


def myCommand():
    # "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak_command = 'Please give some command to me...'
        talkToMe(speak_command)

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        talkToMe('You said: ' + command + '\n')

    # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        talkToMe(
            'Your last command couldn\'t be heard ! I can understand commands like open camera and Quit')
        # speak.Speak('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    # "if statements for executing commands"
    message = 'Ask me to do something, I can understand commands like open camera and Quit'

    if 'open camera' in command:
        os.system('python main.py')

        talkToMe('Done!')

    elif 'Quit' in command:
        talkToMe('See you later Take care !')
        exit()

    else:
        talkToMe(
            'I don\'t know what you mean! I can understand commands like open camera and Quit')


talkToMe('Hey, I am Listening and I am ready for your command !')
# loop to continue executing multiple commands
while True:
    assistant(myCommand())
