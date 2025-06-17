def harshadh(n):
    temp = n
    sum = 0
    while n>0:
        dig = n%10
        sum += dig
        n //= 10
    if temp%sum == 0:
        print('Harshadh Number')
    else:
        print('Not a Harshadh Number')
harshadh(27)
harshadh(25)
