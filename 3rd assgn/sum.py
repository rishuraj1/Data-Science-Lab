# Function to find the sum of numbers in a list
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main code
if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    
    total_sum = sum_of_list(my_list)
    
    print(f"The sum of numbers in the list {my_list} is: {total_sum}")
