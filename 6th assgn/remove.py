# Function to remove tuples of length K from a list
def remove_tuples_of_length(tuple_list, K):
    filtered_list = [tup for tup in tuple_list if len(tup) != K]
    return filtered_list

# Main code
if __name__ == "__main__":
    tuple_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9), (10,)]
    
    K = 2
    
    filtered_tuples = remove_tuples_of_length(tuple_list, K)
    
    print("Original list of tuples:", tuple_list)
    print(f"Tuples with length not equal to {K}:", filtered_tuples)
