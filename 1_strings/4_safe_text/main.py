import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()
    wrong_article = wrong_article.split(".\n")
    wrong_article = [
        sentence[::-1].strip("!").replace("WOOF-WOOF", "CAT").capitalize()
        for sentence in wrong_article
    ]
    wrong_article = ".\n".join(wrong_article)
    return wrong_article
