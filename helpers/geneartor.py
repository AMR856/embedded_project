#!/usr/bin/env python3
from models.computer import Computer
from typing import List
import uuid

def random_generating(n: int) -> List[Computer] :
    computers = []
    for i in range(n):
        cpu_id = uuid.uuid4().hex
        motherboard_id = uuid.uuid4().hex
        disk_id = uuid.uuid4().hex
        mac_address = f"00:5{i % 10}:56:c0:00:{8+i:02x}"
        computers.append(Computer(cpu_id, motherboard_id, disk_id, mac_address))
    return computers
