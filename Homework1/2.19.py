#Zylabs 2.19 Jai Kapoor 1901832

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print('')
print('Lemonade ingredients - yields ' + ('{:.2f}'.format(servings) + ' servings'))

print('{:.2f}'.format(lemon_juice_cups) + ' cup(s) lemon juice')
print('{:.2f}'.format(water_cups) + ' cup(s) water')
print('{:.2f}'.format(agave_nectar_cups) + ' cup(s) agave nectar\n')


desired_servings = float(input('How many servings would you like to make?\n'))
print('')
print('Lemonade ingredients - yields ' + ('{:.2f}'.format(desired_servings) + ' servings'))

if desired_servings == 48.00:
    desired_lemon_juice_cups = lemon_juice_cups * 8
    desired_water_cups = water_cups * 8
    desired_agave_nectar_cups = agave_nectar_cups * 8
else:
    desired_lemon_juice_cups = lemon_juice_cups / 2
    desired_water_cups = water_cups / 2
    desired_agave_nectar_cups = agave_nectar_cups / 2


print('{:.2f}'.format(desired_lemon_juice_cups) + ' cup(s) lemon juice')
print('{:.2f}'.format(desired_water_cups) + ' cup(s) water')
print('{:.2f}'.format(desired_agave_nectar_cups) + ' cup(s) agave nectar\n')


lemon_gallons = desired_lemon_juice_cups/16
water_gallons = desired_water_cups/16
agave_gallons = desired_agave_nectar_cups/16

print('Lemonade ingredients - yields ' + ('{:.2f}'.format(desired_servings) + ' servings'))

print('{:.2f}'.format(lemon_gallons) + ' gallon(s) lemon juice')
print('{:.2f}'.format(water_gallons) + ' gallon(s) water')
print('{:.2f}'.format(agave_gallons) + ' gallon(s) agave nectar')