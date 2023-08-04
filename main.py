import requests
import tkinter as tk
from tkinter import simpledialog, messagebox

# Define the URL globally
url = "https://phonenumbervalidatefree.p.rapidapi.com/ts_PhoneNumberValidateTest.jsp"

def get_phone_data():
    # Retrieve phone number and country initials from the input fields
    phone_number = phone_number_entry.get()
    country_initials = country_initials_entry.get()

    querystring = {"number": phone_number, "country": country_initials}

    headers = {
        "X-RapidAPI-Key": "YOUR API KEY HERE",
        "X-RapidAPI-Host": "phonenumbervalidatefree.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Prepare the result message
    result_message = "\n".join([f"{key}: {value}" for key, value in data.items()])
    # Show the result in a message box
    messagebox.showinfo("Phone Data Result", result_message)


# Create the main window
root = tk.Tk()
root.title("Phone Data Checker")

# Create and place labels and input fields
tk.Label(root, text="Phone Number").grid(row=0, column=0, padx=10, pady=10)
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Country Initials").grid(row=1, column=0, padx=10, pady=10)
country_initials_entry = tk.Entry(root)
country_initials_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the 'Check' button
check_button = tk.Button(root, text="Check", command=get_phone_data)
check_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
