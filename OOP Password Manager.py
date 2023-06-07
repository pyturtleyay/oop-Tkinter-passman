from tkinter import *
from readUsers import readUsers
from tkinter import ttk
from tkinter import messagebox
import string
import random
from pyperclip import *
import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

class newAccountframe(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent.top
        self.root = parent
        ttk.Frame.__init__(self, self.parent,
                           padding="3 3 12 12", style="new.TFrame")
        self.grid(column=0, row=0, sticky=(N, E, S, W))
        self.newUsername = StringVar()
        self.newPassword = StringVar()
        self.newWebsite = StringVar()

        self.usernameLabel = ttk.Label(self, text='New Username', style = 'normalLabel.TLabel')
        self.usernameLabel.grid(column=0, row=0, sticky = (N, W, E, S))

        self.passwordLabel = ttk.Label(self, text='New Password', style = 'normalLabel.TLabel')
        self.passwordLabel.grid(column=0, row=1, sticky = (N, W, E, S))

        self.websiteLabel = ttk.Label(self, text='New Website', style = 'normalLabel.TLabel')
        self.websiteLabel.grid(column=0, row=2, sticky = (N, W, E, S))

        self.websiteEntry = ttk.Entry(self, style = 'normalLabel.TLabel', textvariable = self.newWebsite)
        self.websiteEntry.grid(column=1, row=0, sticky = (N, W, E, S))

        self.passwordEntry = ttk.Entry(self, style = 'normalLabel.TLabel', textvariable = self.newPassword, show="*")
        self.passwordEntry.grid(column=1, row=1, sticky = (N, W, E, S))

        self.usernameEntry = ttk.Entry(self, style = 'normalLabel.TLabel', textvariable = self.newUsername)
        self.usernameEntry.grid(column=1, row=2, sticky = (N, W, E, S))

        self.registerButton = ttk.Button(self, style='normalLabel.TLabel', text='Register', command=self.newAccount)
        self.registerButton.grid(column=1, row=4)

    def passwordCheck(self,password):
        password_length = len(password)
        if password_length < 8:
            raise RuntimeError("The password is too short.")
        if password_length > 32:
            raise RuntimeError("The password is too long.")
        if " " in password:
            raise RuntimeError("Password can't contain space.")
        if "," in password:
            raise RuntimeError("Password can't contain a ','.")
        return True

    def usernameCheck(self,username):
        username_length = len(username)
        if username_length < 8:
            raise RuntimeError("Username too short.")
        if username_length > 25:
            raise RuntimeError("Username too long.")
        if " " in username:
            raise RuntimeError("Username can't contain space.")
        if "," in username:
            raise RuntimeError("Username can't contain ','.")
        return True

    def newAccount(self):
        username = self.newUsername.get().strip()
        password = self.newPassword.get().strip()
        website = self.newWebsite.get().strip()

        usernames = (account.username for account in self.root.currentUserAccounts)

        try:
            if (username not in usernames):
                if self.usernameCheck(username):
                    if self.passwordCheck(password):
                        self.root.currentUserAccounts.append(account(website, username, password))
                        filename = self.root.currentUser + ".txt"
                        f = open(filename, "a")
                        string = "\n" + website + "," + username + "," + password
                        f.write(string)
                        f.close()
                        self.root.updateCurrentUserAccounts()
                        messagebox.showinfo("Registration successful", "You have added a new account successfully")
        except RuntimeError as error:
            messagebox.showinfo("Error", error)



class generatorFrame(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.passwordLength = StringVar()
        self.passwordLength.set(8)
        self.generatedPassword = StringVar()
        ttk.Frame.__init__(self, parent.tabRoot, padding="3 3 12 12", style="new.TFrame")

        button001 = ttk.Button(self, text='Generate Password', command=self.generatePassword)
        button001.grid(column=0, row=3, sticky=(W))
        button002 = ttk.Button(self, text='Copy Password to Clipboard', command=self.copyToClipboard)
        button002.grid(column=1, row=3)
        label001 = ttk.Label(self, text='Password Length')
        label001.grid(column=0, row=1)
        entrybox001 = ttk.Entry(self, textvariable=self.passwordLength)
        label002 = ttk.Label(self, textvariable=self.generatedPassword)
        label002.grid(column=0, row=2)
        entrybox001.grid(column=1, row=1)

    def generatePassword(self):
        lengths = self.passwordLength.get()

        if lengths != "":
            length = int(lengths)
        else:
            length = 8
        generator = LETTERS + NUMBERS + PUNCTUATION
        generator = list(generator)
        random.shuffle(generator)
        password = ''
        for i in range(length):
            password = password + generator[i]
        self.generatedPassword.set(password)

    def copyToClipboard(self):
        pyperclip.copy(self.generatedPassword.get().strip())
class vaultContentsframe(ttk.Frame):
    def __init__(self, parent):
        self.parent=parent
        ttk.Frame.__init__(self, parent.tabRoot, padding="3 3 12 12", style="new.TFrame")
        self.grid(column=0, row=0, sticky=(N, E, S, W))
        self.addAccountbutton = ttk.Button(self, text='Add A New Account', command=self.parent.addNewaccount)
        self.addAccountbutton.grid(column=5, row=5)

        self.accountListFrame=accountListframe(self)
        self.accountDetailFrame=accountDetailFrame(self)
class accountDetailFrame(ttk.Frame):
    def __init__(self, parent):
        self.parent=parent
        self.root = self.parent.parent
        ttk.Frame.__init__(self, parent, padding="3 3 12 12", style="new.TFrame")
        self.grid(column=1, row=0, sticky=(N, E, S, W))

        label01 = ttk.Label(self, textvariable=self.root.username)
        label01.grid(column=0, row=0)
        label02 = ttk.Label(self, textvariable=self.root.password)
        label02.grid(column=0, row=1)
        label03 = ttk.Label(self, textvariable=self.root.website)
        label03.grid(column=0, row=2)
        button01 = ttk.Button(self, text='Copy Password', command=self.copyPassword)
        button01.grid(column=1, row=1)
        button02 = ttk.Button(self, text='Copy Username', command=self.copyUsername)
        button02.grid(column=1, row=0)
        button03 = ttk.Button(self, text='Copy Website', command=self.copyWebsite)
        button03.grid(column=1, row=2)
    def copyPassword(self):
        pyperclip.copy(self.root.password.get().strip())
    def copyUsername(self):
        pyperclip.copy(self.root.username.get().strip())
    def copyWebsite(self):
        pyperclip.copy(self.root.website.get().strip())
class accountListframe(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.root = self.parent.parent
        filename = self.root.currentUser + ".txt"
        f = open(filename, 'r')
        contents = f.readlines()
        accounts = []

        for line in contents:
            tempVariable = line.strip("\n").split(",")
            website = tempVariable[0]
            username = tempVariable[1]
            password = tempVariable[2]
            self.root.currentUserAccounts.append(account(website, username, password))
        f.close()
        ttk.Frame.__init__(self, parent, padding="3 3 12 12", style='new.TFrame')
        self.grid(column=0, row=0)
        self.box = Listbox(self, selectmode=SINGLE)
        self.box.grid(column=0, row=0)
        self.box.bind('<Double-1>', self.root.loginDetails)
        for i in range(len(self.root.currentUserAccounts)):
            self.box.insert(i, self.root.currentUserAccounts[i].site + "|" + self.root.currentUserAccounts[i].username)

    def update(self):
        self.box.delete(0, END)
        for i in range(len(self.root.currentUserAccounts)):
            self.box.insert(i, self.root.currentUserAccounts[i].site + "|" + self.root.currentUserAccounts[i].username)

class account:
    def __init__(self, site, username, password):
        self.site = site
        self.website = site
        self.username = username
        self.password = password

def readUsers():
    f = open("UsersList.txt", 'r')
    users = f.readlines()
    results = {}
    for user in users:
        tempVariable = user.strip("\n").split(",")
        username = tempVariable[0]
        password = tempVariable[1]
        results[username] = password
    f.close()
    return results

class loginFrame(ttk.Frame):
    def __init__(self, parent, userslist):
        self.users = userslist
        self.username = parent.username
        self.password = parent.password
        self.parent = parent

        ttk.Frame.__init__(self, parent.root, padding = "3 3 12 12", style="new.TFrame")

        label1 = ttk.Label(self, background=('#91b1b5'), text="ID:", font=('Verdana'))
        label1.grid(column=1, row=2, sticky=(N, W, E, S))
        label2 = ttk.Label(self, background=('#91b1b5'), text="Password:", font=('Verdana'))
        label2.grid(column=1, row=3, sticky=(N, W, E, S))
        entrybox1 = ttk.Entry(self, textvariable=self.username, font=('Verdana'))
        # entrybox1.place(height=100, width=45)
        entrybox1.grid(column=2, row=2, columnspan=2, sticky=(N, W, E, S))
        entrybox2 = ttk.Entry(self, textvariable=self.password, show='*', font=('Verdana'))
        # entrybox2.place(height=100, width=100)
        entrybox2.grid(column=2, row=3, columnspan=2, sticky=(N, W, E, S))
        loginButton = ttk.Button(self, text=('Login'), command=self.login)
        loginButton.grid(column=2, row=4, sticky=(N, W, E, S))
        quitButton = ttk.Button(self, text='Quit', command=root.destroy)
        quitButton.grid(column=3, row=4, sticky=(N, W, E, S))

        self.parent.root.bind('<Return>', self.login)

        self.grid(column=0, row=0)

    def login(self, *args):
        user = self.username.get()
        pass1 = self.password.get()
        if user in self.users:
            if self.users[user] == pass1:
                messagebox.showinfo("Login successful", "Login successful")
                self.parent.currentUser= user
                self.parent.username.set("")
                self.parent.password.set("")
                self.parent.mainWindow()

            else:
                messagebox.showinfo("wrong password", "wrong password")
        else:
            messagebox.showinfo("Wrong username", "wrong username")


def passwordCheck(password):
    password_length = len(password)
    if password_length < 8:
        raise RuntimeError("The password is too short.")
    if password_length > 32:
        raise RuntimeError("The password is too long.")
    if " " in password:
        raise RuntimeError("Password can't contain space.")
    if "," in password:
        raise RuntimeError("Password can't contain a ','.")
    return True
def usernameCheck(username):
    username_length = len(username)
    if username_length < 8:
        raise RuntimeError("Username too short.")
    if username_length > 25:
        raise RuntimeError("Username too long.")
    if " " in username:
        raise RuntimeError("Username can't contain space.")
    if "," in username:
        raise RuntimeError("Username can't contain ','.")
    return True

def generatePassword(length=8):
    generator = LETTERS+NUMBERS+PUNCTUATION
    generator = list(generator)
    random.shuffle(generator)
    password = ''
    for i in range(length):
        password=password+generator[i]
    return password

class passwordManager:

    def __init__(self, master):
        self.root = master
        self.currentUser = None
        self.users = readUsers()
        self.currentUserAccounts = []
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.s = ttk.Style()
        self.s.configure("new.TFrame", background="#91b1b5")

        self.username = StringVar()
        self.password = StringVar()
        self.website = StringVar()

        self.loginFrame = loginFrame(self, readUsers())
    def loginDetails(self, *args):
        currentSelection = self.vaultContentsframe.accountListFrame.box.curselection()[0]
        self.username.set(self.currentUserAccounts[currentSelection].username)
        self.password.set(self.currentUserAccounts[currentSelection].password)
        self.website.set(self.currentUserAccounts[currentSelection].website)

    def mainWindow(self):
        self.root.unbind('<Return>')
        self.loginFrame.grid_remove()
        self.tabRoot = ttk.Notebook(self.root)
        self.vaultContentsframe = vaultContentsframe(self)
        self.passwordGeneratorFrame = generatorFrame(self)
        self.tabRoot.add(self.vaultContentsframe, text='Vault')
        self.tabRoot.add(self.passwordGeneratorFrame, text='Password Generator')
        self.tabRoot.grid(column=0, row=0, sticky=(N, E, S, W))

    def addNewaccount(self, *args):
        self.top = Toplevel(self.root)
        frame = newAccountframe(self)

    def updateCurrentUserAccounts(self):
        self.vaultContentsframe.accountListFrame.update()

root = Tk()
passMan = passwordManager(root)
root.mainloop()
