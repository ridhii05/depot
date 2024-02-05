#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Dell
#
# Created:     05-02-2024
# Copyright:   (c) Dell 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def convert_to_indian_currency(n):
    num_str = str(n)
    result = ""

    count = 0
    for digit in reversed(num_str):
        if count == 3:
            result = ',' + result
            count = 0
        result = digit + result
        count += 1

    return result

# Example usage
input_value = 504678
output_value = convert_to_indian_currency(input_value)

print(f"Input: {input_value}")
print(f"Output: {output_value}")
