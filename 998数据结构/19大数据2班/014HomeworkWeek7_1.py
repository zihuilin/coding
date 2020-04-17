
def printN(n):
    if n<=9:
        print(n)
    else:
        ge_wei = n%10
        print(ge_wei)
        printN(n//10)

n = 8726
printN(n)
