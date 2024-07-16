# Function to find the maximum of two numbers
def find_maximum(a, b):
    return a if a > b else b

# Main code
if __name__ == "__main__":
    # Input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Finding the maximum number
    maximum = find_maximum(num1, num2)

    # Display the result
    print(f"The maximum of {num1} and {num2} is {maximum}")
