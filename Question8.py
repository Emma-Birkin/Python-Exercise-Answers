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
# Print numbers from 1 to 20. If a number is divisible by 3, print “Fizz”. If the number is divisible by 5 print “Buzz”. If it’s divisible by both 3 and 5, print “FizzBuzz”
