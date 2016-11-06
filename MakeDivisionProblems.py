import random

def MakeProblem(Divisor, Dividend, Decimal):
    print 'Divisor: %d' % Divisor
    print 'Dividend: %d' % Dividend
    print 'Decimal: %d' % Decimal

Divis = random.randint(100, 999)
Divid = random.randint(100000, 999999999)
Decim = random.randint(11, 99)

print MakeProblem(Divis, Divid, Decim)
