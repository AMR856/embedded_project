#!/usr/bin/env python3
from csv import Error
import smtplib
import os
from models.role import Role

class Email:
    __instance = None
    __smtp = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Email, cls).__new__(cls)
            cls.__instance.__initialize_smtp()
        return cls.__instance

    def __initialize_smtp(self):
        try:
            self.__smtp = smtplib.SMTP('smtp.gmail.com', 587)
            self.__smtp.starttls()
            self.__smtp.login(os.getenv('ACCOUNT_EMAIL'), os.getenv('ACCOUNT_PASSWORD'))
            print("SMTP server initialized successfully.")
        except Exception as e:
            print(f"Failed to initialize SMTP: {e}")
            raise Error

    def make_message(self, pc_processor: str = '', pc_motherboard: str = '',
                    pc_hard_drive: str = '', pc_mac: str = '', username: str = '',
                    user_email: str = '', role: Role = Role.OWNER) -> str:
        message: str = ''
        if role is Role.OWNER:
            title = f"PC New Entry: {pc_mac}"
            body = (
                f"A new PC would like to register,\n\n"
                f"Here are the details of the user:\n"
                f"Email: {user_email}\n"
                f"Username: {username}\n"
                f"Processor: {pc_processor}\n"
                f"Motherboard: {pc_motherboard}\n"
                f"Hard Drive: {pc_hard_drive}\n"
                f"MAC Address: {pc_mac}\n\n"
                f"Best regards,\n"
            )
            message = f"Subject: {title}\n\n{body}"
        else:
            title = 'Database Registration'
            body = (
                f"Thank you for registration in this database,\n\n"
                f"Here are the details of your registration:\n"
                f"Email: {user_email}\n"
                f"Username: {username}\n"
            )
            message = f"Subject: {title}\n\n{body}"
        return message

    def send_email(self, msg: str, user_email: str) -> bool:
        try:
            self.__smtp.sendmail(
                os.getenv('ACCOUNT_EMAIL'),
                user_email,
                msg
            )
            print("Email sent successfully.")
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
