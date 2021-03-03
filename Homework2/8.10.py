#ZyLabs 8.10 Jai Kapoor 1901832

x = input()

y = x.replace(' ','')

z = y[::-1]

if z == y:
    print (x, 'is a palindrome')
else:
    print (x, 'is not a palindrome')
