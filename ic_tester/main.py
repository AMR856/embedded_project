import openpyxl 
import math
from typing import List, Union

def get_max(values_list: List[Union[float, None]]) -> Union[int, float]:
    max = float('-inf')
    for value in values_list:
        if value and value > max:
            max = value
    return max

def normalizer(values_list: List[Union[int, float, None, str]],
            max_value: Union[int, float]) -> List[Union[int, float, None, str]]:
    values_list[1] = 'Normalized'
    for i in range(2, len(values_list[2:])):
        if values_list[i]:
            values_list[i] = round(values_list[i] / max_value, 3)
    return tuple(values_list)

if __name__ == "__main__":
    wb = openpyxl.load_workbook('./data/embedded_sysetms_ICS_readings.xlsx')
    ws = wb.active
    rows_count = ws.max_row
    ics_count = math.ceil(rows_count / 5)
    rows_values = list(ws.iter_rows(values_only=True))
    current_ic_index = 0
    while current_ic_index < ics_count:
        print('----------------')
        indexer = 5 * current_ic_index
        names_row = rows_values[indexer]
        print(f'Names Row: {names_row}')
        pins_row = rows_values[indexer + 1]
        print(f'Pins Row: {pins_row}')
        readings_row = rows_values[indexer + 2]
        max_value = get_max(readings_row[2:])
        print(f'Readings Row: {readings_row}')
        normalized_row = normalizer(list(readings_row), max_value)
        print(f'Normalized Row: {normalized_row}')
        current_ic_index += 1
        print('----------------')
