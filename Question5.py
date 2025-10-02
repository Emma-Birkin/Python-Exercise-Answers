def square_list(my_list):
    result = []
    for num in my_list:
        result += [num*num]
    return result

test_list = [1,2,3]
print(square_list(test_list))