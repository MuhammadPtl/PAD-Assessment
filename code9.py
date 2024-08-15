import tkinter
import random
from tkinter import ttk
from tkinter import messagebox

global first_name_entry, last_name_entry, item_combobox, amount_spinbox 

window = tkinter.Tk()
window.title('Julies Hire Page')
window.geometry('450x250')
window.configure(bg='#b5dce9')
frame = tkinter.Frame(window, width=100, height=200)


used_receipt_numbers = set()

def generate_receipt_number():
    while True:
        randInt = random.randint(1000, 9999)
        if randInt not in used_receipt_numbers:
            used_receipt_numbers.add(randInt)
            return randInt

def save_receipt_data(receipt_number, first_name, last_name, item, amount):
    with open("receipts.txt", "a") as file:
        file.write(f"{receipt_number},{first_name},{last_name},{item},{amount}\n")

def load_receipt_data(receipt_number):
    with open("receipts.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == str(receipt_number):
                return data
    return None

def delete_receipt_data(receipt_number):
    lines = []
    with open("receipts.txt", "r") as file:
        lines = file.readlines()
    
    with open("receipts.txt", "w") as file:
        for line in lines:
            if line.strip().split(",")[0] != str(receipt_number):
                file.write(line)

def hire_a():
    window_hire = tkinter.Toplevel()
    window_hire.title('Hire Page')
    window_hire.geometry('400x300')
    window_hire.configure(bg='#b5dce9')

    def check_length(name):
        return len(name) <= 20

    def check_entry(name):
        return name.isalpha()

    def check_empty(name):
        return name !=""

    def check_value(amount):
        try:
            amount = int(amount)
            return 1 <= amount <= 500
        except ValueError:
            return False

    def check_item_selection(item):
        return item in item_combobox['values']

    first_name_label = tkinter.Label(window_hire, text="First Name", bg="white", bd=1, relief="ridge")
    first_name_label.place(x=90, y=25, width=75)
    
    first_name_entry = tkinter.Entry(window_hire)
    first_name_entry.place(x=190, y=25)

    last_name_label = tkinter.Label(window_hire, text="Last Name", bg="white", bd=1, relief="ridge")
    last_name_label.place(x=90, y=75, width=75)
    
    last_name_entry = tkinter.Entry(window_hire)
    last_name_entry.place(x=190, y=75)

    item_label = tkinter.Label(window_hire, text="Hire Option", bg="white", bd=1, relief="ridge")
    item_label.place(x=90, y=125, width=75)

    item_combobox = ttk.Combobox(window_hire, values=["Item 1", "Item 2", "Item 3"])
    item_combobox.place(x=190, y=125)

    amount_label = tkinter.Label(window_hire, text="Item amount", bg="white", bd=1, relief="ridge")
    amount_label.place(x=90, y=175, width=75)

    amount_spinbox = tkinter.Spinbox(window_hire, from_=1, to=500)
    amount_spinbox.place(x=190, y=175)

    home_button = tkinter.Button(window_hire, text="Home", command=window_hire.destroy)
    home_button.place(x=75, y=225, width=100)

    def validate_inputs():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        item = item_combobox.get()
        amount = amount_spinbox.get()

        if not check_empty(first_name):
            messagebox.showerror("Error", "First name cannot be left blank")
        
        if not check_length(first_name):
            messagebox.showerror("Error", "First name can't be more than 20 characters long")
            return
        if not check_entry(first_name):
            messagebox.showerror("Error", "First name can only contain letters ")
            return
        if not check_empty(last_name):
            messagebox.showerror("Error", "Last name cannot be left blank")
            
        if not check_length(last_name):
            messagebox.showerror("Error", "Last name can't be more than 20 characters long")
            return
        if not check_entry(last_name):
            messagebox.showerror("Error", "Last name can only contain letters")
            return
        if not check_item_selection(item):
            messagebox.showerror("Error", "Please select a valid item from the dropdown menu")
            return
        if not check_value(amount):
            messagebox.showerror("Error", "Amount must be a number between 1 and 500")
            return

        # If all validations pass, create the receipt
        receipt_number = generate_receipt_number()
        receipt_details(receipt_number, first_name, last_name, item, amount)

    def receipt_details(receipt_number, first_name, last_name, item, amount): 
        window_hire_details = tkinter.Toplevel()
        window_hire_details.title('Details Page')
        window_hire_details.geometry('450x250')
        window_hire_details.configure(bg='#b5dce9')

        tkinter.Label(window_hire_details, text=f"Receipt Number : {receipt_number}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"First Name : {first_name}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Last Name : {last_name}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Item Chosen : {item}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Amount : {amount}").pack(pady=5)
        close_button = tkinter.Button(window_hire_details, text="Close", command=window_hire_details.destroy)
        close_button.pack(pady=10)

        save_receipt_data(receipt_number, first_name, last_name, item, amount)

    append_button = tkinter.Button(window_hire, text="Append Details", command=validate_inputs)
    append_button.place(x=225, y=225, width=100)

def return_a():
    window_return = tkinter.Toplevel()
    window_return.title('Return Page')
    window_return.geometry('450x250')
    window_return.configure(bg='#b5dce9')

    def confirm_return():
        receipt_number = receipt_entry.get()

        if not receipt_number.isdigit() or len(receipt_number) != 4:
            messagebox.showerror("Error", "Receipt number must be a 4-digit number")
            return
        
        receipt_data = load_receipt_data(receipt_number)
        
        if receipt_data:
            confirm = messagebox.askyesno("Confirm Return", f"Are you sure you want to return:\n\n"
                                                           f"Receipt Number: {receipt_data[0]}\n"
                                                           f"First Name: {receipt_data[1]}\n"
                                                           f"Last Name: {receipt_data[2]}\n"
                                                           f"Item: {receipt_data[3]}\n"
                                                           f"Amount: {receipt_data[4]}\n")
            if confirm:
                delete_receipt_data(receipt_number)
                messagebox.showinfo("Return Processed", "The item(s) have been successfully returned.")     
        else:
            messagebox.showerror("Error", "Receipt not found")
    
    receipt_label = tkinter.Label(window_return, text="Enter Receipt Number:")
    receipt_label.pack(pady=5)
    
    receipt_entry = tkinter.Entry(window_return)
    receipt_entry.pack(pady=5)
    
    return_button = tkinter.Button(window_return, text="Confirm Return", command=confirm_return)
    return_button.pack(pady=5)

    close_button = tkinter.Button(window_return, text="Close", command=window_return.destroy)
    close_button.pack(pady=10)

def receipt_a():
    window_receipt = tkinter.Toplevel()
    window_receipt.title('View Receipts Page')
    window_receipt.geometry('600x400')
    window_receipt.configure(bg='#b5dce9')

    # Frame for displaying all receipts
    display_frame = tkinter.Frame(window_receipt)
    display_frame.pack(fill=tkinter.BOTH, expand=True, pady=10, padx=10)

    # Scrollbar and Text widget to display receipts
    receipt_text = tkinter.Text(display_frame, wrap=tkinter.NONE, width=80, height=20)
    receipt_text.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

    # Load all receipts and display them
    def load_and_display_receipts():
        try:
            with open("receipts.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    for line in lines:
                        data = line.strip().split(",")
                        receipt_text.insert(tkinter.END, f"Receipt Number: {data[0]}\n")
                        receipt_text.insert(tkinter.END, f"First Name: {data[1]}\n")
                        receipt_text.insert(tkinter.END, f"Last Name: {data[2]}\n")
                        receipt_text.insert(tkinter.END, f"Item: {data[3]}\n")
                        receipt_text.insert(tkinter.END, f"Amount: {data[4]}\n")
                        receipt_text.insert(tkinter.END, "-"*40 + "\n")
                else:
                    receipt_text.insert(tkinter.END, "No receipts found.")
        except FileNotFoundError:
            receipt_text.insert(tkinter.END, "Receipts file not found.")

    load_and_display_receipts()

    # Button to close the window
    close_button = tkinter.Button(window_receipt, text="Close", command=window_receipt.destroy)
    close_button.pack(pady=10)



def quit_a():
    confirm = messagebox.askyesno("Confirm Exit", "Are you sure you want to quit?")
    if confirm:
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

