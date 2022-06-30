def gcd(a,b):
    #假定b是那个更大的数
    if b < a:
        a,b=b,a
    while a != 0:
        a,b = b%a,a
    return b

if __name__ == '__main__':
    print(gcd(27,45))