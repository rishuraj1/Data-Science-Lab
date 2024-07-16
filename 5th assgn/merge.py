# Function to merge two dictionaries using update() method
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Main code
if __name__ == "__main__":
    dict1 = {'a': 10, 'b': 20}
    dict2 = {'c': 30, 'd': 40}
    
    merged_dict = merge_dicts(dict1, dict2)
    
    print("Merged dictionary:", merged_dict)
