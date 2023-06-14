def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    output = 0
    previous_value = 0

    for symbol in roman_string:
        value = roman_dict.get(symbol, 0)
        if value > previous_value:
            output -= 2 * previous_value
        output += value
        previous_value = value

    return output
