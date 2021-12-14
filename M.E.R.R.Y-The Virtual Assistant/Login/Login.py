# Modules For GUI
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
from LoginUI import Ui_MainWindow
import sys
from os import listdir,chdir,remove


class MainUI(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		# connecting ok to close function and min
		self.ui.Close.clicked.connect(self.CloseWindow)
		self.ui.Min.clicked.connect(self.MinimizeWindow)
		# MainLogin Function and Browse Function
		self.ui.LoginB.clicked.connect(self.MainLogin)
		self.ui.BrowseB.clicked.connect(self.BrowseDIR)
		# Frameless Window
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.show()
		# Starting UI
		self.StartUI()
		# draggable window
		self.oldPos = self.pos()

	def StartUI(self):
		# starting home screen gif
		self.ui.movie=QMovie("bg.gif")
		self.ui.screen.setMovie(self.ui.movie)
		self.ui.movie.start()
	def BrowseDIR(self):
		file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		self.ui.MusicDirInput.setText(file)
	def MainLogin(self):
		Username=self.ui.UsernameInput.text()
		self.MusicDir=self.ui.MusicDirInput.text()
		# Checking Data
		# listing files of music dir (to check that if there are any files excluding mp3 or something...)
		T=False
		self.ToBeDeletedFiles=[]
		# try:
		MusicDirFiles=listdir(self.MusicDir)
		for i in MusicDirFiles:
			if ".mp3" in i:
				pass
			else:
				T=True
				self.ToBeDeletedFiles.append(i)
		if T==True:
			self.showyesno("This Folder should contain only mp3 files, should i remove the excluding files?","Error")
		# except Exception as e:
		# 	# self.showdialog("No such file location like MusicDir.","Error!")
		# 	print(e)
				
		# cheking whitespaces in username or MusicDir

		if " " in Username:
			self.showdialog("Sorry, Whitespaces are not allowed.","")
		elif Username=="":
			self.showdialog("Username Cant Be Empty.","Error!")
		elif self.MusicDir=="":
			self.showdialog("MusicDir Cant Be Empty.","Error!")
		else:
			# Creating File and Saving User Info
			f=open("loginData.txt","w")
			f.write(Username+"\n"+self.MusicDir)
			f.close()
			self.showdialog("Successfully Logged in","Info")
			self.close()
	def showyesno(self,data,title):
		msgdata= QMessageBox.question(self,title, data, QMessageBox.Yes | QMessageBox.No)
		if msgdata==QMessageBox.Yes:
			chdir(self.MusicDir)
			for i in self.ToBeDeletedFiles:
				remove(i)
	def showdialog(self,data,title):
		msg = QMessageBox(self)
		msgdata= msg.question(self,title, data, msg.Ok)
	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()
	def mouseMoveEvent(self, event):
		delta = QPoint (event.globalPos() - self.oldPos)
		self.move(self.x() + delta.x(), self.y() + delta.y())
		self.oldPos = event.globalPos()
	def CloseWindow(self):
		self.close()
	def MinimizeWindow(self):
		self.showMinimized()


# Final Touch

application=QApplication(sys.argv)
MainWindowApplication=MainUI()
MainWindowApplication.show()
sys.exit(application.exec_())



