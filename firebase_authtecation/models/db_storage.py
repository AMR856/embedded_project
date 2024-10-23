#!/usr/bin/env python3
import hashlib
from models.computer import Computer
import firebase_admin
from firebase_admin import credentials, db
import os

class DbStorage:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def register_user(cls, computer: Computer) -> None:
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = cls.hash_password(password)

        user_data = {
            'username': username,
            'password': hashed_password,
            'cpu_id': computer.cpu_id,
            'motherboard_serial_number': computer.board_serial_number,
            'hard_disk_serial_number': computer.hard_disk_serial_number,
            'mac_address': computer.mac_address
        }
        ref = db.reference('users')
        users = ref.get()
        for _, data in users.items():
            if data['username'] == username and data['cpu_id'] == computer.cpu_id:
                print('User already registered')
                return
        ref.push(user_data)
        print("User registered successfully!")

    @classmethod
    def authenticate_user(cls, computer: Computer) -> bool:
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = cls.hash_password(password)

        ref = db.reference('users')
        users = ref.get()
        for _, user_data in users.items():
            if user_data['username'] == username:
                if user_data['password'] == hashed_password:
                    if (user_data['cpu_id'] == computer.cpu_id and
                        user_data['motherboard_serial_number'] == computer.board_serial_number and
                        user_data['hard_disk_serial_number'] == computer.hard_disk_serial_number and
                        user_data['mac_address'] == computer.mac_address):
                        print("Login successful!")
                        return True
                    else:
                        print("Hardware information does not match.")
                        return False
                else:
                    print("Incorrect password.")
                    return False
        print("Username not found.")
        return False

    @staticmethod
    def connect() -> None:
        cred = credentials.Certificate(os.getenv('ACCOUNT_URL'))
        firebase_admin.initialize_app(cred, {
            'databaseURL': os.getenv('DATABASE_URL')
        })
