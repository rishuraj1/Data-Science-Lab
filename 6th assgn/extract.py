# Function to extract digits from a list of tuples
def extract_digits(tuple_list):
    digits = [digit for tup in tuple_list for digit in tup]
    return digits

# Main code
if __name__ == "__main__":
    tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    
    digit_list = extract_digits(tuple_list)
    
    print("Original list of tuples:", tuple_list)
    print("Extracted digits:", digit_list)
