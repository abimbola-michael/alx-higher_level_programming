#!/usr/bin/python3
def subtractNumbers(numbers):
    same_count = 0
    big_number = max(numbers)

    for num in numbers:
        if big_number > num:
            same_count += num
    return (big_number - same_count)


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_list = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }
    roman_keys = list(roman_list.keys())

    number = 0
    last_roman_number = 0
    numbers_list = [0]

    for roman_char in roman_string:
        for roman_key in roman_keys:
            if roman_key == roman_char:
                if roman_list[roman_char] <= last_roman_number:
                    number += subtractNumbers(numbers_list)
                    numbers_list = [roman_list[roman_char]]
                else:
                    numbers_list.append(roman_list[roman_char])
                    last_roman_number = roman_list[roman_char]
                number += subtractNumbers(number_list)
    return number
