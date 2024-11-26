def encode_text(text: str) -> str | None:
    symbols = {
        " ": "0",
        ".,?!:;": "1",
        "абвг": "2",
        "дежз": "3",
        "ийкл": "4",
        "мноп": "5",
        "рсту": "6",
        "фхцч": "7",
        "шщъы": "8",
        "ьэюя": "9",
    }
    result = []
    symbols_keys = list(list(symbols_key) for symbols_key in symbols.keys())
    for s in text:
        if s not in "".join(list(symbols.keys())):
            return None
            break
        for i in range(len(symbols_keys)):
            if s in symbols_keys[i]:
                result.append(str(i) * (symbols_keys[i].index(s) + 1))
    result = " ".join(result)
    return result
