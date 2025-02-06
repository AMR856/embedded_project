import tkinter
from helpers.validation import email_validator_regex, validate_email_address_with_package, check_username
from tkinter import messagebox
from models.email import Email
from models.db_storage import DbStorage
from models.computer import Computer
import threading
import requests
from models.role import Role
import os

def register_user(computer: Computer, username_input: tkinter.Entry, email_input: tkinter.Entry, root: tkinter.Tk) -> None:
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
            switch_to_authenticated_window(root)
        else:
            messagebox.showinfo('Error', 'Computer is already registered')
    except Exception as err:
        print(f'Error: {err}')

def switch_to_authenticated_window(root: tkinter.Tk):
    for widget in root.winfo_children():
        widget.destroy()
    create_authenticated_window(root)

def start_task(root:tkinter.Tk, label: tkinter.Label):
    threading.Thread(target=lambda: program_arduino(root ,label), daemon=True).start()

def create_authenticated_window(root: tkinter.Tk):
    root.title("Progress Window")
    label = tkinter.Label(root, text="Press the button to start processing")
    label.pack(pady=10)
    start_button = tkinter.Button(root, text="Start Task", width=20, height=3, command=lambda: start_task(root, label))
    start_button.pack()

def program_arduino(root: tkinter.Tk, label: tkinter.Label):
    local_host_url = 'http://localhost:3000'
    url = local_host_url + '/program'
    try:
        root.config(cursor="wait")
        label.config(text="Uploading the code, please wait")
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showerror("Task Failed", "The task didn't finish properly")
            label.config(text="Try again")
            root.config(cursor="")
            return
        root.config(cursor="")
        label.config(text="Uploading is complete!")
        messagebox.showinfo("Task Complete", "The task has finished successfully!")
    except requests.exceptions.RequestException as e:
        root.config(cursor="")
        label.config(text="Error occurred during the request!")
        print(f"Error: {e}")
