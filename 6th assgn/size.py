# Function to find the size of a tuple
def tuple_size(my_tuple):
    return len(my_tuple)

# Main code
if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5)
    
    size = tuple_size(my_tuple)
    
    print(f"The size of the tuple {my_tuple} is: {size}")
