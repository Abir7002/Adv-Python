import tkinter as tk
root = tk.Tk ()
root.geometry('500x400')
root.config(bg="#1d94bf")

def add():
    x = int(n1.get())
    y = int(n2.get())
    z = x+y

    output.set(z)

labell = tk.Label(root,text="Sum of Two Numbers",\
                   font = '90',fg = 'red',bg = 'Yellow'\
                   ).pack()
output = tk.StringVar()

num1 = tk.Label(root,text="Enter the first Number : "\
                ,font='20',bg="#1d94bf").place(x=10,y=40)
n1 = tk.StringVar()
e1 = tk.Entry(root,text="",font='20', textvariable=n1).place(x=230,y=40)
num2 = tk.Label(root,text="Enter the Socend Number : "\
              ,font='20',bg="#1d94bf").place(x=10,y=80)
n2 = tk.StringVar()
e2 = tk.Entry(root,text="",font='20', textvariable=n2).place(x=230,y=80)

Button=tk.Button(root,text="Enter",width=20\
                 ,bg="Yellow",command=add).place(x=140,y=120)
label2=tk.Label(root, text="The Result is:", font='20',bg="#1d94bf").place(x=10, y=150)

result = tk.Label(root,text="",textvariable =output, font='40', fg='black',bg="#1d94bf").place(x=170,y=150)

root.mainloop()

