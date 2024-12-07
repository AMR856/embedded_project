#!/usr/bin/env python3
import wmi
import uuid
from models.computer import Computer
from models.db_storage import DbStorage
from models.email import Email
import tkinter as tk
from tkinter import E, messagebox
from dotenv import load_dotenv
import os


def register_user(computer: Computer):
    email = Email()
    try:
        if DbStorage.register_user(computer):
            msg = email.make_message(computer.cpu_id,
                                    computer.board_serial_number,
                                    computer.hard_disk_serial_number,
                                    computer.mac_address
            )
            email.send_email(msg)
            messagebox.showinfo('Success', 'Computer is now registered')
        else:
            messagebox.showinfo('Error', 'Computer is already registered')
    except Exception as err:
        print(f'Error: {err}')

def login_user(computer: Computer):
    if DbStorage.authenticate_user(computer):
        messagebox.showinfo('Success', 'Login was successful')
    else:
        messagebox.showerror('Error', 'User is not registered')

if __name__ == '__main__':
    load_dotenv()
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

    if os.getenv('DB_STORAGE'):
        DbStorage.connect()
        root = tk.Tk()
        root.title("Firebase Authentication")
        root.geometry("900x300")

        instruction_label = tk.Label(root, text="Please select an action:", font=("Arial", 14))
        instruction_label.pack(pady=10)

        register_button = tk.Button(
            root,
            text="Register",
            command=lambda: register_user(computer),
            width=20,
            height=2
        )
        register_button.pack(pady=10)

        login_button = tk.Button(
            root,
            text="Login",
            command=lambda: login_user(computer),
            width=20,
            height=2
        )
        login_button.pack(pady=10)

        root.mainloop()
