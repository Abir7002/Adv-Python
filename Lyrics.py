import tkinter as tk
root=tk.Tk()
root.geometry("600x500")
root.config(bg="#117DB7")

x = tk.Label(root,text="Enter the Song Name :",font=("calibri",20,'bold'),bg="#117DB7").place(x=10,y=10)
y = tk.Entry(root).place(x=300,y=13,w=280,h=35)
z = tk.Button(root,text="Show",font=20).place(x=240,y=80,w=100,h=30)
