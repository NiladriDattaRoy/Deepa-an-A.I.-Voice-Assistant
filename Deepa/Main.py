from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from pywikihow import search_wikihow 
import Myalarm
import json
import operator
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
import mimetypes
import pygame
from urllib.request import urlopen
import instaloader
import pypdf
import PyQt5
import winsound
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUI import Ui_Jarvis




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices.index)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',200)

#text to speach
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#abs
def abs(a):
    return _abs(a)

def add(a,b):
    return a+b

def diff(a,b):
    return(a-b)

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def invert(a):
    return ~a
inv=invert

def intdiv(a,b):
    return a//b
#alarm


#pdf

def pdf_reader():
    book=open('Artificial Intelligence vs Augmented Intelligence.pdf','rb')
    pdf_reader= pypdf.PdfReader(book)
    pages= len(pdf_reader.pages)
    print(f"Total number of pages in the pdf is: {pages} ")
    speak(f"Total number of pages in the pdf is: {pages} ")
    speak(f"Sir, please enter the page number I have to read")
    pg= int(input("Enter The PageNo.: "))
    page=pdf_reader.pages[pg-1]
    read=page.extract_text()
    print(read)
    speak(read)

#To Wish
def wish():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!!!")
        print("Good Morning!!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!!")
        print("Good Afternoon!!!")
    else:
        speak("Good Evening!!!")
        print("Good Evening!!!")
    print("I am Deepa, and how can I help You?")
    speak("I am Deepa, and how can I help You?")



#for news updates
def news():
   url='https://newsapi.org/v2/everything?q=tesla&from=2024-12-11&sortBy=publishedAt&apiKey=26f9eb5b86b44a25b80c4f53c9b9b768'
   page= requests.get(url).json()
   article= page["articles"]
   head=[]
   day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
   for ar in article:
     head.append(ar["title"])
   for i in range (len(day)):
     print(f"today's {day[i]} news is: {head[i]}")
     speak(f"today's {day[i]} news is: {head[i]}")

'''class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
def run(self):
        self.TaskExecution'''

    #To covert: Voice to Text
def takecommand():
        read= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.......")
            read.adjust_for_ambient_noise(source)
            read.pause_threshold = 1
            audio = read.listen(source,timeout =None,phrase_time_limit =5)

        try:
            print("Recognizing........")
            query= read.recognize_google(audio, language="en-in")
            print(f"user said: {query}") 
        
        except Exception as e:
            return "none"
        return query
#play music
audio_files = [f for f in os.listdir("C:\\Users\\nilad\\Desktop\\Songs") if f.endswith(('.mp3', '.wav'))]
def play_songs_from_folder(folder_path):
    # Initialize the pygame mixer
    pygame.mixer.init()

    # Get a list of audio files in the folder
    global audio_file 

    if not audio_files:
        print("No audio files found in the folder.")
        return

    print(f"Found {len(audio_files)} songs. Starting playback...")
    speak(f"' ',Found, {len(audio_files)} songs, Starting playback...")
    speak(' ')
    speak(' ')
    speak(' ')
    speak(' ')
    try:
        # Load and play each song
        song_path = os.path.join(folder_path, audio_files[4])
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        print(f"Now Playing:{audio_files[4]}")
        speak(f"Now Playing:{audio_files[4]}")
            
            
    except Exception as e:
        print(f"Error playing {song}: {e}")

#switch track
current_song_index = -1
def play_songs_with_controls(folder_path):
    # Initialize pygame mixer
    pygame.mixer.init()
    global current_song_index 
    # Get a list of audio files in the folder
    global audio_files 
    if not audio_files:
        print("No audio files found in the folder.")
        return

    
    

    # Load the first song
    current_song_index = current_song_index + 1 
    pygame.mixer.music.load(os.path.join(folder_path, audio_files[current_song_index]))
    pygame.mixer.music.play()
         
    print(f"Now playing: {audio_files[current_song_index]}")
    speak(f"Now playing: {audio_files[current_song_index]}")

def TaskExecution():
    wish()
    speak("Hello Sir!!")
    while True :
            query=takecommand().lower()

            #logic building for jarvis
        
            #time
            if "time" in query:
                hour= datetime.datetime.now()
                time1="It's: " + hour.strftime("%I:%M ") + hour.strftime("%p")
                print(time1)
                speak(time1)
            
            #date
            if "date" in query:
                hour= datetime.datetime.now()
                date="Today's date is: " + hour.strftime("%d ") + hour.strftime("%B ") + hour.strftime("%Y")
                print(date)
                speak(date)               
                
        
            #name
            if 'what is your name' in query:
                print("My name is Deepa, I am your prsonal A.I. voice assistant")
                speak("My name is Deepa, I am your prsonal A.I. voice assistant")

            #Describe
            if 'describe yourself' in query:
                print("I am Deepa, I am an A.I. voice assistant.\nI was developed by Mr. Niladri Datta Roy of University of Engineering and Management Kolkata, as the final year project in the department of CSE in the year 2024 \nI am just a prototype who can perform certain functions such as playing music, playing songs on youtube , doing mathematical calculations, etc.")
                speak("I am Deepa, I am an A.I. voice assistant.\nI was developed by Mr. Niladri Datta Roy of University of Engineering and Management Kolkata, as the final year project in the department of CSE in the year 2024 \nI am just a prototype who can perform certain functions such as playing music, playing songs on youtube , doing mathematical calculations, etc.")
            #To Open Notepad
            if 'open notepad' in query:
                npath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad"
                speak("Opening notepad!!!")
                os.startfile(npath) 

            #To Close NotePad
            if 'close notepad' in query:
                speak("Ok Sir closing NotePad!!!")
                os.system('taskkill /f /im notepad.exe')
            
            #To Open Epic games
            if 'open epic games' in query:
                epath="C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher"
                speak("opening Epic Games Launcher")
                os.startfile(epath)
            
            #To Close Epic games
            if 'close epic games' in query:
                speak("Ok Sir closing Epic Games Launcher!!!")
                os.system('taskkill /f /im EpicGamesLauncher.exe')
            
            #To Open discord
            if 'open discord' in query:
                dpath="C:\\Users\\nilad\\AppData\\Local\\Discord\\update"
                speak("opening Discord")
                os.startfile(dpath)

            #To Open Telegram
            if 'open telegram' in query:
                tpath="C:\\Users\\nilad\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop\\Telegram"
                speak("opening Telegram")
                os.startfile(tpath)
            
            #To open Whatsapp
            if 'open whatsapp' in query:
                wpath="C:\\Users\\nilad\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Telegram Desktop\\Telegram"
                speak("opening Whatsapp!!!")
                os.startfile(wpath)

            #To Open cmd
            if 'open cmd'in query:
                speak("Opening command prompt..")
                wpath="C:\\Windows\\system32\\cmd.exe"
                os.startfile(wpath)
            
            #To close cmd
            if 'close cmd' in query:
                speak("Ok closing Command Prompt")
                os.system('taskkill /f /im cmd.exe')
            #To Open Chrome
            if 'open google chrome' in query:
                cpath="C:\\Program Files\\Google\\Chrome\\Application\\chrome"
                speak("opening Chrome")
                os.startfile(cpath)
            
            #To Open Camera
            if 'open camera'in query:
                speak("Opening camera...")
                
                cap=cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k= cv2.waitKey(25)
                
                cap.release()
                cv2.destroyAllWindows()
            
            #play music
            if 'play music' in query:
                folder_path="C:\\Users\\nilad\\Desktop\\Songs"
                song=play_songs_from_folder(folder_path)

            #pause music
            if 'pause music' in query:
               pygame.mixer.music.pause()

            #Unpause Music
            if 'unpause music' in query:
                pygame.mixer.music.unpause()
            
            #Switch Track 
            if 'switch track' in query:
                folder_path="C:\\Users\\nilad\\Desktop\\Songs"
                play_songs_with_controls(folder_path)

            #show ip address
            if 'show ip address' in query:
                ip=get('https://api.ipify.org').text
                print(f"Your IP address is {ip}")
                speak(f"Your IP address is {ip}")
            
            #search wikipedia
            if 'wikipedia' in query:
                speak("searching wikipedia")
                query=query.replace("wikipedia", "")
                results= wikipedia.summary(query, sentences=5)
                speak("According to wikipedia")
                print(results)
                speak(results)
            
            #open youtube
            if 'open youtube' in query:
                webbrowser.open("www.youtube.com")
            
            #Open google
            if 'google' in query:
                print("sir, what should I search on google? ")
                speak("sir, what should I search on google? ")
                cm=takecommand().lower()
                webbrowser.open(f"{cm}")
            
            #send message
            if 'send message' in query:
                kit.sendwhatmsg("+919830883792","This is a testing protocol",22,52)
            
            #send sms
            #password = Niiladri@roy232002
            #recovary code = 9Z2UA4BNNHPBSM6P3YQ4BMTY
            if "send sms" in query:
                print("sir, what should I send?")
                speak("sir, what should I send?")
                msz=takecommand()

                from twilio.rest import Client

                account_sid = 'AC8b0871d2e3b810ce8873c4a6c93e7b76'
                auth_token = '7c6548df35000f2043e6fee9fcf2df74'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                   from_='+12312726633',
                   body=msz,
                   to='+919830883792'and '+918777624515' and '+917044632505' and '+918334015748'
                )

                print(message.sid)

            #make call
            if "make call" in query:

                from twilio.rest import Client

                account_sid = 'AC8b0871d2e3b810ce8873c4a6c93e7b76'
                auth_token = '7c6548df35000f2043e6fee9fcf2df74'
                client = Client(account_sid, auth_token)

                message = client.calls\
                    .create(
                   twiml='<Response><Say>Hello This is Deepa</Say></Response>',
                   from_='+12312726633',
                   to='+919830883792'#and '+918777624515' and '+917044632505' and '+918334015748''''
                )

                print(message.sid)

            # set alarm
            if "alarm" in query:
                print("Sir, please tell me the time to set alarm, for example, set alarm at 5:30 am")
                speak("Sir, please tell me the time to set alarm, for example, set alarm at 5:30 am")

                tt=input("Enter Time:")
                tt=tt.replace("set alarm at", "")
                tt=tt.replace(".","")
                tt=tt.upper()

                
                Myalarm.alarm(tt)
                
            #play song 
            if 'play a song on youtube' in query:
                speak("Please write the name of the song to play: ")
                play=input("Please write the name of the song to play: ")
                kit.playonyt(play)
            #Volume up
            if "volume up" in query:
                pyautogui.press("volumeup")
            
            #vloume down
            if "volume down" in query:
                pyautogui.press("volumedown")
            
            #volume mute
            if "volume mute" in query:
                pyautogui.press("volumemute")

            #volume unmute
            if "volume Unmute" in query:
                pyautogui.press("volumeunmute")

            #send email
            if 'send email' in query:
                
                print("What Should I say?")
                speak("What Should I say?")
                content=takecommand().lower()
                if'send a file' in content:
                    email="niladridattaroy25@gmail.com"
                    password="Niladri@25uem"
                    to="niladridatta23@gmail.com"
                    print("OK sir, what is the Subject for the email ?")
                    speak("OK sir, what is the Subject for the email ?")
                    content=takecommand().lower()
                    subject=content

                    print("and sir, What is the message for this email?")
                    speak("and sir, What is the message for this email?")
                    content2=takecommand().lower()
                    message=content2
                    speak("Sir please enter the correct path of the file in the shell")
                    location=input("Please Enter the path here: ")

                    speak("Please wait I am sending the email now")

                    msg=MIMEMultipart()
                    msg['From']=email
                    msg['To']=to
                    msg['Subject']=subject

                    msg.attach(MIMEText(message, 'plain'))

                    #Setup the attachment
                    filename=os.path.basename(location)
                    attatchment=open(location, "rb")
                    part=MIMEBase('application', 'octate-base')
                    part.set_payload(attatchment.read())
                    encoders.encode_base64(part)
                    part.add_header('content-Disposition', 'attatchment; filename= %s'% filename)

                    #Attach the attachment
                    msg.attach(part)

                    server=smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text=msg.as_string()
                    server.sendmail(email, to, text)
                    server.quit()
                    print("The message has been sent to Niladri")
                    speak("The message has been sent to Niladri")

                else:
                    email="niladridattaroy25@gmail.com"
                    password="Niladri@25uem"
                    to="niladridatta23@gmail.com" 
                    message=content
                    server=smtplib.SMTP('smtp.gmail.com', 587)
                    server.startis()
                    server.login(email, password)
                    server.sendmail(email, to, text)
                    server.quit()
                    print("The message has been sent to Niladri")
                    speak("The message has been sent to Niladri")
        
            #set alarm
            if 'set alarm' in query:
                t=int(datetime.datetime.now().hour())
                if t==17:
                    songs="C:\\Users\\nilad\\Desktop\\Songs"
                    os.startfile(os.path.join(songs, read))
            
            #jokes
            if'tell me a joke' in query:
                joke=pyjokes.get_joke(language="en", category="neutral") 
                speak(joke)

            #To read news
            if 'read the news' in query:
                speak("please wait sir, fetching the news")
                news()
            
            #Shutdown the system
            if'shutdown the system' in query:
                os.system('shutdown /s /t 5')

            #restart the system
            if'restart the system' in query:
                os.system('shutdown /r /t 5')
            
            #go to sleep
            if'go to sleep' in query:
                os.system('rund1132.exe powrprof.dll,SetSuspendState 0,1,0')
            
            #To Switch the tab
            if'switch the tab' in query:
                speak("Ok Sir, Switching the Tab!")
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')
            
            #calculation
            if "do a calculation" in query or "make a calculation" in query:
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    print('What to do you want to calculate ?, for example "Say, 1 plus 1"')
                    speak('What to do you want to calculate ?, for example "Say, 1 plus 1"')
                    print("listening.......")
                    r.adjust_for_ambient_noise(source)
                    audio=r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+': operator.add, #Plus
                        '-': operator.sub,#Substract
                        'x': operator.mul,#Multiply
                        '/': operator.__truediv__,#Dvide
                    }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1, op2 =int(op1),int(op2)
                    return get_operator_fn(oper)(op1,op2)
                print("Your result is :")
                speak("Your result is :")
                print(eval_binary_expr(*(my_string.split())))
                speak(eval_binary_expr(*(my_string.split())))

            #Weather
            if "temperature" in query:
                url= 'http://ipinfo.io/json'
                response=urlopen(url)
                data=json.load(response)
                City= data['city']
                search = (f"Temparature in {City}")
                url=f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")
                temp=data.find("div",class_="BNeawe").text
                print(f"Current {search} is {temp}")
                speak(f"Current {search} is {temp}")


            #To check insta profile
            if "instagram profile" in query:
                speak("sir, please enter the user profile correctly:")
                name=input('Enter account name: ')
                webbrowser.open(f'https://www.instagram.com/{name}')
                speak(f"Sir, here is the profile of the user {name}")
                
                speak("sir, would you like to save the profile picture of this account...")
                condition=takecommand().lower()
                if 'sure' in condition:
                    mod= instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    print("Sir, I have successfully saved the picture, you can view it now...")
                    speak("Sir, I have successfully saved the picture, you can view it now...")
            
            #To take screensort
            if "take screenshot" in query or "take a screenshot" in query:
                print("Please tell me the name of the screenshot")
                speak("Please tell me the name of the screenshot")
                name= takecommand().lower()
                speak("Sir, please wait let me save the screenshot")
                img= pyautogui.screenshot()
                img.save(f"{name}.png")
                print("sir, I have succesfully saved the screenshot, you can view it now...")
                speak("sir, I have succesfully saved the screenshot, you can view it now...")
            
            #To view pdf
            if "read pdf" in query:
                pdf_reader()

            #To hide files
            if 'hide all the files' in query:
                os.system("attrib +h /s /d")
                print("Sir, I have successfully hidden all the files")
                speak("Sir, I have successfully hidden all the files")
            
            #To unhide files
            if 'unhide all the files' in query:
                os.system("attrib -h /s /d")
                print("Sir, I have successfully unhidden all the files")
                speak("Sir, I have successfully unhidden all the files")    

            #To find location
            if 'my location'in query:
                speak('Wait sir, let me check!!!')
                try:
                    ipadd=get('https://api.ipify.org').text
                    print(ipadd)
                    url= 'http://ipinfo.io/json'
                    response=urlopen(url)
                    data=json.load(response)
                    city= data['city']
                    region=data['region']
                    print(f"sir, i am asuming that your location is:, {city}, {region}, India ")
                    speak(f"sir, i am asuming that your location is:, {city}, {region}, India ")
                
                except Exception as  e:
                    speak("Sorry sir, can't find your location")
                    pass
            
            #how to do mode
            if "activate how to do mode" in query:
                speak("Sir, how to do mode is now activated!!")
                while True:
                    print("Sir, please tell me what you want to know?")
                    speak("Sir, please tell me what you want to know?")
                    how = takecommand()
                    try:
                        if "exit" in how or "close" in how:
                            speak("Ok sir, closing how to do mode!")
                            break
                        else:
                            max_result=1
                            how_to= search_wikihow(how, max_result)
                            assert len(how_to)==1
                            how_to[0].print()
                            print(how_to[0].summary)
                            speak(how_to[0].summary)

                    except Exception as e:
                        speak("sorry sir,I am not able to find this")

            
            #no thanks
            if "you can sleep" in query:
                print("ok sir!, I am going to sleep now, but you can call me anytime.")
                speak("ok sir!, I am going to sleep now, but you can call me anytime.")
                break

            #terminate
            if "terminate" in query:
             print("Thank You for using me sir!, Have a nice day ahead!")
             speak("Thank You for using me sir!, have a nice day ahead!")
             sys.exit()
            #startexecution= MainThread()

'''class Main(QMainWindow):
                def __init__(self):
                    super().__init__
                    self.ui= Ui_Jarvis()
                    self.ui.setupUi(self)
                    self.ui.pushButton.clicked.connect(self.startTask)
                    self.ui.pushButton_2.clicked.connect(self,close)

                def startTask(self):
                    self.ui.movie = QtGui.QMovie("../../Downloads/Nt6v.gif")
                    self.ui.label.setMovie(self.ui.movie)
                    self.ui.movie.start()

                    self.ui.movie = QtGui.QMovie("../../Downloads/T8bahf.gif")
                    self.ui.label_2.setMovie(self.ui.movie)
                    self.ui.movie.start()
                    timer= QTimer(self)
                    timer.timeout.connect(self,showTime)
                    timer.start(1000)
                    startexecution.start()

                def showTime(self):
                    current_time = QTime.currentTime()
                    current_date= QDate.currentDate()
                    label_time = current_time.toString('hh:mm:ss')
                    label_date= current_date.toString(Qt.ISODate)
                    self.ui.textBrowser.setText(label_date)
                    self.ui.textBrowser.setText(label_time)            

app = QApplication(sys.argv)
jarvis= Main()
jarvis.show()
exit(app_exec_())'''




if __name__ == "__main__":
    while True:
        permission = takecommand()
        if "wake up" in permission:
            TaskExecution()
        if "goodbye" in permission or "good bye" in permission:
            print("Thank You for using me sir!, Have a nice day ahead!")
            speak("Thank You for using me sir!, have a nice day ahead!")
            sys.exit()
    