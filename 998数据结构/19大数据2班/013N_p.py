
def p(n):
    if n==0:
        return 1
    else:
        return p(n-1) * n

print(p(4))
