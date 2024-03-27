from pytube import YouTube
import tkinter as tk
from tkinter import messagebox, filedialog
root = tk.Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("Download YouTube Video")
root.config(bg="#4287f5")
def Download():
    youtube_link = video_link.get()
    download_folder = download_Path.get()
    getVideo = YouTube(youtube_link)
    videoStream = getVideo.streams.get_highest_resolution()
    videoStream.download(download_folder)
    messagebox.showinfo("Successfully download" + download_folder)
def Browse():
    download_Directory = filedialog.askdirectory(initialdir="Your Directory path", title="save video")
    download_Path.set(download_Directory)

x = tk.Label(root,text="YouTub Video Download",font=("ariale black",20,'bold'),bg="#4287f5").pack()
a = tk.Label(root,text="YouTub Link :",font=("calibri",18,'bold'),bg="#f5425a").place(x=10,y=60)
b = tk.Label(root,text="Destination :",font=("calibri",18,'bold'),bg="#f5425a").place(x=10,y=105)
video_link  = tk.StringVar()

a1 =tk.Entry(root, textvariable=video_link).place(x=160,y=60,w=300,h=32)
download_Path = tk.StringVar()
b1 =tk.Entry(root, textvariable=download_Path).place(x=160,y=105,w=200,h=32)
c = tk.Button(root,text="Browse",font=("calibri",11,'bold'),command=Browse).place(x=370,y=105,w=110,h=32)
d = tk.Button(root,text="Download Video",font=("calibri",19,'bold'),command=Download).place(x=150,y=155)