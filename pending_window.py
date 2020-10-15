from tkinter import *
window_pending = Tk()
window_pending.title(" PENDING ")
window_pending.geometry("500x500")

def pending():
    heading_label = Label(window_pending,text="PENDING",width=50,font={"times new roman",100,"bold"})
    heading_label.place(x=3,y=30)
    application_by_label = Label(window_pending, text="Application By", width=50, font={"times new roman", 100, "bold"})
    application_by_label.place(x=5, y=100)
    request_overview_label = Label(window_pending, text="Request Overview", width=50, font={"times new roman", 100, "bold"})
    request_overview_label.place(x=5, y=150)

pending()
window_pending.mainloop()