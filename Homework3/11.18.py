#ZyLabs 11.18 Jai Kapoor 1901832

numbers = [int(i) for i in input().split()]

numbers.sort()

nonnegative_numbers = [i for i in numbers if (i >= 0)]
print(*nonnegative_numbers, sep=' ', end='' + ' ')
