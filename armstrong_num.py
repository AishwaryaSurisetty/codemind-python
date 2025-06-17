def armstrong(n):
    sum = 0
    count = 0
    n1 = n
    n2 = n
    while n > 0:
        dig = n%10
        count += 1
        n //= 10
    while n1 > 0:
        dig1 = n1%10
        sum += dig1**count
        n1 //= 10
    if n2 == sum:
        print('Armstrong Number')
    else:
        print('Not a Armstrong')
armstrong(153)
armstrong(45)
