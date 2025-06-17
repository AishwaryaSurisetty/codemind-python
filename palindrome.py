def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        dig = n%10
        rev = rev*10 + dig
        n //= 10
    if temp == rev:
        print('Palindrome Number')
    else:
        print('Not a palindrome')
palindrome(21)
palindrome(11)
palindrome(121)
