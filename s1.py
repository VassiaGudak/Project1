import re

def findSumReg(fileName):
    """
    Returns amount of all numbers in the input file. Ignores letters, non-characters 
    like punctuation and spaces.

    fileName: name of input file
    returns: sum of all numbers
    """
    return sum([int(num) for num in re.findall('[0-9]+',open(fileName).read())])

'''
#if __name__ == '__main__':
    # To test findSumReg:
    
    test1 = findSumReg("regex_sum_42.txt")
    assert '44' == str(test1)[:2] and '22' == str(test1)[-2:]
    print "1. Amount of test 1 is: " + str(test1)

   test2 = findSumReg("regex_sum_283744.txt")
   assert '35' == str(test2)[:2] and '27' == str(test2)[-2:]
   print "1. Amount of test 2 is: " + str(test2)
'''