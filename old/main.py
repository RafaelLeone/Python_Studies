def concatenate_lists(list1, list2):
    return list1 + list2

def order_list(new_list):
    return sorted(new_list)

def find_median(new_list):
    list_length = len(new_list)
    
    # If list_length is even:
    if list_length % 2 == 0:
        mid1 = new_list[list_length // 2 - 1] # subtract 1 because lists' first position is 0.
        mid2 = new_list[list_length // 2] # double slash means the floor result will be returned.
        return (mid1 + mid2) / 2
    # Or if list_length is odd:
    else:
        return new_list[list_length // 2]

# Example usage:
list1 = [1, 3, 5]
list2 = [7, 2, 4, 6]

concatenated_list = concatenate_lists(list1, list2)
ordered_list = order_list(concatenated_list)
median = find_median(ordered_list)

print("Concatenated List:", concatenated_list)
print("Ordered List:", ordered_list)
print("Median:", median)
