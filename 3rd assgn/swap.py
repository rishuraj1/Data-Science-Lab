# Function to swap elements at given indices in a list
def swap_elements(lst, idx1, idx2):
    if 0 <= idx1 < len(lst) and 0 <= idx2 < len(lst):
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    else:
        print("Error: Invalid indices")

# Main code
if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    
    index1 = 1
    index2 = 3
    
    swap_elements(my_list, index1, index2)
    
    print("List after swapping elements at index", index1, "and", index2, ":", my_list)
