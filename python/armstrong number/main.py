def is_armstrong_number(number):
    """
    Check if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power
    of the number of digits.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to iterate over digits
    digits = str(number)
    num_digits = len(digits)

    # Calculate the sum of digits each raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

    # Check if the sum of powers equals the original number
    return sum_of_powers == number

# Input from the user
num = int(input("Enter a number: "))

# Check and display the result
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
