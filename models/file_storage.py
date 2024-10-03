#!/usr/bin/env python3
from .computer import Computer
from typing import List
import json
import os

class FileStorage:
    __all_computers : List[Computer] = []
    __storage_path: str = './data/data.json'
    __first_time = True

    @classmethod
    def all_computers(cls) -> List[Computer]:
        return cls.__all_computers

    @classmethod
    def get_all_computers_with_reading(cls):
        if cls.__first_time:
            cls.__all_computers.clear()
            cls.__first_time = False
        try:
            with open(cls.__storage_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError as err:
                    return []
                for _, value in data.items():
                    computer = Computer(value['cpu_id'],
                                        value['board_serial_number'],
                                        value['hard_disk_serial_number'],
                                        value['mac_address'])
                    cls.__all_computers.append(computer)
            return cls.__all_computers
        except FileNotFoundError as err:
            cls.make_file()

    @classmethod
    def is_in(cls, computer: Computer) -> int:
        for compu in cls.get_all_computers_with_reading():
            if compu.id == computer.id:
                return cls.__all_computers.index(compu)
        return -1

    @classmethod
    def add_new(cls, computer: Computer) -> None:
        cls.get_all_computers_with_reading().append(computer)
        cls.save_all()

    @classmethod
    def delete(cls, computer: Computer) -> bool:
        try:
            index = cls.is_in(computer)
            del cls.get_all_computers_with_reading()[index]
            cls.save_all()
            return True
        except ValueError:
            return False

    @classmethod
    def save_all(cls) -> None:
        saved_dict = {}
        for computer in cls.get_all_computers_with_reading():
            saved_dict['computer_' + computer.cpu_id] = {
                'cpu_id': computer.cpu_id,
                'board_serial_number': computer.board_serial_number,
                'hard_disk_serial_number': computer.hard_disk_serial_number,
                'mac_address': computer.mac_address
            }
        with open(cls.__storage_path, 'w', encoding='utf8') as file:
            json.dump(saved_dict, file, indent=4)

    @classmethod
    def check_computer(cls, computer: Computer) -> None:
        if cls.is_in(computer) == -1:
            cls.add_new(computer)

    @classmethod
    def make_file(cls) -> None:
        if not os.path.exists(cls.__storage_path):
            with open(cls.__storage_path, 'w') as file:
                pass
