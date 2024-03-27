import tkinter as tk
root=tk.Tk()
root.title("Revers")
root.geometry("400x300")
root.config(bg="#32a885")
root.resizable(0,0)
def reverse():
    reverse = 0
    num = int(n.get())
    
    while num>0:
        r = num%10
        reverse = reverse*10+r
        num//=10
    output.set(reverse)
output = tk.StringVar()
x = tk.Label(root,text="Reverse",font=('calibri',20),bg="#32a885",fg="red").pack()
y = tk.Label(root,text="Enter the Number : ",font=('calibri',18),bg="#32a885").place(x=10,y=55)
n = tk.StringVar()
y1 = tk.Entry(root,font=('calibri',18), textvariable=n).place(x=240,y=55,width=150,height=35)
z = tk.Button(root,text="Enter",font=('calibri',15),bg="lime",activebackground="#32a885", command=reverse).place(x=150,y=110,width=100,height=35)
a = tk.Label(root,text="",font=('calibri',18),bg="#32a885",fg="white", textvariable=output).place(x=120,y=150,width=150,height=35)
