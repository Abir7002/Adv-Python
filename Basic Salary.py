import tkinter as tk
root = tk.Tk()
root.geometry('550x600')
root.title("Basic Salary")
root.config(bg="#42f578")

label = tk.Label(root,text="Basic Salary",font=("Georgia",30,'bold')).pack()

label1 = tk.Label(root,text="Basic Salary",font=('calibri',18,'bold')).place(x=10,y=80)
En1 = tk.Entry(root,width=30).place(x=160,y=80,height=40)
label2 = tk.Label(root,text="DA",font=('calibri',18,'bold')).place(x=10,y=130)
