from tkinter import *
import os
import subprocess


root = Tk()
root.title("Login Window")
canvas = Canvas(root, width=640, height=480, bg="black")
canvas.pack()


# title1
text1 = Label(root, text="Connect to your Instagram to see!!",
              fg="maroon", bg="black", width=40)
text1.config(font=("MS Sans Serif", 15))
text1.place(relx=0.10, rely=0.3)

# the username label
usernameLabel = Label(root, text="Username:",
                      fg="SkyBlue2", bg="black")
usernameLabel.place(relx=0.3, rely=0.4)


# creating field for username input
username = Entry(root, fg="maroon", bg="black", borderwidth=3)
username.place(relx=0.4, rely=0.4)

# what happens when you click the login button


def click():
    from Not_Followers import InstaBot
    Selenium = InstaBot(username.get(), password.get())
    Selenium.get_unfollowers()
    Selenium.closing()
    root.destroy()
    subprocess.call([r'D:\Programe\Python_Stuff\InstaBot\Opener.bat'])


my_file = open(
    r"D:\Programe\Python_Stuff\InstaBot\Not_Followers.txt", "r+")
my_file.truncate(0)
my_file.close()

# the password label
passwordLabel = Label(root, text="Password:",
                      fg="SkyBlue2", bg="black")
passwordLabel.place(relx=0.3, rely=0.45)


# creating field for password input
password = Entry(root, fg="maroon", bg="black", borderwidth=3, show='*')
password.place(relx=0.4, rely=0.45)


# creating the login button
login = Button(root, text="Login", bg="black", fg="maroon", command=click)
login.place(relx=0.3, rely=0.6, width=200)


root.mainloop()
