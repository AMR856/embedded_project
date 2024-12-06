#!/usr/bin/env python3
import smtplib
import os
class Email:
    __s: smtplib.SMTP
    def __init__(self) -> None:
        self.__s = smtplib.SMTP('smtp.gmail.com', 587)
        self.__s.starttls()
        self.__s.login(os.getenv('ACCOUNT_EMAIL'), os.getenv('ACCOUNT_PASSWORD'))
        self.owner_email = os.getenv('OWNER_EMAIL')

    def make_message(self, pc_processor: str, pc_mother_board: str,
                    pc_hard_drive: str, pc_mac: str) -> str:
        title = f"PC New Entry: {pc_mac}"
        body = (
            f"A new pc would like to register,\n\n"
            f"Here are the details of the PC system:\n"
            f"Processor: {pc_processor}\n"
            f"Motherboard: {pc_mother_board}\n"
            f"Hard Drive: {pc_hard_drive}\n"
            f"MAC Address: {pc_mac}\n\n"
            f"Best regards,\n"
        )
        message = f"Firebase Registeration: {title}\n\n{body}"
        return message

    def send_email(self, msg: str) -> bool:
        try:
            self.smtp_server.sendmail(os.getenv('EMAIL_ACCOUNT'), self.owner_email, msg)
            print("Email sent successfully.")
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def get_smtp_instance(self) -> smtplib.SMTP:
        return self.__s
