from tkinter import *
window_dashboard = Tk()
window_dashboard.title(" DASHBOARD ")
window_dashboard.geometry("500x500")

#def dashboard():
heading_label = Label(window_dashboard,text="DASHBOARD",width=50,font={"times new roman",100,"bold"})
heading_label.place(x=30,y=30)
request_button = Button(window_dashboard, text="Request", width=20, font={"times new roman", 100, "bold"})
request_button.place(x=150, y=100)
approve_button = Button(window_dashboard, text="Approve", width=20, font={"times new roman", 100, "bold"})
approve_button.place(x=150, y=150)
reject_button = Button(window_dashboard, text="Reject", width=20, font={"times new roman", 100, "bold"})
reject_button.place(x=150, y=200)
pending_button = Button(window_dashboard, text="Pending", width=20, font={"times new roman", 100, "bold"})
pending_button.place(x=150, y=250)

#dashboard()
window_dashboard.mainloop()