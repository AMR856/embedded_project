#!/usr/bin/env python3
import hashlib
from models.computer import Computer
import firebase_admin
import uuid
from firebase_admin import credentials, db
import os

class DbStorage:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def register_user(cls, computer: Computer) -> bool:
        user_data = {
            'user_id': str(uuid.uuid4()),
            'cpu_id': computer.cpu_id,
            'motherboard_serial_number': computer.board_serial_number,
            'hard_disk_serial_number': computer.hard_disk_serial_number,
            'mac_address': computer.mac_address
        }
        ref = db.reference('users')
        users = ref.get()
        for _, data in users.items():
            if data.get('cpu_id') == computer.cpu_id and \
            data.get('motherboard_serial_number') == computer.board_serial_number and \
            data.get('hard_disk_serial_number') == computer.hard_disk_serial_number and \
            data.get('mac_address') == computer.mac_address:
                return False
        ref.push(user_data)
        return True

    @classmethod
    def authenticate_user(cls, computer: Computer) -> bool:
        ref = db.reference('users')
        users = ref.get()
        for _, user_data in users.items():
                if (user_data.get('cpu_id')  == computer.cpu_id and
                    user_data.get('motherboard_serial_number') == computer.board_serial_number and
                    user_data.get('hard_disk_serial_number') == computer.hard_disk_serial_number and
                    user_data.get('mac_address')  == computer.mac_address):
                    return True
        return False

    @staticmethod
    def connect() -> None:
        cred = credentials.Certificate(os.getenv('ACCOUNT_URL'))
        firebase_admin.initialize_app(cred, {
            'databaseURL': os.getenv('DATABASE_URL')
        })
