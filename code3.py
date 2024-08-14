import tkinter
import random
from tkinter import ttk
from tkinter import messagebox


global first_name_entry, last_name_entry, item_combobox, amount_spinbox 

window = tkinter.Tk()
window.title('Julies Hire Page')
window.geometry('450x250')
frame = tkinter.Frame(window, width=100, height=200)
title_name_label = tkinter.Label(window, text="Julie's Party Hire", font=("Comic Sans", 16, "italic"))
title_name_label.place(x=150, y=15)



def generate_receipt_number():
    while True:
        randInt = random.randint(100000, 999999)
        if randInt not in used_receipt_numbers:
            used_receipt_numbers.add(randInt)
            return randInt
        
used_receipt_numbers = set()
        
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

    def get_new_receipt_number():
        return generate_receipt_number()

    
    
    def receipt_details(): 
        window_hire_details = tkinter.Toplevel()
        window_hire_details.title('Details Page')
        window_hire_details.geometry('450x250')

        

        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        item = item_combobox.get()
        amount = amount_spinbox.get()
        receipt_number = get_new_receipt_number()
        
        
        
        tkinter.Label(window_hire_details, text=f"Receipt Number : {receipt_number}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"First Name : {first_name}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Last Name : {last_name}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Item Chosen : {item}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Amount : {amount}").pack(pady=5)


    append_button = tkinter.Button(window_hire, text="Append Details", command=receipt_details)
    append_button.place(x=250, y=150, width=100)

    

    
    

    

    
    

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

