import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry('400x500')
root.title("Notepad")
menubar = tk.Menu(root)
def _exit_():
    root.destroy()
def about():
    messagebox.showinfo("Notepad", "Version 1.0.21")
    
file=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="New")
file.add_command(label="New Window")
file.add_command(label="Open...")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_separator()
file.add_command(label="PageSetup...")
file.add_command(label="Print..")
file.add_separator()
file.add_command(label="Exit" ,command=_exit_)
edit = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_separator()
edit.add_command(label="Search with Bing..")
edit.add_command(label="Find..")
edit.add_command(label="Find Next")
edit.add_command(label="Find Previous")
edit.add_command(label="Replace...")
edit.add_command(label="Go To...")
edit.add_separator()
edit.add_command(label="Select All")
edit.add_command(label="Time/Date")
form=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=form)
form.add_command(label="Word Wrap")
form.add_command(label="Font...")
vi=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=vi)
vi.add_command(label="Zoom")
vi.add_command(label="Status Bar")
he=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=he)
he.add_command(label="View Help")
he.add_command(label="Send Feedback")
he.add_separator()
he.add_command(label="About Notepade", command=about)
textarea = tk.Text(root,width=200,height=200).pack()

root.config(menu=menubar)
root.mainloop()