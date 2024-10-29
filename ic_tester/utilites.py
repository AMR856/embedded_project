from typing import List, Union, Dict

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

def filter_row(normlalized_row: List[Union[None, float]]) -> List:
    filtered_data = [round(x, 4) for x in normlalized_row if x is not None]
    return filtered_data

def save_to_file(ic_saved_dict: Dict[str, List[float]]) -> None:
    with open('./data/ics_data.txt', 'w', encoding='utf8') as file:
        for key, value in ic_saved_dict.items():
            file.write(f'{key}: {value}\n')
