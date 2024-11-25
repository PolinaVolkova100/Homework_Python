def decode_numbers(numbers: str) -> str | None:
    """Пишите ваш код здесь."""
    symbols = {
        "1": ".,?!:;",
        "2": "абвг",
        "3": "дежз",
        "4": "ийкл",
        "5": "мноп",
        "6": "рсту",
        "7": "фхцч",
        "8": "шщъы",
        "9": "ьэюя",
        "0": " ",
    }
    numbers = numbers.split()
    result = ""
    for number in numbers:
        if number in [symbol * len(number) for symbol in symbols.keys()] and len(
            number
        ) <= len(symbols[number[0]]):
            result += symbols[number[0]][len(number) - 1]
        else:
            result = "None"
            break
    return result
