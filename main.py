# Modules For GUI
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt,QPoint,QThread,QTimer,QTime,QDate,QRect
from PyQt5.QtGui import QMovie,QPixmap,QIcon
from PyQt5.uic import loadUiType
from UI import Ui_MainWindow
import sys
# threading
from threading import Thread as RunExtraTASKS
# Modules for Functions and tasks
import webbrowser
from os import system,startfile,listdir,cpu_count,remove,chdir
from playsound import playsound
from time import sleep,strftime,time
from speech_recognition import Microphone,Recognizer
from random import choice
from difflib import get_close_matches
from pyautogui import press
from psutil import sensors_battery,virtual_memory,cpu_percent
from pyperclip import copy
from wikipedia import summary
from pyttsx3 import init as RunVoiceEngine

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#######################################################################################


class MainThread(QThread):
	def __init__(self):
		super(MainThread,self).__init__()
	def run(self):
		self.Usage=True
		
		self.CountRunTime()
	
	def CountRunTime(self):
		self.start_time=time()
		self.runloop=True
	
		while self.runloop==True:
			RunTime=int(time()-self.start_time)
			boring="res/Res/Boring.mp3"
			if RunTime==20 and self.Usage==True:
				playsound(boring)
			elif RunTime==40 and self.Usage==True:
				playsound(boring)
			elif RunTime==60 and self.Usage==True:
				playsound(boring)
			elif RunTime==80 and self.Usage==True:
				playsound(boring)
			elif RunTime==100 and self.Usage==True:
				playsound(boring)
			elif RunTime==120 and self.Usage==True:
				playsound(boring)
			elif RunTime==140 and self.Usage==True:
				playsound(boring)
			elif RunTime==160 and self.Usage==True:
				playsound(boring)
			elif RunTime==180 and self.Usage==True:
				playsound(boring)
			elif RunTime==190 and self.Usage==True:
				playsound(boring)
			elif RunTime==200 and self.Usage==True:
				playsound(boring)

	def takeCommand(self):
		print("command started to take")
		#It takes microphone input from the user and returns string output
		r = Recognizer()
		with Microphone() as source:
			print("Listening...")
			r.pause_threshold = 1
			audio = r.listen(source)
		try:
			print("Recognizing...")    
			query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
			print(f"User said: {query}\n")  #User query will be printed.

		except Exception as e:
			# print(e)    
			print("Say that again please...")   #Say that again will be printed in case of improper voice 
			return "None" #None string will be returned
		return query


	def stop(self):
		self.runloop=False
	def FalseUsage(self):
		self.Usage=False
	def TaskExecution(self):
		print("Voice Recognizing started...")
		while True:
			time.sleep(3)
			T=self.takeCommand()
			t=T.lower()

			# webpages
			yt="https://youtube.com/"
			amazon="https://amazon.in/"
			instagram="https://instagram.com/"
			gmail="https://gmail.com/"
			google="https://google.com/"
			# res files
			hello="res/Res/Hello.mp3"
			ytvoice="res/Res/OpeningYT.mp3"
			azvoice="res/Res/OpeningAZ.mp3"
			instavoice="res/Res/OpeningInsta.mp3"
			gmvoice="res/Res/OpeningGmail.mp3"
			idk="res/Res/IDK.mp3"
			googlevc="res/Res/OpeningGoogle.mp3"
			iak="res/Res/IAK.mp3"
			if "youtube" in t:
				webbrowser.open(yt)
				playsound(ytvoice,block=False)
			elif t=="hi":
				playsound(hello,block=False)
			elif t=="hello":
				playsound(hello,block=False)
			elif "i am " in t:
				playsound(iak,block=False)
			elif "amazon" in t:
				webbrowser.open(amazon)
				playsound(azvoice,block=False)
			elif "instagram" in t:
				webbrowser.open(instagram)
				playsound(instavoice,block=False)
			elif "gmail" in t:
				webbrowser.open(gmail)
				playsound(gmvoice,block=False)
			elif "google" in t:
				webbrowser.open(google)
				playsound(googlevc,block=False)
			elif "cmd" in t:
				os.startfile("C:/Windows/System32/cmd.exe")
			elif "notepad" in t:
				os.startfile("C:/Windows/System32/cmd.exe")
			elif t=="close":
				self.stop()
				close()

			else:
				playsound(idk,block=False)
			
class SecondThread(QThread):
	def __init__(self):
		super(SecondThread,self).__init__()
	def getCPUUsage(self):
		cpuUsage=cpu_percent(0.1)
		return cpuUsage
	def getRAMUsage(self):
		ramUsage=virtual_memory()[2]
		return ramUsage
	def getBattery(self):
		try:
			battery = sensors_battery()
			batteryPercentage=battery.percent
			return batteryPercentage
		except Exception:
			return 100
	def Runsay(self,text):
		engine = RunVoiceEngine()
		voices = engine.getProperty('voices')
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-30)
		engine.setProperty('voice',voices[4].id)
		engine.say(text)
		engine.runAndWait()

		
	def say(self,text):
		RunExtraTASKS(
			target=self.Runsay, args=(text,), daemon=True
		).start()

ThreadF2=SecondThread()
ThreadF=MainThread()


class MainUI(QMainWindow):
	def __init__(self):
		super().__init__()
		self.CheckAndLogin()
		lgfile=open("Login/loginData.txt")
		self.music_dir=lgfile.readlines()[1]
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		# Some important Vars
		self.firefox_path = '""C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"" %s'
		# Some Important Steps
		
		# Connecting Important Buttons
		self.ui.Close.clicked.connect(self.CloseWindow)
		self.ui.Minimize.clicked.connect(self.MinimizeWindow)
		self.ui.pushButton_3.clicked.connect(self.startUI)
		# Hiding Some Stuff
		self.ui.TASK.setStyleSheet("background-color:transparent;\n"
"color:transparent;\n"
"border:none;")
		self.ui.TakeTASK.setStyleSheet("background-color:transparent;\n"
"color:transparent;\n"
"border:none;")
		# Hiding Time Date frame
		self.ui.time_Date_frame.setStyleSheet("background-color:transparent;")
		self.ui.framep.setStyleSheet("background-color:transparent;")
		# Frameless Window
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.show()
		# get position for draggable window
		self.ui.TASK.setEnabled(False)
		self.ui.TakeTASK.setEnabled(False)
		self.oldPos = self.pos()
	


	def TellAJoke(self):
		jokefile=open("res/JokeFile.txt")
		jokes=jokefile.readlines()
		self.random_joke=choice(jokes)
		self.symbol_removed=self.random_joke.replace("<>",".")
		ThreadF2.say(self.symbol_removed)
	def CheckAndLogin(self):
		dirls=listdir("Login")
		if "loginData.txt" in dirls:
			pass
		else:
			chdir("Login")
			system("python Login.py")
			chdir("..")
	def ExecuteTask(self):
		ThreadF.FalseUsage()
		Task=self.ui.TASK.text()
		task=Task.lower()

		# webpages
		yt="https://youtube.com/"
		amazon="https://amazon.in/"
		instagram="https://instagram.com/"
		gmail="https://gmail.com/"
		google="https://google.com/"
		# res
		hello="res/Res/Hello.mp3"

		ytvoice="res/Res/OpeningYT.mp3"
		azvoice="res/Res/OpeningAZ.mp3"
		instavoice="res/Res/OpeningInsta.mp3"
		gmvoice="res/Res/OpeningGmail.mp3"
		idk="res/Res/IDK.mp3"
		googlevc="res/Res/OpeningGoogle.mp3"
		iak="res/Res/IAK.mp3"
		LTVoice="res/Res/LightTheme.mp3"
		cmdvoice="res/Res/OpeningCMD.mp3"
		copiedvc="res/Res/ResultCopied.mp3"
		wikisearchvc="res/Res/WikiSearch.mp3"
		nothingfoundvc="res/Res/nothingFound.mp3"

		if "youtube" in task:
			webbrowser.open(yt)
			playsound(ytvoice,block=False)
		elif task=="hi":
			playsound(hello,block=False)
			self.ui.reply.setText("Hello.")
		elif task=="hello":
			playsound(hello,block=False)
			self.ui.reply.setText("Hello.")
		elif "i am " in task:
			playsound(iak,block=False)
			self.ui.reply.setText("Actually i already know that...")
		elif "amazon" in task:
			webbrowser.open(amazon)
			playsound(azvoice,block=False)
			self.ui.reply.setText("Opening Amazon...")
		elif "a joke" in task or "another joke" in task or "please joke" in task or task=="another one please":
			self.TellAJoke() 
			self.ui.reply.setText(str(self.symbol_removed))
		elif "instagram" in task:
			webbrowser.open(instagram)
			playsound(instavoice,block=False)
			self.ui.reply.setText("Opening Instagram...")
		elif "gmail" in task:
			webbrowser.open(gmail)
			playsound(gmvoice,block=False)
			self.ui.reply.setText("Opening Gmail...")
		elif "google" in task:
			webbrowser.open(google)
			playsound(googlevc,block=False)
			self.ui.reply.setText("Opening Google...")
		elif task=="cmd":
			os.startfile("C:/Windows/System32/cmd.exe")
			playsound(cmdvoice,block=False)
			self.ui.reply.setText("Opening Command prompt...")
		elif "wiki" in task:
			topic_in_list=task.split("wiki ")
			topic_in_list.remove('')
			topic_in_string=str(topic_in_list)
			replaced_errors=topic_in_string.replace("['","")
			MainTopic=replaced_errors.replace("']","")
			playsound(wikisearchvc,block=False)
			try:
				search=summary(MainTopic)
				copy(search)
				playsound(copiedvc,block=False)
			except Exception:
				playsound(nothingfoundvc,block=False)
		elif "notepad" in task:
			os.startfile("C:/Windows/System32/cmd.exe")
			self.ui.reply.setText("Opening Notepad...")
		elif task=="light theme":
			self.ui.label.setStyleSheet("color:rgb(48,48,48);\n"
"font-size:15px;")
			self.ui.frame.setStyleSheet("background-color:white;")
			playsound(LTVoice,block=False)
			self.ui.TimeL.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"font-size:20px;")
			self.ui.DateL.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"font-size:20px;")
			icon = QIcon()
			icon.addPixmap(QPixmap("res/Close X.png"), QIcon.Normal, QIcon.Off)
			self.ui.Close.setIcon(icon)

			icon2 = QIcon()
			icon2.addPixmap(QPixmap("res/Minimize Centered.png"), QIcon.Normal, QIcon.Off)
			self.ui.Minimize.setIcon(icon2)
			self.ui.reply.setText("Changed to Light Theme.")
		elif "decrease sound" in task or "volume down" in task:
			press("volumedown")
		elif task=="mute":
			press("volumemute")
		elif "increase sound" in task or "volume up" in task:
			press("volumeup")

		elif "medium volume" in task:
			for i in range(50):
				press("volumeup")
			for i in range(25):
				press("volumedown")
		elif task=="rload" or task=="reload":
			self.showCPUUsage()
			self.showRAMUsage()
			self.showBattery()
		elif "close chrome" in task:
			system("taskkill /im chrome.exe")
		elif "close firefox" in task:
			system("taskkill /im firefox.exe")
		elif "play music" in task:
			music_command_list=task.split("music")
			music_nameraw2=str(music_command_list[1])
			music_nameraw=music_nameraw2.replace("'[","")
			music_name=music_nameraw.replace("]'","")
			music="music/"+music_name
			# exception/random
			music_list=listdir(self.music_dir)
			random_music=choice(music_list)
			self.MusicPlaying=False
			
			if music_name=="":
				if self.MusicPlaying==False:
					music_to_playraw=choice(music_list)
					music_to_play=music_to_playraw.strip()
					music_n="music/"+music_to_play
					self.MusicPlaying=True
					
					playsound(music_n,block=False)

					self.ui.reply.setText("Playing Music...")

			
				elif self.MusicPlaying==True:
					playsound("res/Res/already_playing.mp3")
				
					self.ui.reply.setText("Music is Already Playing...")
				else:
					if self.MusicPlaying==False:
						playsound(music,block=False)
						self.MusicPlaying=True
						playsound("res/Res/playing_music.mp3",block=False)
						self.ui.reply.setText("Playing Music")
					elif self.MusicPlaying==True:
						playsound("res/Res/already_playing")
			else:
				if self.MusicPlaying==False:
					closest_match=get_close_matches(music_name+".mp3", music_list)
					closem_str=str(closest_match)
					closem=closem_str.replace("['","")
					closem2=closem.replace("']","")
					if "[]" in closem2:
						playsound("res/Res/NoMusicRandom.mp3",block=False)
						playsound("music/"+random_music,block=False)
						self.ui.reply.setText("Playing Music...")
						self.MusicPlaying=True
					else:
						playsound("music/"+closem2,block=False)
						
						playsound("res/Res/playing_music.mp3",block=False)
						self.ui.reply.setText("Playing Music...")
				elif self.MusicPlaying==True:
					playsound("res/Res/already_playing")
					self.ui.reply.setText("Music is Already Playing")
		elif task=="close":
			self.CloseWindow()
		elif task=="shutdown":
			playsound("res/Res/ShutDown.mp3",block=False)
			system("shutdown /s")
			self.ui.reply.setText("Shutting Down...")
		elif task=="restart":
			playsound("res/Res/Restart.mp3",block=False)
			system("shutdown /r")
			self.ui.reply.setText("Restarting...")
		elif task=="logoff" or task=="logout":
			playsound("res/Res/LogOff.mp3",block=False)
			system("shutdown /l")
			self.ui.reply.setText("Logging Off...")
	
		else:
			playsound(idk,block=False)
			self.ui.reply.setText("Sorry, i dont know that...")
	def startUI(self):
		fl=open("RunningCache.txt","w")
		fl.close()
		self.start_time = time()
	
		VoiceGifLocation="res/Voice.gif"
		HomeGifLocation="res/HomeScreenDark.gif"
		# CPU,Battery,RAM
		self.showCPUUsage()
		self.showRAMUsage()
		self.showBattery()
		# loading voice gif
		self.ui.info.setPixmap(QPixmap("res/frame2.jpg"))
		self.LoadVoiceGIF()
		# Showing info bar data
		self.ui.CPU.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:rgb(53,184,240);\n"
"font-size:20px;")
		self.ui.RAM.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:rgb(53,184,240);\n"
"font-size:20px;")
		self.ui.Battery.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:rgb(53,184,240);\n"
"font-size:20px;")

		# removing and disabling the start button 
		self.ui.pushButton_3.setStyleSheet("background-color:transparent;\n"
"color:transparent;\n"
"border:none;")
		self.ui.pushButton_3.setEnabled(False)

		# Enabling buttons and entries
		self.ui.TASK.setEnabled(True)
		self.ui.TakeTASK.setEnabled(True)

		# starting home screen gif
		self.ui.movie=QMovie(HomeGifLocation)
		self.ui.screen.setMovie(self.ui.movie)
		self.ui.movie.start()

		# Time and date(connected to the showTime function)
		timer=QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(1000)

		
		
		# start MainThread
		ThreadF.start()

		# showing hidden time and date...
		self.ui.time_Date_frame.setPixmap(QPixmap("res/frame.jpg"))
		self.ui.framep.setStyleSheet("background-color:rgb(52,183,239);")
		# connecting main tasks to button
		self.ui.TakeTASK.clicked.connect(self.ExecuteTask)
		self.ui.TASK.returnPressed.connect(self.ExecuteTask)
		self.ui.TakeTASK.setStyleSheet("\n"
"QPushButton{\n"
"    background-color:white;\n"
"    border:1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:gray;\n"
"    color:white;\n"
"}")
		self.ui.TASK.setStyleSheet("background-color:white;\n"
"color:black;")
		self.WishUser()
	def LoadVoiceGIF(self):
		VoiceGifLocation="res/Voice.gif"
		self.VoiceGIPHY=QMovie(VoiceGifLocation)
		self.ui.VoiceGIF.setMovie(self.VoiceGIPHY)
		self.VoiceGIPHY.start()
	

	def WishUser(self):

		Hour=strftime("%H")
		inthour=int(Hour)
		
		if inthour>0 and inthour<12:
			playsound("res/Res/GoodMorning.mp3",block=False)
			self.ui.reply.setText("Good Morning, i am Marry, your virtual assistant.")
		elif inthour>12 and inthour<14:
			playsound("res/Res/GoodNoon.mp3",block=False)
			self.ui.reply.setText("Good Noon, i am Marry, your virtual assistant.")

		elif inthour>14 and inthour<17:
			playsound("res/Res/GoodAfternoon.mp3",block=False)
			self.ui.reply.setText("Good Afternoon, i am Marry, your virtual assistant.")

		elif inthour>17 and inthour<24:
			playsound("res/Res/GoodEvening.mp3",block=False)
			self.ui.reply.setText("Good Evening, i am Marry, your virtual assistant.")

	def showTime(self):
		current_time=strftime("%r")
		current_date=strftime("%a, %d %b %Y")
		self.ui.TimeL.setText(current_time)
		self.ui.DateL.setText(current_date)
	def showCPUUsage(self):
		cpu=ThreadF2.getCPUUsage()
		finalcpu="C.P.U: "+str(cpu)+"%"
		self.ui.CPU.setText(finalcpu)
	def showRAMUsage(self):
		ramU=ThreadF2.getRAMUsage()
		finalram="R.A.M: "+str(ramU)+"%"
		self.ui.RAM.setText(finalram)
	def showBattery(self):
		batteryUsage=ThreadF2.getBattery()
		finalbat="BATTERY: "+str(batteryUsage)+"%"
		self.ui.Battery.setText(finalbat)

	def MinimizeWindow(self):
		self.showMinimized()
	def CloseWindow(self):
		ThreadF.stop()
		self.close()
	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()
	def mouseMoveEvent(self, event):
		delta = QPoint (event.globalPos() - self.oldPos)
		self.move(self.x() + delta.x(), self.y() + delta.y())
		self.oldPos = event.globalPos()


# Final Touch
application=QApplication(sys.argv)
MainWindowApplication=MainUI()
MainWindowApplication.show()
sys.exit(application.exec_())