from tkinter import *
window_request = Tk()
window_request.title("  REQUEST  ")
window_request.geometry("500x500")
def request():

    heading_lable = Label(window_request,text="Request",width=50,font={"times new roman",100,"bold"}).place(x=3,y=30)

    request_no = IntVar()
    request_by = StringVar()
    application_by = StringVar()
    estimate_by = StringVar()
    description = StringVar()

    request_sr_no_label = Label(window_request,text="Request Sr. No. :",width=18,font={"ariel",10})
    request_sr_no_label.place(x=5,y=75)

    request_sr_no_entry = Entry(window_request,textvar = request_no).place(x=200,y=75)

    request_by_label = Label(window_request,text="Request By :",width=15,font={"ariel",10})
    request_by_label.place(x=5,y=105)

    request_by_entry = Entry(window_request,textvar = request_by).place(x=200,y=105)

    application_by_label = Label(window_request,text="Application By :",width=17,font={"ariel",10})
    application_by_label.place(x=5,y=135)

    application_by_entry = Entry(window_request,textvar=application_by).place(x=200,y=135)

    estimate_by_label = Label(window_request,text="Estimate By :",width=15,font={"ariel",10})
    estimate_by_label.place(x=5,y=165)

    estimate_by_entry = Entry(window_request,textvar=estimate_by).place(x=200,y=165)

    description_label = Label(window_request,text="Description :",width=15,font={"ariel",10})
    description_label.place(x=5,y=195)

    description_entry = Entry(window_request,textvar=description).place(x=200,y=195)

    submit_button = Button(window_request,text="Submit",width= 10,fg = "Green",font={"ariel", 13, "bold"})
    submit_button.place(x=100,y=245)
    cancel_button = Button(window_request, text="Cancel", width=10, fg="Red", font={"ariel", 13, "bold"})
    cancel_button.place(x=225, y=245)

request()

window_request.mainloop()