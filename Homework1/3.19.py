#Zylabs 3.18 Jai Kapoor 1901832
import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_width * wall_height

gallon = 350.00
paint_needed = float(wall_area/gallon)

print('Wall area: ' + str(wall_area) + ' square feet')
print('Paint needed: ' + ('{:.2f}'.format(paint_needed)) + ' gallons')

if paint_needed <= 1:
    cans_needed = 1
else:
    cans_needed = math.ceil(paint_needed)

print('Cans needed: ' + str(cans_needed) + ' can(s)\n')

color = (input('Choose a color to paint the wall: \n'))
if color == 'red':
    print(paint_colors['red'])



# FIXME (4): Calculate and output the total cost of paint can needed depending on color
