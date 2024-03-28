import tkinter as tk
root = tk.Tk()
root.geometry("500x450")
root.resizable(0,0)
root.config(bg="#5B90C4")
def celsius():
    f = int(t.get())
    c = (5/9)*(f -32)
    output.set(c)
def fahrenheit():
    c = int(t.get())
    f = (9/5)*c + 32
    output.set(f)

    
output = tk.StringVar()
a = tk.Label(root,text="Temperature Converter",font=('calibri',20,'bold'),bg="#5B90C4",fg="lime").pack()
b = tk.Label(root,text="Enter the Temperature",font=('calibri',15,'bold'),bg="#5B90C4").place(x=10,y=50)
t = tk.StringVar()
b1 = tk.Entry(root, textvariable=t).place(x=250,y=50,w=145,h=35)
c = tk.Button(root,text="Celsius",command=celsius,font=('calibri',14,'bold'),bg='lime').place(x=150,y=100,w=100,h=25)
d = tk.Button(root,text="Fahrenheit",command=fahrenheit,font=('calibri',14,'bold'),bg='red').place(x=260,y=100,w=100,h=25)
r = tk.Label(root,text="" , bg="#5B90C4", textvariable=output).place(x=270,y=140)
root.mainloop()
