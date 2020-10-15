from tkinter import  *
import db_connectivity_files.connector_file
import tkinter.messagebox
#import os
window_login=Tk()
username = StringVar()
password = StringVar()

def validateuser_ui():
    name= username.get()
    passwd= password.get()
    #passw = password.get()
    print(name,passwd,"username and password")
    object = db_connectivity_files.connector_file.storemanagement()
    object.makeconnection()
    #print("return value:",object.validateuser(name,passwd))
    if object.validateuser(name,passwd) ==1:
        window_login.destroy()
        exec(open("dashboard.py").read())
        #os.system("stud_dashboard.py")
        #tkinter.messagebox.showinfo("success","login Successful")
    else:
        tkinter.messagebox.showinfo("Failed","Enter Valid username and password")

window_login.title("Login Window")
window_login.geometry("370x300")
#login name text box
usernamelabel= Label(window_login,text="User name:",width=20,font={"ariel",10,"bold"})
usernamelabel.place(x=5,y=35)

#login name text box
uname = Entry(window_login,textvar = username).place(x= 150,y= 35)

# password widget
passwordlable = Label(window_login, text="Password:", width=20, font={"ariel", 10, "bold"})
passwordlable.place(x=5, y=135)

pwdentry = Entry(window_login,textvar = password,show='* ').place(x=150, y=135)

# login button
loginbutton = Button(window_login,text= "login", width= 11,fg = "white",command = validateuser_ui, bg = "brown",font={"ariel", 13, "bold"})
loginbutton.place(x=30,y=235)

window_login.mainloop()
