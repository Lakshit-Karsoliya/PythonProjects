from tkinter import *
import numpy
from numpy import random
root=Tk()
root.title("Hex Color Piker")
root.geometry("700x800")
root.resizable(0,0)

label=Label(root,text="\nEnter HEX Color Code\n")
label.grid(row=0,column=0)
e=Entry(root,border=0)
e.grid()

def generate():
	
	str=e.get()
		
	if str[0]=="#" and(len(str)==4 or len(str)==7):
		label2=Label(root,text="\n\nColor of HEX\n Code "+e.get()+" is\n")
		label2.grid(row=5,column=0)
		canvas=Canvas(root,bg=str,width=200,height=200)
		canvas.grid(row=5,column=1)
		
	else:
		el=Label(root,text="error")
		el.grid(row=5,column=1)


def clear():
		e.delete(0,END)
		
def destroy():
		root.destroy()

def randomcolor():
	x=random.choice([0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"],size=(6))
	code="#"+x[0]+x[1]+x[2]+x[3]+x[4]+x[5]
	label2=Label(root,text="\n\nHex code of \nRandom Color is\n"+code)
	label2.grid(row=5,column=0)
	canvas=Canvas(root,bg=code,width=200,height=200)
	canvas.grid(row=5,column=1)
		
				
						
btn=Button(root,text="GENERATE\n COLOR",command=generate,height=4,width=15,border=0,bg="green",fg="white")
btn.grid(row=0,column=1,rowspan=2)

clrbtn=Button(root,text="clear",command=clear,fg="white",background='red',activebackground="pink",highlightcolor="blue",border=0)
clrbtn.grid()

randombtn=Button(root,text="RandomColor",command=randomcolor,border=0,bg="cyan",activebackground="green")
randombtn.grid(row=2,column=1,ipadx=37)

footer=Label(root,text="you can use three digit as\n well as six digit hex color code\nfor white color #fff , #ffffff \nboth are correct\nWARNING!!!\nAny code other than hex color code\n throws error in \n python output window",fg="red")
footer.grid(row=10,columnspan=2)

exit=Button(root,text="Exit",command=destroy,border=0,bg="red",fg="white")
exit.grid(sticky="e",column=1)

root.mainloop()