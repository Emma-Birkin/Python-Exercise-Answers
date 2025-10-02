def square_list(my_list):
    result = []
    for num in my_list:
        result += [num*num]
    return result

test_list = [1,2,3]
print(square_list(test_list))
# Write a function that takes a list of integers and returns a list of those integers squared (i.e. each value multiplied by itself). Test with the list [1,2,3]
