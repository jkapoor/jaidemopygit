#ZyLabs 6.17 Jai Kapoor 1901832

word = input()
password = ''

word = word.replace('i', '!')
word = word.replace('a', '@')
word = word.replace('m', 'M')
word = word.replace('B', '8')
word = word.replace('o', '.')

word += 'q*s'

print(word)
