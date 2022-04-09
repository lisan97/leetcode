def gcd(a,b):
    #假定b是那个更大的数
    if b < a:
        a,b=b,a
    while a != 0:
        a,b = a%b,a
    return a