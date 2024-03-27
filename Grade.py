import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
root.title("Delhi Public School")
root.resizable(0,0)
root.config(bg="#474E8B")

def result():
    English = int(m1.get())
    Hindi = int(m2.get())
    Maths = int(m3.get())
    Science = int(m4.get())
    SST = int(m5.get())
    p = (English+Hindi+Maths+Science+SST)/5
    output.set(p)
    if p>=90:
        Grade.set("Your Grade is S")
    elif p>80:
        Grade.Set("Your Grade is A")
    elif p>70:
        Grade.set("Your Grade is B")
    elif p>60:
        Grade.set("Your Grade is C")
    elif P>50:
        Grade.set("Your Grade is D")
    elif p>40:
        Grade.set("Your Gradebis E")
    else:
        Grade.set("Gher Jaa Bhai Tu")

    

output = tk.StringVar()
Grade = tk.StringVar()
title = tk.Label(root,text="Delhi Public School",font=('Georgia',25,'bold'),bg="#474E8B").pack()
a = tk.Label(root,text="Check Your Grade",font=('Calibri',20,'bold'),bg="#474E8B").place(x=200,y=50)
b = tk.Label(root,text="Enter Your Marks in English",font=('Calibri',15,'bold'),bg="#474E8B").place(x=10,y=100)
c = b = tk.Label(root,text="Enter Your Marks in Hindi",font=('Calibri',15,'bold'),bg="#474E8B").place(x=10,y=140)
d = tk.Label(root,text="Enter Your Marks in Maths",font=('Calibri',15,'bold'),bg="#474E8B").place(x=10,y=180)
e = tk.Label(root,text="Enter Your Marks in Science",font=('Calibri',15,'bold'),bg="#474E8B").place(x=10,y=220)
f = tk.Label(root,text="Enter Your Marks in SST",font=('Calibri',15,'bold'),bg="#474E8B").place(x=10,y=260)
g = tk.Button(root,text="Submit",bg="lightgreen",command=result).place(x=250,y=300,w=90,h=30)
result = tk.Label(root,text="",textvariable=output,font=40,bg="#474E8B").place(x=250,y=340)
h = tk.Label(root,text="",textvariable=Grade,font=40,bg="#474E8B").place(x=250,y=380)
m1= tk.StringVar()
b1 = tk.Entry(root,textvariable=m1,font=20).place(x=270,y=100,h=30)
m2= tk.StringVar()
c1 = tk.Entry(root,textvariable=m2,font=20).place(x=270,y=140,h=30)
m3= tk.StringVar()
d1 = tk.Entry(root,textvariable=m3,font=20).place(x=270,y=180,h=30)
m4= tk.StringVar()
e1 = tk.Entry(root,textvariable=m4,font=20).place(x=270,y=220,h=30)
m5= tk.StringVar()
f1 = tk.Entry(root,textvariable=m5,font=20).place(x=270,y=260,h=30)


root.mainloop()
                 
