import os
import tkinter as tk
root = tk.Tk()
root.geometry("300x150")
root.resizable(0,0)
root.title("ShutDown")
root.config(bg="black")

def shutdown():
    return os.system("Shutdown /s /t 1")
def restart():
    return os.system("Shutdown /r /t 1")
def logout():
    return os.system("Shutdown -l")

x = tk.Button(root,text="Shutdown",command=shutdown,bg="Red",font=15,fg="white").place(x=10,y=50,w=90,h=40)
y = tk.Button(root,text="Restart",command=restart,bg="orange",font=15,fg="white").place(x=100,y=50,w=90,h=40)
z = tk.Button(root,text="Log out",command=logout,bg="Green",font=15,fg="white").place(x=190,y=50,w=90,h=40)
