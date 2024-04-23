#[1]
#Find the two highest different numbers and how many times they appear in the array
#The highest two numbers:
#[10,30,50,50,40,80,100,100,80,100]
# 100: 3
# 80: 2
#
#Restrictions
#============
#	1. run time complexity: O(n)
#	2. space complexity: O(1)
#	3. parsing the array only once
#	4. not changing the input

arr = [100,100,100,100,100]

def find_higher(current_list):
    first_highest_appearances = 0
    second_highest_appearances = 0
    negative_infinity = float('-inf')
    first_highest_number = negative_infinity
    second_highest_number = negative_infinity
    
    for number in current_list:
        if number > first_highest_number:
            second_highest_number = first_highest_number
            first_highest_number = number
            second_highest_appearances = first_highest_appearances
            first_highest_appearances = 0
        if number > second_highest_number and number != first_highest_number:
            second_highest_number = number
            second_highest_appearances = 0

        if number == first_highest_number:
            first_highest_appearances += 1
        if number == second_highest_number:
            second_highest_appearances += 1
            
        result = { first_highest_number: first_highest_appearances, second_highest_number: second_highest_appearances, }
        
        if second_highest_number == negative_infinity:
            result ={ first_highest_number: first_highest_appearances, }
            
    return result

print(find_higher(arr))

# Study purposes only. Not used.
def count_appearances(first_highest, second_highest, curr_list):
    first_highest_appearances = 0
    second_highest_appearances = 0
    for number in curr_list:
        if number == first_highest:
            first_highest_appearances += 1
        if number == second_highest:
            second_highest_appearances += 1
    result = { first_highest: first_highest_appearances, second_highest: second_highest_appearances, }
    return result
