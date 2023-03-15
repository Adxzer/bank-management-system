""" -----------------------------------------------------------
Bank management system with Tkinter GUI and MySQL database. The
program is a simple bank management system that allows the user
to create a new account, deposit money, withdraw money, and view
account details.

(C) 2023 Adam Persson, Vellinge, Sweden
email: adambenjamin.persson@edu.vellinge.se
----------------------------------------------------------- """

# Import the tkinter and mysql libraries to use their classes.
import tkinter as tk
import mysql.connector

# Setup the database connection.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

# Configure the root window.
root = tk.Tk()
root.title("List Browser")
root.geometry("330x300")
root.resizable(False, False)

def clearInterface():
    # Loop the interface and destroy all widgets
    for interface in root.winfo_children():
        interface.destroy()

def login_interface():
    # Clear the interface before creating a new one.
    clearInterface()

    # Create root widgets for the login screen.
    username_label = tk.Label(root, text="Username")
    username_entry = tk.Entry(root, width=30)
    password_label = tk.Label(root, text="Password")
    password_entry = tk.Entry(root, width=30, show="*")
    header_label = tk.Label(root, text="DIGITAL BANK", font=("Arial", 14, "bold"))
    login_button = tk.Button(root, text="Login", width=15, height=1)
    sing_up_button = tk.Button(root, text="Sign up", width=10, height=1, border=0, font=("Arial", 9, "italic"))

    # Place the root widgets.
    header_label.place(x=93, y=20)
    username_label.place(x=75, y=70)
    username_entry.place(x=70, y=90)
    password_label.place(x=75, y=120)
    password_entry.place(x=70, y=140)
    login_button.place(x=105, y=195)
    sing_up_button.place(x=123, y=235)

    # Start the root main loop.
    root.mainloop()

login_interface()