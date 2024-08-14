import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title('Julies Hire Page')
window.geometry('450x250')
frame = tkinter.Frame(window, width=100, height=200)
title_name_label = tkinter.Label(window, text="Julie's Party Hire", font=("Comic Sans", 16, "italic"))
title_name_label.place(x=150, y=15)

def hire_a():
    window_hire = tkinter.Toplevel()
    window_hire.title('Hire Page')
    window_hire.geometry('450x250')

    first_name_label = tkinter.Label(window_hire, text="First Name:")
    first_name_label.place(x=80, y=25)
    
    first_name_entry = tkinter.Entry(window_hire)
    first_name_entry.place(x=50, y=50)

    last_name_label = tkinter.Label(window_hire, text="Last Name:")
    last_name_label.place(x=255, y=25)
    
    last_name_entry = tkinter.Entry(window_hire)
    last_name_entry.place(x=225, y=50)

    item_label = tkinter.Label(window_hire, text="Hire Option")
    item_label.place(x=80, y=75)

    item_combobox = ttk.Combobox(window_hire, values=["Item 1", "Item 2", "Item 3"])
    item_combobox.place(x=50, y=100)

    amount_label = tkinter.Label(window_hire, text="Item amount")
    amount_label.place(x=250, y=75)

    amount_spinbox = tkinter.Spinbox(window_hire, from_=1, to=500)
    amount_spinbox.place(x=225, y=100)

    home_button = tkinter.Button(window_hire, text="Home", command=window_hire.destroy)
    home_button.place(x=70, y=150, width=100)

    append_button = tkinter.Button(window_hire, text="Append Details", command=append_details)
    append_button.place(x=250, y=150, width=100)

def append_details():
    window_hire_details = tkinter.Toplevel()
    window_hire.title('Details Page')
    window_hire.geometry('450x250')

    
    

    

    
    

def return_a():
    window_hire = tkinter.Toplevel()
    window_hire.title('Return Page')
    window_hire.geometry('450x250')

def receipt_a():
    window_hire = tkinter.Toplevel()
    window_hire.title('View Receipt Page')
    window_hire.geometry('450x250')

def quit_a():
    window.destroy()


hire_button = tkinter.Button(window, text="Hire", command=hire_a)
hire_button.pack(padx=10, pady=40)
hire_button.place(x=175, y=45, width=100)

return_button = tkinter.Button(window, text="Return", command=return_a)
return_button.pack(padx=10, pady=40)
return_button.place(x=175, y=85, width=100)


viewreceipt_button = tkinter.Button(window, text="View Receipt", command=receipt_a)
viewreceipt_button.pack(padx=10, pady=40)
viewreceipt_button.place(x=175, y=125, width=100)


quit_button = tkinter.Button(window, text="Quit", command=quit_a)
quit_button.pack(padx=10, pady=40)
quit_button.place(x=175, y=165, width=100)

window.mainloop()

