from tkinter import *
window_reject = Tk()
window_reject.title(" REJECT ")
window_reject.geometry("500x500")

def reject():
    heading_label = Label(window_reject,text="REJECT",width=50,font={"times new roman",100,"bold"})
    heading_label.place(x=3,y=30)
    application_by_label = Label(window_reject, text="Application By", width=50, font={"times new roman", 100, "bold"})
    application_by_label.place(x=5, y=100)
    status_label = Label(window_reject, text="Status", width=50, font={"times new roman", 100, "bold"})
    status_label.place(x=5, y=150)
    reject_by_label = Label(window_reject, text="Reject By", width=50, font={"times new roman", 100, "bold"})
    reject_by_label.place(x=5, y=200)
    reason_label = Label(window_reject, text="Reason", width=50, font={"times new roman", 100, "bold"})
    reason_label.place(x=5, y=250)

reject()
window_reject.mainloop()