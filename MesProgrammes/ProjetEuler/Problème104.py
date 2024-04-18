def fibonacci():
    panadigital_digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    fn1,fn2 = 1,1
    loop = True
    index = 2
    while loop == True:
        fn1,fn2 = fn2,fn1+fn2
        #first and last 9 digits
        if sorted(str(fn2%1_000_000_000)) == panadigital_digit and sorted(str(fn2)[:9]) == panadigital_digit:
            index += 1
            loop = False
        else:
            index += 1
    print(index)

fibonacci()
