import tkinter as tk
from tkinter import messagebox
import re


def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)


def validate_phone(phone_number):
    regex = r'^[0-1-2-3-4-5-6-7-8-9]+$'
    return re.match(regex, phone_number)



# Function to save user data and show the information
def register_user():
    # Get user input from the entry widgets
    username = entry_username.get()
    password = entry_password.get()
    
    confirm_password = entry_confirmpassword.get()

    email = entry_email.get()
    full_name = entry_full_name.get()
    phone_number = entry_phone.get()
    

    # Simple validation: Check if any field is empty
    if not username or not password or not confirm_password  or not email or not full_name or not phone_number :
        messagebox.showerror("Error", "All fields are required!")
        return
    

     # Check if email is valid
    if not validate_email(email):
        messagebox.showwarning("Input Error", "Please enter a valid email address.")
        return
    
    if not validate_phone(phone_number):
        messagebox.showwarning("Input Error", "Please enter a valid phone number.")
        return 
    
    # Check if passwords match
    if password != confirm_password:
        messagebox.showwarning("Password Error", "Passwords do not match.")
        return


    # Create a dictionary to hold the user data
    user_data = {
        'Username': username,
        'Password': password,
        'Confirm password' : confirm_password, 
        'Email': email,
        'Full Name': full_name,
        'Phone Number': phone_number
    }

    

    # Save data to a file
    with open("user_data.txt", "a") as file:
        file.write(str(user_data) + "\n")

    # Show the user data in a message box
    user_info = f"Username: {username}\nPassword: {password}\nConfirm Password : {confirm_password} \nEmail: {email}\nFull Name: {full_name}\nPhone Number: {phone_number}"
    messagebox.showinfo("Registration Successful", f"User Registered Successfully!\n\n{user_info}")

    # Clear the form fields
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_confirmpassword.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_full_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("User Registration Form")

# Create labels and entry widgets for the form
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, pady=5, padx=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, pady=5, padx=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, pady=5, padx=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, pady=5, padx=10)


label_password = tk.Label(root, text="Confrim Password:")
label_password.grid(row=2, column=0, pady=5, padx=10)
entry_confirmpassword = tk.Entry(root, show="*")
entry_confirmpassword.grid(row=2, column=1, pady=5, padx=10)


label_email = tk.Label(root, text="Email:")
label_email.grid(row=3, column=0, pady=5, padx=10)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1, pady=5, padx=10)

label_full_name = tk.Label(root, text="Full Name:")
label_full_name.grid(row=4, column=0, pady=5, padx=10)
entry_full_name = tk.Entry(root)
entry_full_name.grid(row=4, column=1, pady=5, padx=10)

label_phone = tk.Label(root, text="Phone Number:")
label_phone.grid(row=5, column=0, pady=5, padx=10)
entry_phone = tk.Entry(root)
entry_phone.grid(row=5, column=1, pady=5, padx=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=register_user)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)

# Start the GUI loop
root.mainloop()
