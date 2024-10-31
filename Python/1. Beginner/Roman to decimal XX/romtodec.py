tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def RomanNumeralToDecimal(roman_numeral):
    sum = 0
    prev_value = 0

    for char in roman_numeral:
        curr_value = tallies[char]

        if curr_value > prev_value:
            sum += curr_value - 2 * prev_value
        else:
            sum += curr_value

        prev_value = curr_value

    return sum

# Example usage:
roman_numeral = "V"
decimal_value = RomanNumeralToDecimal(roman_numeral)
print(decimal_value)  # Output: 9