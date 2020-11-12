"""
This is basic calculator python application 
you can add more buttons and increase its functionality
Calculation history are shown in scrolledtext area 
You make changes according to your taste
Enjoy  :-)
"""
from tkinter import *
from tkinter.scrolledtext import *
root=Tk()
root.minsize(height=900,width=700)
root.resizable(0,0)
root.title("Calculator")

e=Entry(root,width=42)
e.grid(row=0,columnspan=4,sticky="w")

def button(number):
	cur=e.get()
	e.delete(0,END)
	e.insert(0,str(cur)+str(number))

def buttonchar(char):
	c=e.get()
	e.delete(0,END)
	e.insert(0,str(c)+char)
	
def addnum(sym):
	n1=e.get()
	plus=sym
	e.delete(0,END)
	e.insert(0,n1+plus)
	
def evaluate():
	try:
		x=str(e.get())
		n=eval(str(e.get()))
		e.delete(0,END)
		e.insert(0,n)
		y=str(n)
		h="\n"+x+"="+y
		history.insert(0.0,h)
	except:
		pass
	
def delete():
	e.delete(0,END)
	
def remove():
	a=e.get()
	a=str(a)
	l=len(a)
	e.delete(l-1,l)
	return 0

b0=Button(root,text="1",command=lambda:button(1),border=0)
b0.grid(row=1,column=0,ipadx=50,ipady=40)
b1=Button(root,text="2",command=lambda:button(2),border=0)
b1.grid(row=1,column=1,ipadx=50,ipady=40)
b2=Button(root,text="3",command=lambda:button(3),border=0)
b2.grid(row=1,column=2,ipadx=50,ipady=40)
b3=Button(root,text="4",command=lambda:button(4),border=0)
b3.grid(row=2,column=0,ipadx=50,ipady=40)
b4=Button(root,text="5",command=lambda:button(5),border=0)
b4.grid(row=2,column=1,ipadx=50,ipady=40)
b5=Button(root,text="6",command=lambda:button(6),border=0)
b5.grid(row=2,column=2,ipadx=50,ipady=40)
b6=Button(root,text="7",command=lambda:button(7),border=0)
b6.grid(row=3,column=0,ipadx=50,ipady=40)
b7=Button(root,text="8",command=lambda:button(8),border=0)
b7.grid(row=3,column=1,ipadx=50,ipady=40)
b8=Button(root,text="9",command=lambda:button(9),border=0)
b8.grid(row=3,column=2,ipadx=50,ipady=40)
b9=Button(root,text="0",command=lambda:button(0),border=0)
b9.grid(row=4,column=1,ipadx=50,ipady=40)
bdot=Button(root,text=".",command=lambda:buttonchar("."),border=0)
bdot.grid(row=4,column=0,ipadx=50,ipady=40)

btnadd=Button(root,text="+",command=lambda:addnum("+"),border=0)
btnadd.grid(row=2,column=3,ipadx=50,ipady=40)
btnsub=Button(root,text="-",command=lambda:addnum("-"),border=0)
btnsub.grid(row=3,column=3,ipadx=50,ipady=40)
btnmul=Button(root,text="*",command=lambda:addnum("*"),border=0)
btnmul.grid(row=4,column=3,ipadx=50,ipady=40)
btndiv=Button(root,text="/",command=lambda:addnum("/"),border=0)
btndiv.grid(row=1,column=3,ipadx=50,ipady=40)

delbtm=Button(root,text="Del",command=delete,bg="red",fg="white",border=0)
delbtm.grid(row=5,column=3,ipadx=36,ipady=100)

remove=Button(root,text="<",command=remove,border=0,bg="red",fg="white")
remove.grid(row=4,column=2,ipadx=50,ipady=40)

btnequal=Button(root,text="=",command=evaluate,bg="green",fg="white")
btnequal.grid(row=5,columnspan=3,ipadx=234,ipady=100)

H=Label(root,text="History")
H.grid(sticky="w")

history=ScrolledText(root,width=42,height=8)
history.grid(columnspan=4,sticky="w")


root.mainloop()