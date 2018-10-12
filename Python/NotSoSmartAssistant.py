import speech_recognition as sr
import time
import webbrowser
r = sr.Recognizer()
r.energy_threshold = 1000
mic = sr.Microphone()
#Function definitions
def Speech2Text():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        text1 = text.split()
        i=0
        while(i<len(text1)):
            if (text1[i]=='Facebook' or text1[i]=='news' or text1[i]=='YouTube'):
                return(text1[i])
            i = i+1
        return -1
    except sr.UnknownValueError:
        print('You may have to restart the program, your speech was probably unclear')
        return 0
def Links(site):
    if (site=='Facebook'):
        webbrowser.open('https://www.facebook.com/')
    elif (site=='news'):
        webbrowser.open('https://www.reddit.com/r/worldnews/')
    elif (site=='YouTube'):
        webbrowser.open('https://www.youtube.com/')
    else:
        print('Sorry, I\'m not that smart yet. That was not on the list')

#Jarvis welcome statements
print('Hello and Good Morning, this is Jarvis Jr. Just like Jarvis from Iron Man except that my technology is about 20 years short of that. . .\n')
time.sleep(1)
print('What would you like to start of your online journey with? Unfortunately, you\'re stuck with me and your options are limited (for now..). They are: \n')
print('Please remember to choose one option each time you run me :) \n')
print('1. Facebook \n')
print('2. News \n')
print('3. Youtube \n')
time.sleep(1)
print('Your choice is..')
choice = Speech2Text()
if(choice!=0):
    Links(choice)





