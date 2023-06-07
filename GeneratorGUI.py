from tkinter import *
from tkinter import ttk
from Generate_Password import generatePassword
import pyperclip
def copyToClipboard():
    pyperclip.copy(password.get())

def passwordWrapper(*args):
    password.set(generatePassword(int(passwordLength.get())))
root = Tk()
#root.geometry("500x500")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
password = StringVar()
passwordLength = StringVar()
s = ttk.Style()
s.configure("new.TFrame", background="#91b1b5")
passwordGeneratorFrame = ttk.Frame(root, padding="3 3 12 12", style="new.TFrame")
passwordGeneratorFrame.grid(column=0, row=0, sticky=(N, W, E, S))
button001 = ttk.Button(passwordGeneratorFrame, text='Generate Password', command=passwordWrapper)
button001.grid(column=0, row=3, sticky=(W))
button002 = ttk.Button(passwordGeneratorFrame, text='Copy Password to Clipboard', command=copyToClipboard)
button002.grid(column=1, row=3)
label001 = ttk.Label(passwordGeneratorFrame, text='Password Length')
label001.grid(column=0, row=1)
entrybox001 = ttk.Entry(passwordGeneratorFrame, textvariable=passwordLength)
label002 = ttk.Label(passwordGeneratorFrame, textvariable=password)
label002.grid(column=0, row=2)
entrybox001.grid(column=1, row=1)
root.mainloop()