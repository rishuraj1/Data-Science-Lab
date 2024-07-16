# Function to calculate factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main code
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")
