def automorphic(n):
    sq = n**2
    temp = n
    mod = 1
    while temp > 0:
        mod *= 10
        temp //= 10
    if sq%mod == n:
        print('Automorphic Number')
    else:
        print('Not a Automorphic Number')
automorphic(25)
automorphic(5)
automorphic(12)

 
