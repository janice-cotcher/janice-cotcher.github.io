# Calculate the surface area and volume of a triangular pyramid
def area_tri(b,h):
  """Calculate the area of a triangle for base b and height h"""
  return 0.5*b*h


def surface_area(b,h):
  """Calculate the surface area of a triangular pyramid with equal faces
  where b is the base and h is the height of each side
  """
  SA = 4 * area_tri(b,h)
  print("The total surface area is " + str(SA) + "cm^2")


def volume(b, h, H):
  """Calculate the volume of a triangular pyramid with equal faces
  where b is the base and h is the height of each side and H is
  the height if the pyramid
  """
  V = (1/3)*area_tri(b,h)*H
  print("The volume is " + str(V) + "cm^3")


def py_values(b, h, H):
  """Call surface area and volume of a triangular pyramid"""
  print("Characteristics of a Triangular Pyramid:")
  print("The area of the triangular ends are " +str(area_tri(b,h)) +"cm^2")
  surface_area(b, h)
  volume(b, h, H)
  print("\n")


py_values(2, 3, 5)
py_values(5.0,6.0, 10.0)