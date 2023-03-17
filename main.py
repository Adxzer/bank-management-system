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
    database="bankmanagementdb"
)

# Create a cursor to execute SQL queries.
mycursor = mydb.cursor()

# Create the database & main tables if it doesn't exist.
mycursor.execute("CREATE DATABASE IF NOT EXISTS bankmanagementdb")
mycursor.execute("CREATE TABLE IF NOT EXISTS accounts (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), gmail VARCHAR(255), password VARCHAR(255), balance INT)")

# Configure the root window.
root = tk.Tk()
root.title("Digital Bank")
root.geometry("330x300")
root.resizable(False, False)

def signup_connect(username, gmail, password):    
    # Check if the username is already taken.
    mycursor.execute("SELECT username FROM accounts")
    usernames = mycursor.fetchall()
    for user_main in usernames:
        for user_fetch in user_main:
            if user_fetch == username:
                return
        
    # Check if the gmail is already taken.
    mycursor.execute("SELECT gmail FROM accounts")
    gmails = mycursor.fetchall()
    for gmail_main in gmails:
        for gmail_fetch in gmail_main:
            if gmail_fetch == gmail:
                return
        
    # Check if the password is too short.
    if len(password) < 8:
        return
    
    # Check if the username is too short or long.
    if len(username) < 8 and len(username) > 32:
        return
    
    # Check if the gmail is too short or long.
    if "@gmail.com" not in gmail:
        return
    else:
        if len(gmail) < 8 and len(gmail) > 32:
            return

    # Insert the new account into the database.
    mycursor.execute("INSERT INTO accounts (username, gmail, password, balance) VALUES (%s, %s, %s, %s)", (username, gmail, password, 0))
    mydb.commit()
    login_click(username)
    
def login_connect(username, password):
    # Check if the password is correct for the gmail.
    mycursor.execute("SELECT password FROM accounts WHERE username = %s", (username,))
    passwords = mycursor.fetchall()
    for password_main in passwords:
        for password_fetch in password_main:
            if password_fetch == password:
                login_click(username)
                return
            
def deposit_connect(username, amount):
    # Check if the amount is a number.
    if not amount.isdigit():
        return
    
    # Update the balance in the database.
    amount = int(amount)
    mycursor.execute("UPDATE accounts SET balance = balance + %s WHERE username = %s", (amount, username))
    mydb.commit()
    login_click(username)

def login_click(username):
    # Clear the interface before creating a new one.
    clearInterface()
    
    # Get the balance from the database using the username.
    mycursor.execute("SELECT balance FROM accounts WHERE username = %s", (username,))
    balance = mycursor.fetchall()
    for balance_main in balance:
        for balance_fetch in balance_main:
            balance = balance_fetch

    # Create root widgets for the main screen.
    header_label = tk.Label(root, text="DIGITAL BANK", font=("Arial", 14, "bold"))
    credentials_header_label = tk.Label(root, text="ACCOUNT DETAILS:", font=("Arial", 10, "bold"))
    username_label = tk.Label(root, text=username)
    currency_label = tk.Label(root, text=str(balance) + "$", font=("Arial", 14))
    deposit_button = tk.Button(root, text="Deposit", width=15, height=1, command= lambda: deposit_interface(username))
    withdraw_button = tk.Button(root, text="Withdraw", width=15, height=1)
    logout_button = tk.Button(root, text="Logout", width=10, height=1, border=0, font=("Arial", 9, "italic"), command=login_interface)

    # Place the root widgets.
    header_label.place(x=93, y=20)
    credentials_header_label.place(x=50, y=60)
    username_label.place(x=50, y=85)
    currency_label.place(x=250, y=90)
    deposit_button.place(x=45, y=170)
    withdraw_button.place(x=175, y=170)
    logout_button.place(x=128, y=215)

def signup_click():
    # Clear the interface before creating a new one.
    clearInterface()

    # Create root widgets for the signup screen.
    username_label = tk.Label(root, text="Username")
    username_entry = tk.Entry(root, width=30)
    gmail_label = tk.Label(root, text="Gmail")
    gmail_entry = tk.Entry(root, width=30)
    password_label = tk.Label(root, text="Password")
    password_entry = tk.Entry(root, width=30, show="*")
    header_label = tk.Label(root, text="DIGITAL BANK", font=("Arial", 14, "bold"))
    signup_button = tk.Button(root, text="Sign up", width=15, height=1, command= lambda: signup_connect(username_entry.get(), gmail_entry.get(), password_entry.get()))
    login_button = tk.Button(root, text="Login", width=10, height=1, border=0, font=("Arial", 9, "italic"), command=login_interface)

    # Place the root widgets.
    header_label.place(x=93, y=20)
    username_label.place(x=75, y=55)
    username_entry.place(x=70, y=75)
    gmail_label.place(x=75, y=105)
    gmail_entry.place(x=70, y=125)
    password_label.place(x=75, y=155)
    password_entry.place(x=70, y=175)
    signup_button.place(x=105, y=215)
    login_button.place(x=123, y=255)
 
def clearInterface():
    # Loop the interface and destroy all widgets
    for interface in root.winfo_children():
        interface.destroy()

def deposit_interface(username):
    # Clear the interface before creating a new one.
    clearInterface()

    # Get the balance from the database using the username.
    mycursor.execute("SELECT balance FROM accounts WHERE username = %s", (username,))
    balance = mycursor.fetchall()
    for balance_main in balance:
        for balance_fetch in balance_main:
            balance = balance_fetch

    # Create root widgets for the deposit screen.
    amount_label = tk.Label(root, text="Amount:")
    currency_label = tk.Label(root, text=str(balance) + "$", font=("Arial", 14))
    amount_entry = tk.Entry(root, width=30)
    header_label = tk.Label(root, text="DIGITAL BANK", font=("Arial", 14, "bold"))
    deposit_button = tk.Button(root, text="Deposit", width=15, height=1, command= lambda: deposit_connect(username, amount_entry.get()))
    back_button = tk.Button(root, text="Back", width=10, height=1, border=0, font=("Arial", 9, "italic"), command= lambda: login_click(username))

    # Place the root widgets.
    header_label.place(x=93, y=20)
    amount_label.place(x=75, y=75)
    amount_entry.place(x=70, y=95)
    currency_label.place(x=152, y=145)
    deposit_button.place(x=105, y=215)
    back_button.place(x=123, y=255)

def login_interface():
    # Clear the interface before creating a new one.
    clearInterface()

    # Create root widgets for the login screen.
    username_label = tk.Label(root, text="Username")
    username_entry = tk.Entry(root, width=30)
    password_label = tk.Label(root, text="Password")
    password_entry = tk.Entry(root, width=30, show="*")
    header_label = tk.Label(root, text="DIGITAL BANK", font=("Arial", 14, "bold"))
    login_button = tk.Button(root, text="Login", width=15, height=1, command= lambda: login_connect(username_entry.get(), password_entry.get()))
    sing_up_button = tk.Button(root, text="Sign up", width=10, height=1, border=0, font=("Arial", 9, "italic"), command=signup_click)

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