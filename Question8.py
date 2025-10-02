def fizzbuzz():
    i = 1
    while i <= 20:
        if (i % 3 == 0) and (i % 5 == 0):
            print (str(i) + " is FizzBuzz")
        elif i % 3 == 0:
            print (str(i) + " is Fizz")
        elif i % 5 == 0:
            print (str(i) + " is Buzz")
        else:
            print (str(i) + " is neither")
        i += 1
fizzbuzz()