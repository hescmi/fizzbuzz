try:
    number = int(raw_input("Enter an integer from 0 to 100: "))

    assert number < 101, "Value entered greater than 100."
    assert number > 0, "Value entered less than 0."


except ValueError:
    print "The value entered was not an integer."
    try:
        number = int(raw_input("Enter an interger from 0 to 100: "))
    except ValueError:
        print "Please look up what an integer is.  Then try again."

    
else:
    start = 1
    print "Fizz buzz counting up to {0}".format(number)

    while number + 1 > start:
        if start % 3 == 0 and start % 5 == 0:
            print "fizz buzz"
            start += 1
        elif start % 3 == 0:
            print "fizz"
            start += 1
        elif start % 5 == 0:
            print "buzz"
            start += 1
        else:
            print start
            start += 1
