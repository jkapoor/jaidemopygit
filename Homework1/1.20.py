#ZyLabs 1.20 Jai Kapoor 1901832

print('Enter integer:')
user_num1 = int(input())
print('You entered: ' + str(user_num1))

user_2 = user_num1 * user_num1
user_3 = user_num1 * user_num1 * user_num1

a = ' squared is '
b = ' cubed is '
c = 'And '
d = ' !!'
e = ' is '
f = 4
plus = ' + '
mult = ' * '

print(str(user_num1) + a + str(user_2))
print(c + str(user_num1) + b + str(user_3) + d)

print('Enter another integer:')
user_num2 = int(input())
user_num4 = 4 + user_num2
user_num5 = 4 * user_num2

print(str(f) + plus + str(user_num2) + e + str(user_num4))
print(str(f) + mult + str(user_num2) + e + str(user_num5))

