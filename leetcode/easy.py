def roman_integer(input: str) -> int:
    """
    Given a roman numeral, convert it to an integer.

    >>> roman_integer("I")
    1
    >>> roman_integer("III")
    3
    >>> roman_integer("IV")
    4
    >>> roman_integer("IX")
    9
    >>> roman_integer("LVIII")
    58
    >>> roman_integer("MCMXCIV")
    1994
    """
    numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = 0
    skip = False

    for i, c in enumerate(input):
        if skip:
            skip = False
            continue

        prev_num = input[i - 1] if i > 0 else None
        next_num = input[i + 1] if i < len(input) - 1 else None

        # check if previous number is equal or greater than current number
        if prev_num and numbers[prev_num] <= numbers[c]:
            total += numbers[c]
        elif next_num and numbers[next_num] > numbers[c]:
            total += numbers[next_num] - numbers[c]
            skip = True
        else:
            total += numbers[c]

    return total
