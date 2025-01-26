#!/usr/bin/env python3
from typing import Any, Dict
import firebase_admin
from firebase_admin import credentials, firestore
import os

class DbStorage:
    @classmethod
    def authenticate_user(cls, email: str, username: str) -> bool:
        """
        Authenticates a computer by checking if its hardware details exist in the Firestore database.

        Args:
            email: Email of the user to be authenticated
            username: Username of the user to be authenticated
        Returns:
            bool: True if the computer exists in the database, False otherwise.
        """
        db = firestore.client()
        collection = db.collection('users')
        users = collection.get()
        for user in users:
            user_data: Dict[Any] = user.to_dict()
            if user_data.get('email') == email and user_data.get('username') == username:
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
