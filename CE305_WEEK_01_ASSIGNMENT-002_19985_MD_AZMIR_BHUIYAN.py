def float_to_14_bit_binary(num):
    # Check for negative number and convert to positive for processing
    sign_bit = '0'
    if num < 0:
        sign_bit = '1'
        num = abs(num)

    # Separate the integer and fractional parts
    int_part = int(num)
    frac_part = num - int_part

    # Convert integer part to binary
    int_binary = bin(int_part)[2:]

    # Convert fractional part to binary with 8 bits precision
    frac_binary = ""
    for _ in range(8):
        frac_part *= 2
        frac_bit = int(frac_part)
        frac_binary += str(frac_bit)
        frac_part -= frac_bit

    # Normalize and calculate the exponent
    exponent = len(int_binary) - 1

    # Combine sign bit, exponent, and fractional part
    binary_representation = sign_bit + format(exponent + 63, '06b') + int_binary[1:] + frac_binary

    # Ensure the binary representation is exactly 14 bits
    binary_representation = binary_representation[:14].ljust(14, '0')

    return binary_representation

# Example usage
input_number = -26.625
binary_representation = float_to_14_bit_binary(input_number)
print(f"The binary representation of {input_number} is {binary_representation}")
