import tkinter
from helpers.valdation import email_validator_regex, validate_email_address_with_package, check_username
from tkinter import messagebox
from models.email import Email
from models.db_storage import DbStorage
from models.computer import Computer
from models.role import Role
import os

def register_user(computer: Computer, username_input: tkinter.Entry, email_input: tkinter.Entry) -> None:
    email = Email()
    username = username_input.get()
    if not check_username(username):
        messagebox.showerror('Error', 'Username is not valid')
        return
    user_email = email_input.get()
    if not email_validator_regex(user_email) and not validate_email_address_with_package(user_email)[0]:
        messagebox.showerror('Error', 'Email is not valid')
        return
    try:
        if DbStorage.register_user(computer, username, user_email):
            owner_msg = email.make_message(
                                    computer.cpu_id,
                                    computer.board_serial_number,
                                    computer.hard_disk_serial_number,
                                    computer.mac_address,
                                    username,
                                    user_email,
                                    Role.OWNER
            )
            email.send_email(owner_msg, os.getenv('OWNER_EMAIL'))
            user_msg = email.make_message(
                                    username=username,
                                    user_email=user_email,
                                    role=Role.USER
            )
            email.send_email(user_msg, user_email)
            messagebox.showinfo('Success', 'Computer is now registered')
        else:
            messagebox.showinfo('Error', 'Computer is already registered')
    except Exception as err:
        print(f'Error: {err}')

def login_user(computer: Computer, username_input: tkinter.Entry, email_input: tkinter.Entry):
    username = username_input.get()
    if not check_username(username):
        messagebox.showerror('Error', 'Username is not valid')
        return
    user_email = email_input.get()
    if not email_validator_regex(user_email) and not validate_email_address_with_package(user_email)[0]:
        messagebox.showerror('Error', 'Email is not valid')
        return
    if DbStorage.authenticate_user(computer):
        messagebox.showinfo('Success', 'Login was successful')
    else:
        messagebox.showerror('Error', 'User is not registered')
