#!/usr/bin/env python3
import wmi
import uuid
from models.computer import Computer
from models.file_storage import FileStorage
from helpers.geneartor import random_generating

if __name__ == '__main__':
    pc = wmi.WMI()
    # computers = random_generating(1)
    computer = Computer(pc.WIN32_Processor()[0].ProcessorId,
                        pc.Win32_BaseBoard()[0].SerialNumber,
                        pc.Win32_DiskDrive()[0].SerialNumber.strip(),
                        ':'.join(
                            ['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]
                            ))
    # for compu in computers:
    #     FileStorage.check_computer(compu)
    FileStorage.check_computer(computer)
    for compu in FileStorage.all_computers():
        print(compu)
        print('--------------')
