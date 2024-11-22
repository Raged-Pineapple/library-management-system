import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from flow1 import lend_book
from flow2 import send_return_alert
from flow3 import mark_book_returned

# Function to handle the submit button (First section)
def submit():
    name = name_entry.get()
    usn = usn_entry.get()
    book_id = book_id_entry.get()
    email = email_entry.get()

    if not name or not usn or not book_id or not email:
        messagebox.showwarning("Input Error", "Please fill all fields!")
    else:
        lend_book(name, usn, book_id, email)


# Function to handle the cancel button (First section)
def cancel():
    name_entry.delete(0, tk.END)
    usn_entry.delete(0, tk.END)
    book_id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# Function to handle the send alert button (Second section)
def send_alert():
    send_return_alert()


# Function to handle the returned button (Third section)
def returned():
    usn = returned_usn_entry.get()
    if not usn:
        messagebox.showwarning("Input Error", "Please enter a USN!")
    else:
        mark_book_returned(usn)


# Function to display only the selected section
def show_section():
    selected = section_var.get()
    section1_frame.pack_forget()
    section2_frame.pack_forget()
    section3_frame.pack_forget()

    if selected == 1:
        section1_frame.pack(pady=20)
    elif selected == 2:
        section2_frame.pack(pady=20)
    elif selected == 3:
        section3_frame.pack(pady=20)


# Create the main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("500x400")
root.configure(bg="#f5f5f5")

# Create a top frame for the logo and title
top_frame = tk.Frame(root, bg="#f5f5f5")
top_frame.pack(fill="x", pady=10)

# Add logo to the top frame
try:
    logo_image = Image.open("C:/Users/Dell/Downloads/professional logo for library management system app.png")
    logo_image = logo_image.resize((50, 50), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(top_frame, image=logo_photo, bg="#f5f5f5")
    logo_label.image = logo_photo
    logo_label.grid(row=0, column=0, padx=10)
except Exception as e:
    messagebox.showerror("Error loading logo", f"Couldn't load logo: {e}")

# Add title to the top frame
title_label = tk.Label(top_frame, text="Library Management System", font=("Helvetica", 18, "bold"), fg="#333", bg="#f5f5f5")
title_label.grid(row=0, column=1, sticky="w", padx=10)

# Adjust column weight for proper alignment
top_frame.grid_columnconfigure(1, weight=1)


# Create radio buttons to select sections
section_var = tk.IntVar(value=1)  # Set default section to 1

radio_frame = tk.Frame(root, bg="#f5f5f5")
radio_frame.pack(pady=10)

radio1 = tk.Radiobutton(radio_frame, text="Lend Book", variable=section_var, value=1, command=show_section, bg="#f5f5f5")
radio1.grid(row=0, column=0, padx=10)
radio2 = tk.Radiobutton(radio_frame, text="Send Alert", variable=section_var, value=2, command=show_section, bg="#f5f5f5")
radio2.grid(row=0, column=1, padx=10)
radio3 = tk.Radiobutton(radio_frame, text="Return Book", variable=section_var, value=3, command=show_section, bg="#f5f5f5")
radio3.grid(row=0, column=2, padx=10)

# Section 1: Accept Name, USN, Book ID, Email
section1_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)
name_label = tk.Label(section1_frame, text="Name:", bg="#ffffff")
name_label.grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(section1_frame)
name_entry.grid(row=0, column=1, pady=5)

usn_label = tk.Label(section1_frame, text="USN:", bg="#ffffff")
usn_label.grid(row=1, column=0, sticky="w", pady=5)
usn_entry = tk.Entry(section1_frame)
usn_entry.grid(row=1, column=1, pady=5)

book_id_label = tk.Label(section1_frame, text="Book ID:", bg="#ffffff")
book_id_label.grid(row=2, column=0, sticky="w", pady=5)
book_id_entry = tk.Entry(section1_frame)
book_id_entry.grid(row=2, column=1, pady=5)

email_label = tk.Label(section1_frame, text="Email:", bg="#ffffff")
email_label.grid(row=3, column=0, sticky="w", pady=5)
email_entry = tk.Entry(section1_frame)
email_entry.grid(row=3, column=1, pady=5)

submit_button = tk.Button(section1_frame, text="Submit", command=submit, bg="#4CAF50", fg="white")
submit_button.grid(row=4, column=0, pady=10)

cancel_button = tk.Button(section1_frame, text="Cancel", command=cancel, bg="#F44336", fg="white")
cancel_button.grid(row=4, column=1, pady=10)

# Section 2: Send Alert
section2_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove", padx=20, pady=20)
send_alert_button = tk.Button(section2_frame, text="Send Alert", command=send_alert, bg="#FF9800", fg="white")
send_alert_button.pack(pady=10)

# Section 3: Accept USN and Returned Book
section3_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove", padx=20, pady=20)
returned_usn_label = tk.Label(section3_frame, text="Enter USN:", bg="#ffffff")
returned_usn_label.pack(pady=5)

returned_usn_entry = tk.Entry(section3_frame)
returned_usn_entry.pack(pady=5)

returned_button = tk.Button(section3_frame, text="Mark as Returned", command=returned, bg="#4CAF50", fg="white")
returned_button.pack(pady=10)

# Initially display the first section
show_section()

# Start the Tkinter event loop
root.mainloop()
