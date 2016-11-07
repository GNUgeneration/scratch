lengthOfpattern = int(raw_input("How many multiples do you want: "))
num = int(raw_input("Please give me the # you want the multiples of: "))
                                
for i in range(1,lengthOfpattern + 1):
    print i,'|', num * i
