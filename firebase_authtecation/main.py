#!/usr/bin/env python3
import wmi
import uuid
from models.computer import Computer
from models.file_storage import FileStorage
from models.db_storage import DbStorage
from dotenv import load_dotenv
import os
# from helpers.geneartor import random_generating

if __name__ == '__main__':
    load_dotenv()
    pc = wmi.WMI()
    computer = Computer(pc.WIN32_Processor()[0].ProcessorId,
                        pc.Win32_BaseBoard()[0].SerialNumber,
                        pc.Win32_DiskDrive()[0].SerialNumber.strip(),
                        ':'.join(
                            ['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]
                            ))
    if os.getenv('DB_STORAGE'):
        DbStorage.connect()
        while True:
            print('#########################################################')
            print('What do you want to do: ')
            print('1- Registring into the database')
            print('2- Logging in the database')
            print('3- Exit the program')
            print('#########################################################')
            user_input = int(input())
            if user_input == 1:
                DbStorage.register_user(computer)
            elif user_input == 2:
                logged_in: bool = DbStorage.authenticate_user(computer)
                if logged_in:
                    break
            elif user_input == 3:
                break
            else:
                print('Invalid choice')
                continue
