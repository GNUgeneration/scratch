import random

def MakeProblem():
    divisor = random.randint(100, 999)
    dividend = random.randint(100000, 999999999)
    divisor_decimals = random.randint(11, 99)
    dividend_decimals = random.randint(11, 99)
    print 'divisor: %d' % divisor
    print 'dividend: %d' % dividend
    print 
    print 'divisor decimal digits: %d' % divisor_decimals
    print 'dividend decimal digits: %d' % dividend_decimals
    print 
    return 'Have a nice day!'
    

print MakeProblem()
