def neon_num(n):
    sq = n**2
    sum = 0
    while sq > 0:
        dig = sq%10
        sum += dig
        sq //= 10
    if sum == n:
        print('Neon Number')
    else:
        print('Not a Neon Number')
neon_num(9)
neon_num(2)
neon_num(171)
neon_num(1)
