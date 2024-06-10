import re
import sys


# Задание 6
def strip_punctuation_ru(data):
    punctuation_pattern = r"[!\"#$%&'()*+,-./:;<=>?@\[\\\]^_`{|}~«»—]"

    stripped_text = re.sub(punctuation_pattern, " ", data)

    return " ".join(stripped_text.split())


input_string = sys.stdin.readline().strip()

print(strip_punctuation_ru(input_string))


# Задание 5
def test_strip_punctuation_ru():
    test_data = [
        'Здесь нет запятых. Но есть точки.',
        'Уфа - город, где я живу.',
        'Перед "Но" ставится запятая.',
        'Просто точка.',
        'Много... многоточий!!!',
        '«Кавычки» и другие -- знаки',
        'Скобки (и в них текст)',
        'Точка внутри предложения. Точка'
    ]
    expected_results = [
        'Здесь нет запятых Но есть точки',
        'Уфа город где я живу',
        'Перед Но ставится запятая',
        'Просто точка',
        'Много многоточий',
        'Кавычки и другие знаки',
        'Скобки и в них текст',
        'Точка внутри предложения Точка'
    ]

    for data, expected in zip(test_data, expected_results):
        if strip_punctuation_ru(data) != expected:
            print("NO")
            return
    print("YES")


test_strip_punctuation_ru()
