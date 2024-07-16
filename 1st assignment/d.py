# Function to check if a number is an Armstrong number
def is_armstrong(number):
    num_digits = len(str(number))
    
    sum = 0
    temp = number
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10
    
    if number == sum:
        return True
    else:
        return False

# Main code
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    
    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
