# recommended
# program to calculate the area of a rectangle


def area_rect():
  """Calculate the area of rectangle with dimensions length and width"""
  length = float(input("Input the length of the rectangle: "))
  width = float(input("Input the width of the rectangle: "))
  Area = length * width
  print("The area is " + str(Area) + "cm^2")


area_rect()