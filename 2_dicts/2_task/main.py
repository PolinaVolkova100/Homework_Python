def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    text = [word.strip('!?,.$%#^-;":') for word in text.lower().split()]
    most_common = {}

    for word in text:
        if len(word) > 2:
            most_common[word] = most_common.get(word, 0) + 1

    most_common = dict(sorted(most_common.items(), key=lambda value: value[0]))
    most_common = dict(
        sorted(most_common.items(), key=lambda value: value[1], reverse=True)
    )
    most_common = dict(list(most_common.items())[:10])

    return most_common
