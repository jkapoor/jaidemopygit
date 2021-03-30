#ZyLabs 11.22 Jai Kapoor 1901832
user_input = input()
list_of_words = user_input.split()

for element in list_of_words:
    count = 0
    for current in list_of_words:
        if element == current:
            count += 1
    print(element, count)   
