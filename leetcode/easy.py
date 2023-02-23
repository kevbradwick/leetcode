def roman_integer(s: str) -> int:
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

    # iterate over a window of two characters, shifting the window by one
    # if the first character is less than the second, subtract it from the total
    # otherwise, add it to the total. finally, add the last character to the total
    for a, b in zip(s, s[1:]):
        if numbers[a] < numbers[b]:
            total -= numbers[a]
        else:
            total += numbers[a]
    return total + numbers[s[-1]]
