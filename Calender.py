from tkinter import *
import tkinter as tk
import calendar
from datetime import date
root = tk.Tk()
root.config(bg="#346eeb")
root.title("Calendar")
root.geometry('450x500')

def show():
    m=int(mon.get())
    y=int(yea.get())
    ot= calendar.month(y,m)
    cal.insert(0, ot)      
def clear():
    cal.delete(1.0,"end")

def exit():
    root.destroy()
    
label=tk.Label(root,text="CALENDAR",font=('Algerian',23,'bold')).pack()
label1=tk.Label(root,text="Month",font=('calibri',18,'bold')).place(x=10,y=50)
mon=tk.IntVar()
Month = tk.Spinbox(root,width="4",from_=1,to=12,textvariable=mon).place(x=90,y=59,width=50,height=20)

label2= tk.Label(root,text="Year",font=('calibri',18,'bold')).place(x=200,y=50)
yea=tk.IntVar()
Year = tk.Spinbox(root,width="5",from_=2000,to=2070,textvariable=yea).place(x=260,y=59,width=50,height=20)

cal = tk.Text(root,width=30,height=10).place(x=80,y=100)
bu = tk.Button(root,text="Submit",font=('calibri',15,'bold'),width=10,command=show).place(x=20,y=300)
bu1 =tk.Button(root,text="Clear",font=('calibri',15,'bold'),width=10,command=clear).place(x=160,y=300)
bu2 =tk.Button(root,text="Exit",font=('calibri',15,'bold'),width=10,command=exit).place(x=300,y=300)
root.mainloop()
