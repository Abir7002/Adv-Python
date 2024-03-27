import tkinter as tk
root=tk.Tk()
root.geometry('500x400')
root.config(bg="#4B7A4E")

def bmi():
    weight = float(w.get())
    height = float(h.get())
    bmi = weight/(height*height)
    output.set(bmi)
    

output = tk.StringVar()
label = tk.Label(root,text="BMI CALCULATOR",font=('georgia',25,'bold')).pack()

label1=tk.Label(root,text="Enter your Weight(kg)",font=('calibri',18,'bold')).place(x=10,y=50)
w = tk.StringVar()
entry=tk.Entry(root,text="", textvariable=w).place(x=250,y=55,height=25,width=150)
label2 =tk.Label(root,text="Enter your Height(m)",font=('calibri',18,'bold')).place(x=10,y=100)
h = tk.StringVar()
entry=tk.Entry(root,text="",textvariable=h).place(x=250,y=110,height=25,width=150)
bu = tk.Button(root,text="Submit",font=20,command=bmi).place(x=170,y=160,width=80,height=40)
result = tk.Label(root,text="", textvariable= output).place(x=130,y=200)
root.mainloop()
