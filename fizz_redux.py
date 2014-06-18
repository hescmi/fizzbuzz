import sys

def fizzbizz(bizz_num=15):
    if len(sys.argv) > 1:
        try:
            bizz_num = int(sys.argv[1])
        except ValueError:
            print "The value provided was not an integer please try again."
            exit(1)
    else:
        pass

    start = 1
    print "Fizz buzz is go. Count up to {} commencing!".format(bizz_num)

    while bizz_num + 1 > start:
        if bizz_num == 0:
            print "Nothing to do"
            start += 1
        elif divbizz(start) == True and divbizz(start,5) == True:
            print "fizz buzz"
            start += 1
        elif divbizz(start) == True:
            print "fizz"
            start += 1
        elif divbizz(start,5) == True:
            print "buzz"
            start += 1
        else:
            print start
            start += 1

####
#
####

def divbizz(x,y=3):
    if x % y == 0:
        return True
    else:
        return False


####
#
####

if __name__ == '__main__':
  fizzbizz()

