from tkinter import *
window_approve = Tk()
window_approve.title("  APPROVE  ")
window_approve.geometry("500x500")

def approve():

    heading_lable = Label(window_approve,text="Approve",width=50,font={"times new roman",100,"bold"}).place(x=3,y=30)

    request_by = StringVar()
    application_by = StringVar()


    request_by_label = Label(window_approve,text="Request By :",width=15,font={"ariel",10})
    request_by_label.place(x=5,y=105)

    request_by_entry = Entry(window_approve,textvar = request_by).place(x=200,y=105)

    application_by_label = Label(window_approve,text="Application By :",width=17,font={"ariel",10})
    application_by_label.place(x=5,y=135)

    application_by_entry = Entry(window_approve,textvar=application_by).place(x=200,y=135)

    approve_status_label = Label(window_approve,text="Approve Status",width=17,font={"ariel",10})
    approve_status_label.place(x=5,y=165)

    approved_items_label = Label(window_approve,text="Approved Items",width=17,font={"ariel",10})
    approved_items_label.place(x=5,y=195)

    current_stage_label = Label(window_approve,text="Current Stage", width=16, font={"ariel", 10})
    current_stage_label.place(x=5, y=195)

    submit_button = Button(window_approve,text="Submit",width= 10,fg = "Green",font={"ariel", 13, "bold"})
    submit_button.place(x=100,y=245)
    cancel_button = Button(window_approve, text="Cancel", width=10, fg="Red", font={"ariel", 13, "bold"})
    cancel_button.place(x=225, y=245)

approve()

window_approve.mainloop()