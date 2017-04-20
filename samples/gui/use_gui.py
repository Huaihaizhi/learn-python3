#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from tkinter import *
import tkinter.messagebox as messegebox
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput=Entry(self)
		self.nameInput.pack()
		self.quitButton=Button(self,text='Hello',command=self.hello)
		self.quitButton.pack()

	def hello(self):
		name=self.nameInput.get() or 'world'
		messegebox.showinfo('Message','Hello,%s' % name)

app=Application()
app.master.title('Hello World')
app.mainloop()