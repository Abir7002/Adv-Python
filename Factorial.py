import tkinter as tk
root = tk.Tk()
root.geometry("400x300")
root.resizable(0,0)
root.config(bg="#7335c4")

def factorial():
    num=int(n.get())
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial *i
    output.set(factorial)

output=tk.StringVar()
x = tk.Label(root,text="Factorial No",font=('calibri',20,'bold'),bg="#7335c4",fg="white").pack()

y = tk.Label(root,text="Enter the Number : ",font=('rockwell',15,'bold'),bg="#7335c4",fg="white").place(x=10,y=50)
n = tk.StringVar()
y1 = tk.Entry(root, textvariable=n, font=25).place(x=230,y=50,width=150,height=30)
z = tk.Button(root,text="Enter",command=factorial,font=("algerian",18,'bold'),bg="lime",fg="White").place(x=160,y=90,w=100,h=30)
a = tk.Label(root,text="",bg="#7335c4", textvariable=output, font=20).place(x=170,y=130)
