#!/usr/bin/env python3
import wmi
import uuid
from models.computer import Computer # type: ignore
from models.file_storage import FileStorage # type: ignore

if __name__ == '__main__':
    pc = wmi.WMI()
    # computer = Computer('BFEBFBFF000906A3',
    #             'MP29MSXD',
    #             '5CD2_E485_2161_6A0F',
    #             '00:50:56:c0:00:08'
    # )
    computer = Computer(pc.WIN32_Processor()[0].ProcessorId,
                        pc.Win32_BaseBoard()[0].SerialNumber,
                        pc.Win32_DiskDrive()[0].SerialNumber.strip(),
                        ':'.join(
                            ['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]
                            ))
    FileStorage.check_computer(computer)
    for compu in FileStorage.all_computers():
        print(compu)
        print('--------------')
