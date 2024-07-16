# Function to find maximum and minimum elements in a tuple
def find_max_min(my_tuple):
    max_element = max(my_tuple)
    min_element = min(my_tuple)
    return max_element, min_element

# Main code
if __name__ == "__main__":
    my_tuple = (10, 20, 5, 40, 30)
    
    max_element, min_element = find_max_min(my_tuple)
    
    print(f"The maximum element in the tuple {my_tuple} is: {max_element}")
    print(f"The minimum element in the tuple {my_tuple} is: {min_element}")
