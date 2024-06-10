import re
import sys


# Задание 4
def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(8|\+7)[\-\s]?(?:\(\d{3}\)|\d{3})[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}$'

    return re.match(pattern, number) is not None


input_string = sys.stdin.readline().strip()

if is_correct_mobile_phone_number_ru(input_string):
    print("YES")
else:
    print("NO")


# Задание 3
def test_is_correct_mobile_phone_number_ru():
    test_numbers = [
        '8(996)452-32-21',
        '+7 927 453-12-37',
        '89312324124',
        '+7(939)4564321',
        '7(933)144-55-77',
        '+9 123 456-78-90',
        '8 927 721 98 00',
        '+7-999-000-05-60',
        '8(957)1111111',
        '+7 957 222 2222'
    ]
    expected_results = [True, True, True, True, False, False, True, True, True, True]

    for number, expected in zip(test_numbers, expected_results):
        if is_correct_mobile_phone_number_ru(number) != expected:
            print("NO")
            return
    print("YES")


test_is_correct_mobile_phone_number_ru()
