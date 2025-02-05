#!/usr/bin/env python3
import hashlib
from typing import Any, Dict
from models.computer import Computer
import firebase_admin
import uuid
from firebase_admin import credentials, firestore
import os

class DbStorage:
    """
    A class to handle database operations for registering and authenticating computer hardware in Firebase Firestore.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes a given password using SHA-256.

        Args:
            password (str): The password to be hashed.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def register_user(cls, computer: Computer, username: str, email: str) -> bool:
        """
        Registers a computer in the Firestore database if it is not already registered.

        Args:
            computer (Computer): An instance of the Computer class containing hardware details.

        Returns:
            bool: True if the computer was successfully registered, False if it already exists.
        """
        db = firestore.client()
        user_id: str = str(uuid.uuid4())

        user_data: Dict[Any] = {
            'cpu_id': computer.cpu_id,
            'motherboard_serial_number': computer.board_serial_number,
            'hard_disk_serial_number': computer.hard_disk_serial_number,
            'mac_address': computer.mac_address,
            'username': username,
            'email': email
        }

        collection = db.collection('users')
        users = collection.get()

        for user in users:
            data: Dict[Any] = user.to_dict()
            if (data.get('cpu_id') == computer.cpu_id and
                data.get('motherboard_serial_number') == computer.board_serial_number and
                data.get('hard_disk_serial_number') == computer.hard_disk_serial_number and
                data.get('mac_address') == computer.mac_address):
                return False

        collection.document(user_id).set(user_data)
        return True

    @classmethod
    def authenticate_user(cls, computer: Computer) -> bool:
        """
        Authenticates a computer by checking if its hardware details exist in the Firestore database.

        Args:
            computer (Computer): An instance of the Computer class containing hardware details.

        Returns:
            bool: True if the computer exists in the database, False otherwise.
        """
        db = firestore.client()
        collection = db.collection('users')
        users = collection.get()

        for user in users:
            user_data: Dict[Any] = user.to_dict()
            if (user_data.get('cpu_id') == computer.cpu_id and
                user_data.get('motherboard_serial_number') == computer.board_serial_number and
                user_data.get('hard_disk_serial_number') == computer.hard_disk_serial_number and
                user_data.get('mac_address') == computer.mac_address):
                return True

        return False

    @staticmethod
    def connect() -> None:
        """
        Connects to Firebase using credentials and initializes the app.

        The credentials are loaded from environment variables:
            - ACCOUNT_URL: Path to the Firebase service account JSON file.
            - DATABASE_URL: URL of the Firebase Realtime Database.

        Raises:
            Exception: If the Firebase app is already initialized or credentials are missing.
        """
        cred = credentials.Certificate(os.getenv('ACCOUNT_URL'))
        firebase_admin.initialize_app(cred, {
            'databaseURL': os.getenv('DATABASE_URL')
        })