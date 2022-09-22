def assign_name(name):
    print("His name is", name)
assign_name("felix")

# cod eto calculate the areas of various shapes
import math

def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Enter either circle or rectangle")

def rectangle_area():
    length = float(input("enter the length: "))
    width = float(input("enter the width: "))
    area = length * width
    print("Area of rectangle is: ", area)
def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print("area of circle is {:.2f}".format(area))



def main():
    shape_type = input("Which sahpe do you want the area of: ")
    get_area(shape_type) #calls the function to check the shape entered

main()
