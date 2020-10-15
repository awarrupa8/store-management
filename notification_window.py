from tkinter import *
window_notification = Tk()
window_notification.title(" NOTIFICATION ")
window_notification.geometry("500x500")

def notification():
    heading_label = Label(window_notification,text="NOTIFICATION",width=50,font={"times new roman",100,"bold"})
    heading_label.place(x=3,y=30)
    request_pending_list_label = Label(window_notification, text="Request Pending List By Authority ", width=50, font={"times new roman", 100, "bold"})
    request_pending_list_label.place(x=5, y=100)

notification()
window_notification.mainloop()