import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    info = get_employees_info()
    info = [sentence.split() for sentence in info]
    parsed_employees_info = []
    for lst in info:
        dct = {
            "id": 0,
            "name": "",
            "last_name": "",
            "age": 0,
            "salary": 0,
            "position": "",
        }
        for i in range(0, len(lst), 2):
            if lst[i] in dct:
                if lst[i] == "id" or lst[i] == "age":
                    dct[lst[i]] = int(lst[i + 1])
                elif lst[i] == "salary":
                    dct[lst[i]] = float(lst[i + 1])
                else:
                    dct[lst[i]] = lst[i + 1]
        parsed_employees_info.append(dct)
    return parsed_employees_info
