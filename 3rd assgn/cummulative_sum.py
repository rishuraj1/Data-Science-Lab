# Function to compute cumulative sum of a list
def cumulative_sum(numbers):
    cumulative = []
    running_sum = 0
    for num in numbers:
        running_sum += num
        cumulative.append(running_sum)
    return cumulative

# Main code
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    
    cumulative_result = cumulative_sum(my_list)
    
    print(f"The cumulative sum of {my_list} is: {cumulative_result}")
