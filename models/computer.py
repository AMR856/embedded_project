#!/usr/bin/env python3
class Computer:
    def __init__(self, cpu_id: str, board_serial_number: str,
                hard_disk_serial_number: str,  mac_address: str) -> None:
        self.__cpu_id = cpu_id
        self.__board_serial_number = board_serial_number
        self.__hard_disk_serial_number = hard_disk_serial_number
        self.__mac_address = mac_address

    @property
    def cpu_id(self) -> str:
        return self.__cpu_id

    @property
    def board_serial_number(self) -> str:
        return self.__board_serial_number

    @property
    def hard_disk_serial_number(self) -> str:
        return self.__hard_disk_serial_number

    @property
    def mac_address(self) -> str:
        return self.__mac_address

    @property
    def id(self) -> str:
        return 'computer_' + self.__cpu_id

    def __str__(self) -> str:
        return (f"Computer Information:\n"
                f"ID: {self.id}\n"
                f"CPU ID: {self.cpu_id}\n"
                f"Board Serial Number: {self.board_serial_number}\n"
                f"Hard Disk Serial Number: {self.hard_disk_serial_number}\n"
                f"MAC Address: {self.mac_address}")
