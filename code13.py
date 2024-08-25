import tkinter
import random
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


# Declare global variables
global first_name_entry, last_name_entry, item_combobox, amount_spinbox 

# Create the main application window
window = tkinter.Tk()
window.title('Julies Hire Page')
window.geometry('450x300')
window.configure(bg='#b5dce9')


# Set to store used receipt numbers to avoid repeats
used_receipt_numbers = set()

# Function to generate a unique 4-digit receipt number
def generate_receipt_number():
    while True:
        randInt = random.randint(1000, 9999)
        if randInt not in used_receipt_numbers:
            used_receipt_numbers.add(randInt)
            return randInt

# Function to save the receipt data to a text file
def save_receipt_data(receipt_number, first_name, last_name, item, amount):
    with open("receipts.txt", "a") as file:
        file.write(f"{receipt_number},{first_name},{last_name},{item},{amount}\n")

# Function to load receipt data from the text file based on the receipt number
def load_receipt_data(receipt_number):
    with open("receipts.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == str(receipt_number):
                return data
    return None

# Function to delete receipt data from the text file based on the receipt number
def delete_receipt_data(receipt_number):
    lines = []
    with open("receipts.txt", "r") as file:
        lines = file.readlines()
    
    with open("receipts.txt", "w") as file:
        for line in lines:
            if line.strip().split(",")[0] != str(receipt_number):
                file.write(line)

logo = Image.open("image1.png").resize((200, 100))
logo_image = ImageTk.PhotoImage(logo)

img_label = tkinter.Label(window, image=logo_image)
img_label.image = logo_image 
img_label.place(x=150, y=1, width=200, height=100)

# Function to open the "Hire" page window
def hire_a():
    window_hire = tkinter.Toplevel()
    window_hire.title('Hire Page')
    window_hire.geometry('400x300')
    window_hire.configure(bg='#b5dce9')

    # Input validation functions
    def check_length(name):
        return len(name) <= 20

    def check_entry(name):
        return name.isalpha()

    def check_empty(name):
        return name != ""

    def check_value(amount):
        try:
            amount = int(amount)
            return 1 <= amount <= 500
        except ValueError:
            return False

    def check_item_selection(item):
        return item in item_combobox['values']

    # Labels and input fields for first name, last name, item selection, and amount
    title_label = tkinter.Label(window_hire, text="H I R E", font=("Georgia", 16), bg='#b5dce9')
    title_label.place(x=150, y=15, width=100)
    
    first_name_label = tkinter.Label(window_hire, text="First Name", bg="white", bd=1, relief="ridge")
    first_name_label.place(x=90, y=50, width=75)
    
    first_name_entry = tkinter.Entry(window_hire)
    first_name_entry.place(x=190, y=50)

    last_name_label = tkinter.Label(window_hire, text="Last Name", bg="white", bd=1, relief="ridge")
    last_name_label.place(x=90, y=100, width=75)
    
    last_name_entry = tkinter.Entry(window_hire)
    last_name_entry.place(x=190, y=100)

    item_label = tkinter.Label(window_hire, text="Hire Option", bg="white", bd=1, relief="ridge")
    item_label.place(x=90, y=150, width=75)

    item_combobox = ttk.Combobox(window_hire, values=["Balloons", "Plates", "Spoons"], state='readonly')
    item_combobox.place(x=190, y=150)

    amount_label = tkinter.Label(window_hire, text="Item amount", bg="white", bd=1, relief="ridge")
    amount_label.place(x=90, y=200, width=75)

    amount_spinbox = tkinter.Spinbox(window_hire, from_=1, to=500)
    amount_spinbox.place(x=190, y=200)

    # Button to close the "Hire" window and return to the main window
    home_button = tkinter.Button(window_hire, text="Home", command=window_hire.destroy)
    home_button.place(x=75, y=250, width=100)

    # Function to validate inputs and create a receipt if valid
    def validate_inputs():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        item = item_combobox.get()
        amount = amount_spinbox.get()

        # Validate first name
        if not check_empty(first_name):
            messagebox.showerror("Error", "First name cannot be left blank")
            return
        
        if not check_length(first_name):
            messagebox.showerror("Error", "First name can't be more than 20 characters long")
            return
        if not check_entry(first_name):
            messagebox.showerror("Error", "First name can only contain letters ")
            return

        # Validate last name
        if not check_empty(last_name):
            messagebox.showerror("Error", "Last name cannot be left blank")
            return
            
        if not check_length(last_name):
            messagebox.showerror("Error", "Last name can't be more than 20 characters long")
            return
        if not check_entry(last_name):
            messagebox.showerror("Error", "Last name can only contain letters")
            return

        # Validate item selection and amount
        if not check_item_selection(item):
            messagebox.showerror("Error", "Please select a valid item from the dropdown menu")
            return
        if not check_value(amount):
            messagebox.showerror("Error", "Amount must be a number between 1 and 500")
            return

        # If all validations pass, create the receipt
        receipt_number = generate_receipt_number()
        receipt_details(receipt_number, first_name, last_name, item, amount)

    # Function to display the receipt details in a new window and save the data
    def receipt_details(receipt_number, first_name, last_name, item, amount): 
        window_hire_details = tkinter.Toplevel()
        window_hire_details.title('Details Page')
        window_hire_details.geometry('250x250')
        window_hire_details.configure(bg='#b5dce9')

        tkinter.Label(window_hire_details, text=f"Receipt Number : {receipt_number}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"First Name : {first_name}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Last Name : {last_name}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Item Chosen : {item}").pack(pady=5)
        tkinter.Label(window_hire_details, text=f"Amount : {amount}").pack(pady=5)

        # Button to close the receipt details window
        close_button = tkinter.Button(window_hire_details, text="Close", command=window_hire_details.destroy)
        close_button.pack(pady=10)

        # Save the receipt data to a file
        save_receipt_data(receipt_number, first_name, last_name, item, amount)

    # Button to append details (trigger input validation and receipt creation)
    append_button = tkinter.Button(window_hire, text="Append Details", command=validate_inputs)
    append_button.place(x=225, y=250, width=100)

# Function to open the "Return" page window
def return_a():
    window_return = tkinter.Toplevel()
    window_return.title('Return Page')
    window_return.geometry('400x200')
    window_return.configure(bg='#b5dce9')

    title_label = tkinter.Label(window_return, text="R E T U R N", font=("Georgia", 16), bg='#b5dce9')
    title_label.place(x=100, y=15, width=200)

    # Function to confirm return of an item based on receipt number
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
    
    # Label and input field for entering receipt number
    receipt_label = tkinter.Label(window_return, text="Enter Receipt Number:")
    receipt_label.place(x=125, y=50, width=150)
    
    receipt_entry = tkinter.Entry(window_return)
    receipt_entry.place(x=150, y=75, width=100)
    
    # Button to confirm the return process
    return_button = tkinter.Button(window_return, text="Confirm Return", command=confirm_return)
    return_button.place(x=150, y=100, width=100)

    # Button to close the "Return" window
    close_button = tkinter.Button(window_return, text="Close", command=window_return.destroy)
    close_button.place(x=150, y=135, width=100)
    
# Function to open the "View Receipts" page window
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


    

# Create a button that opens the "Hire" page when clicked
hire_button = tkinter.Button(window, text="Hire", command=hire_a)
hire_button.pack(padx=10, pady=40)
hire_button.place(x=175, y=65, width=100)
# Create a button that opens the "return" page when clicked
return_button = tkinter.Button(window, text="Return", command=return_a)
return_button.pack(padx=10, pady=40)
return_button.place(x=175, y=105, width=100)

# Create a button that opens the "View Receipts" page when clicked
viewreceipt_button = tkinter.Button(window, text="View Receipt", command=receipt_a)
viewreceipt_button.pack(padx=10, pady=40)
viewreceipt_button.place(x=175, y=145, width=100)

# Create a button that quits the application when clicked
quit_button = tkinter.Button(window, text="Quit", command=quit_a)
quit_button.pack(padx=10, pady=40)
quit_button.place(x=175, y=185, width=100)
# Start the Tkinter event loop
window.mainloop()

