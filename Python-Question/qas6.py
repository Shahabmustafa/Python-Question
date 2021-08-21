# (4) A simple Cuboid class [2 pts.]

# Write a simple Cuboid class with the following attributes and methods:
# Attributes:
# length, width, height (all three are integers)
# Methods:
# ● An initializer __init__(self,l,w,h) which sets the Cuboid instance’s length, width and
# height from user­provided arguments
# ● A method get_area(self) which takes no arguments and returns the Cuboid’s surface
# area (2*length*width + 2*width*height + 2*height*length)
# ● A method get_volume(self) which takes no arguments and returns the Cuboid’s volume
# (length*width*height)
# Once you have written the class, create one instance of it with a random length, width, and
# height. Print out the Cuboid instance’s dimensions (length, width, height), surface area and
# volume. Save your work as a2­4.py

                    # ANSWER
# Python Program to find Volume and Surface Area of Cuboid

length = float(input('Please Enter the Length of a Cuboid: '))
width = float(input('Please Enter the Width of a Cuboid: '))
height = float(input('Please Enter the Height of a Cuboid: '))

# Calculate the Surface Area
SA = 2 * (length * width + length * height + width * height)

# Calculate the Volume
Volume = length * width * height

print("\n The Surface Area of a Cuboid" ,SA)
print(" The Volume of a Cuboid ", Volume)
