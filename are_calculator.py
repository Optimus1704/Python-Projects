# Checkpoint Project

# Area calculator

# Graphic design

import math

print('=' * 18)
print('Area Calculator 📐')
print('=' * 18)
print('')
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')
print('')

# Error control

# I designed this error control part to avoid the ValueError quote,
# allowing the user to try until he/she enters the valid number.

while True:
    try:
        shape = int(input('Which shape: '))
        if shape in [1,2,3,4,5]:
            break
        else:
            print('')
            print('Invalid value entered')
            print('')
    except ValueError:
        print('')
        print('Enter a valid number')
        print('')

print('')

# Code

# I designed the calculator to use float values for a more realistic design,
# allowing it to work with decimals like a standard calculator.

if shape == 1:
    base = float(input('Base: '))
    height = float(input('Height: '))
    area_triangle = (height * base) / 2
    print('')
    print(f'The area is {area_triangle:.2f}')
elif shape == 2:
    width = float(input('Width: '))
    length = float(input('Length: '))
    area_rectangle = length * width
    print('')
    print(f'The area is {area_rectangle:.2f}')
elif shape == 3:
    side = float(input('Side: '))
    area_square = side ** 2
    print('')
    print(f'The area is {area_square:.2f}')
elif shape == 4:
    radius = float(input('Radius: '))
    area_circle = math.pi * (radius ** 2)
    print('')
    print(f'The area is {area_circle:.2f}')
elif shape == 5:
    print('End of session')
