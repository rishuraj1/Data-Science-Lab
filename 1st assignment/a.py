# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main code
if __name__ == "__main__":
    # Input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Adding the numbers
    result = add_numbers(num1, num2)

    # Display the result
    print(f"The sum of {num1} and {num2} is {result}")
