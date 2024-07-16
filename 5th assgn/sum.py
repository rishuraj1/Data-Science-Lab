# Function to find sum of all values in a dictionary
def sum_of_values(dictionary):
    total_sum = sum(dictionary.values())
    return total_sum

# Main code
if __name__ == "__main__":
    my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
    
    total_sum = sum_of_values(my_dict)
    
    print(f"The sum of all values in the dictionary {my_dict} is: {total_sum}")
