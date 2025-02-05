#!/usr/bin/env python3
import wmi
import uuid
from models.computer import Computer
from models.db_storage import DbStorage
from register_function import register_user
from helpers.utils import load_env
from tkinter import messagebox
import threading
import requests
import tkinter as tk

def program_arduino():
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

def start_task():
    threading.Thread(target=program_arduino, daemon=True).start()


if __name__ == '__main__':
    load_env('.\\.env')
    pc = wmi.WMI()
    pc_processor = pc.WIN32_Processor()[0].ProcessorId
    pc_motherboard = pc.Win32_BaseBoard()[0].SerialNumber
    pc_hard_drive = pc.Win32_DiskDrive()[0].SerialNumber.strip()
    pc_mac = ':'.join(
        ['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1]
    )

    computer = Computer(pc_processor,
                        pc_motherboard,
                        pc_hard_drive,
                        pc_mac)

    pc_info = {
        "processor": pc_processor,
        "motherboard": pc_motherboard,
        "hard_drive": pc_hard_drive,
        "mac": pc_mac
    }
    DbStorage.connect()
    root = tk.Tk()
    root.geometry("900x300")
    if DbStorage.authenticate_user(computer):
        root.title("Progress Window")
        label = tk.Label(root, text="Press the button to start processing")
        label.pack(pady=10)
        start_button = tk.Button(root, text="Start Task", width=20, height=3, command=start_task)
        start_button.pack()
        root.mainloop()
    else:
        root.geometry("900x300")
        root.title("Authentication Window")
        username_label = tk.Label(root, text="Enter your username:")
        username_label.pack(pady=5)
        username_input = tk.Entry(root, width=30)
        username_input.pack(pady=5)
        email_label = tk.Label(root, text="Enter your email:")
        email_label.pack(pady=5)
        email_input = tk.Entry(root, width=30)
        email_input.pack(pady=5)
        register_button = tk.Button(
            root,
            text="Register",
            command=lambda: register_user(computer, username_input, email_input),
            width=20,
            height=2
        )
        register_button.pack(pady=10)
        root.mainloop()
