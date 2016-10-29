import random

def MakeProblem(Divisor, Dividend):
    print 'Divisor: %d' % Divisor
    print 'Dividend: %d' % Dividend

Divis = random.randint(100, 999)
Divid = random.randint(100000, 999999999)

print MakeProblem(Divis, Divid)
