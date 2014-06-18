import sys

####
#Set value to count up to
####

def gen_input(argv_number):
    try:

        if argv_number == None:
            number = int(raw_input("Enter an integer from 0 to 100: "))
        else:
            number = int(argv_number)

        try:
            assert number < 101, "Value entered greater than 100"
            assert number >= 0, "Value entered less than 0."
        except AssertionError:
            print "Value not in accepted range. Try again."
            exit(1)

    except ValueError:
        print "The value entered was not an integer."

        try:
            number = int(raw_input("Enter an interger from 0 to 100: "))
        except ValueError:
            print "Please look up what an integer is.  Then try again."
            exit(1)
        else:
            get_down_to_fizzbuzzness(number)

    else:
        get_down_to_fizzbuzzness(number)

####
#Count up
####

def get_down_to_fizzbuzzness(fizzbuzzit):
    start = 1
    number = fizzbuzzit
    print "Fizz buzz counting up to {0}".format(number)

    while number + 1 > start:
        if number == 0:
            print "Nothing to do"
            start += 1
        elif start % 3 == 0 and start % 5 == 0:
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


####
#Run Script
####

if len(sys.argv) > 1:
    cmd_number = sys.argv[1]
else:
    cmd_number = None

gen_input(cmd_number)

