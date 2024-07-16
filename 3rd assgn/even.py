# Function to find even numbers in a list
def find_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# Main code
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    even_nums = find_even_numbers(my_list)
    
    print(f"The even numbers in the list {my_list} are: {even_nums}")
