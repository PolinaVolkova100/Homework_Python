def format_phone(phone_number: str) -> str:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    formatted_phone_number = ""
    for s in phone_number:
        if s.isdigit() == True:
            formatted_phone_number += s

    if len(formatted_phone_number) == 11 and (
        formatted_phone_number[:2] == "89" or formatted_phone_number[:2] == "79"
    ):
        formatted_phone_number = formatted_phone_number[1:]
        formatted_phone_number = f"8 ({formatted_phone_number[0:3]}) {formatted_phone_number[3:6]}-{formatted_phone_number[6:8]}-{formatted_phone_number[8:]}"
    elif len(formatted_phone_number) == 10 and formatted_phone_number[0] == "9":
        formatted_phone_number = f"8 ({formatted_phone_number[0:3]}) {formatted_phone_number[3:6]}-{formatted_phone_number[6:8]}-{formatted_phone_number[8:]}"

    return formatted_phone_number
    return formatted_phone_number
