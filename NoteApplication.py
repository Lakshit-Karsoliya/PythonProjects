import tkinter
import os

from tkinter.simpledialog import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from tkinter import *
import time
root=Tk()
root.update()
root.geometry("300x250+300+300")
root.minsize(height=500,width=500)
root.title("NoteApplication")

#--------THEME COLOR VARIABLES--#
background="white"
foreground="black"
#----x--THEME COLOR VAR---x-----#


fn=Label(root,text="Filename:",bg=background,fg=foreground,width=500)
fn.pack()

path=Entry(root,bg=background,fg=foreground,width=500,border=0)
path.pack()

textarea=ScrolledText(root,height=500,width=500,state='normal',bg=background,fg=foreground,border=0)
textarea.pack()
#----------FILE CLASS--------#
class File():
	def save():
		try:
			text=textarea.get(0.0,END)
			file=open(path.get()+".txt","x")
			file.write(text)
			file.close()
			showinfo(title="message",message="file saved in"+os.getcwd())
		except:
			showerror(title="An Error Occur",message="Unable to save file\ninsert file name ")
	
	def delete():
		try:
			os.remove(path.get()+".txt")
			showinfo(title="info",message="file is deleted")
		except:
			showerror(title="error",message="please open a\nto delete")
#function for open file

	def openfile():
		textarea.delete(0.0,END)
		openfile=open(path.get()+".txt","r")
		a=openfile.read()
		textarea.insert(0.0,a)
		
	def exit():
		root.destroy()

#-------------INFO CLASS------

class Info():
	def properties():
		showinfo(title="Properties",message="File name:"+path.get()+".txt\nLocation:"+os.getcwd()+"\nSize:")
	
	def showtime():
		showinfo(title	="Time",message=time.ctime())	
				
	def inserttime():
		textarea.insert(END,time.ctime())
		
#------Theme Class-------


class Theme():
	def dark():
		textarea.config(background="black",foreground="white")
		path.config(background="black",foreground="white")
		fn.config(background="black",foreground="white")
		menubar.config(background="black",foreground="white",activebackground="black",activeforeground="white")
		
	def light():
		textarea.config(background="white",foreground="black")
		path.config(background="white",foreground="black")
		fn.config(background="white",foreground="black")
		menubar.config(background="white",foreground="black",activebackground="white",activeforeground="black")
		
	def materialdark():
		textarea.config(background="black",foreground="cyan")
		path.config(background="black",foreground="yellow")
		fn.config(background="black",foreground="yellow")
		menubar.config(background="black",foreground="pink",activebackground="black",activeforeground="white")
		

def file():
	file=File()
	filemenu=Menu(menubar,border=0)
	filemenu.add_command(label="Save",command=File.save)
	filemenu.add_command(label="Open",command=File.openfile)
	filemenu.add_command(label="Delete",command=File.delete)
	filemenu.add_command(label="Exit",command=File.exit)
	menubar.add_cascade(label="File",menu=filemenu)
	root.config(menu=menubar)
	
def info():
	info=Info()
	infomenu=Menu(menubar,border=0)
	infomenu.add_command(label="Properties",command=Info.properties)
	infomenu.add_command(label="InsertTime",command=Info.inserttime)
	infomenu.add_command(label="Time",command=Info.showtime)
	menubar.add_cascade(label="Info",menu=infomenu)
	root.config(menu=menubar)
	
def theme():
	theme=Theme()
	tmenu=Menu(menubar,border=0)
	tmenu.add_command(label="Dark",command=Theme.dark)
	tmenu.add_command(label="TangyDark",command=Theme.materialdark)
	tmenu.add_command(label="Lignt",command=Theme.light)
	menubar.add_cascade(label="Theme",menu=tmenu)
	root.config(menu=menubar)
	

menubar=Menu(root,bg=background,fg=foreground,border=0,activebackground=background,activeforeground=foreground)
file()
info()
theme()

root.mainloop()