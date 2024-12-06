#!/usr/bin/env python3
import wmi
import uuid
from models.computer import Computer
# from models.file_storage import FileStorage # This was used for testing
from models.db_storage import DbStorage
import tkinter as tk
from dotenv import load_dotenv
import os
# from helpers.geneartor import random_generating # This was used for testing

def check_user(pr_processor: str, pc_motherboard: str,
            pc_hard_drive: str, pc_mac: str):
    pass

if __name__ == '__main__':
    load_dotenv()
    pc = wmi.WMI()
    pc_processor = pc.WIN32_Processor()[0].ProcessorId
    pc_motherboard = pc.Win32_BaseBoard()[0].SerialNumber
    pc_hard_drive = pc.Win32_DiskDrive()[0].SerialNumber.strip()
    pc_mac = ':'.join(
                            ['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]
            )

    computer = Computer(pc_processor,
                        pc_motherboard,
                        pc_hard_drive,
                        pc_mac
                )

    if os.getenv('DB_STORAGE'):
        DbStorage.connect()
        while True:
            root = tk.Tk()
            root.title("Firebase Auth")
            root.geometry("900x300")
            label = tk.Label(root, text="Enter IC readings: ")
            label.pack(pady=10)
            entry = tk.Entry(root, width=80)
            entry.pack(pady=5)
            button = tk.Button(root, text="Submit", command=check_user)
            button.pack(pady=10)
            root.mainloop()
