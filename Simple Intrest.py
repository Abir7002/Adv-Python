import tkinter as tk
root = tk.Tk()
root.geometry('500x400')
root.title("Simple Interesr")
root.config(bg="#1d94bf")

def Simple():
    p = int(n1.get())
    r = int(n2.get())
    t = int(n3.get())
    si = p*r*t/100
    output.set(si)

Label = tk.Label(root,text="Simple Interest",\
                 font=('Georgia',25,'bold'),fg='red',bg='lime')\
                 .pack()
x = tk.Label(root,text="Enter the principle : ",\
             font=20,bg="#1d94bf").place(x=10,y=70)
n1 = tk.StringVar()
x1 = tk.Entry(root,width='20', bg='teal', fg='white', font='20',\
              textvariable=n1).place(x=200,y=70, height=30)



output=tk.StringVar()

y = tk.Label(root,text="Enter the Rate : ",\
             font=20,bg="#1d94bf").place(x=10,y=110)
n2 = tk.StringVar()
y1 = tk.Entry(root,width='20', bg='teal', fg='white', font='20',textvariable=n2)\
     .place(x=200,y=110, height=30)


z = tk.Label(root,text="Enter the Time : ",\
             font=20,bg="#1d94bf").place(x=10,y=150)
n3 = tk.StringVar()
z1 = tk.Entry(root,width='20', bg='teal', fg='white', font='20',textvariable=n3)\
     .place(x=200,y=150, height=30)

a = tk.Button(root,text="Calculate",width=40,height=2,bg="hotpink", command=Simple).place(x=100,y=200)

Label1= tk.Label(root,text="The Number is : ",font=20,bg="#1d94bf").place(x =10,y=260)
result= tk.Label(root,text="",textvariable=output,bg="#1d94bf").place(x=10,y=250)


root.mainloop()
