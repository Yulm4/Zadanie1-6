import sys

# Задание 2
def is_palindrome(data):
    cleaned_data = ''.join(data.lower().split())
    return cleaned_data == cleaned_data[::-1]

input_string = sys.stdin.readline().strip()

if is_palindrome(input_string):
    print("YES")
else:
    print("NO")

# Задание 1
def test_is_palindrome():
    test_cases = ["кабак", "собака", "потоп", "еще", "заказ", "код", "дед"]
    results = [True, False, True, True, True, False, True]

    for i, test_case in enumerate(test_cases):
        if is_palindrome(test_case) != results[i]:
            print("NO")
            return
    print("YES")

test_is_palindrome()
