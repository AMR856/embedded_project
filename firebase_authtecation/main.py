#!/usr/bin/env python3
import wmi
import uuid
from models.computer import Computer
from models.db_storage import DbStorage
from tkinter_functions import register_user, login_user
import tkinter as tk
from dotenv import load_dotenv
import os

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

        login_button = tk.Button(
            root,
            text="Login",
            command=lambda: login_user(computer, username_input, email_input),
            width=20,
            height=2
        )
        login_button.pack(pady=10)

        root.mainloop()
