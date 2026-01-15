from processing import *

def draw():
  # This code will print out a simple drawing of a man with a hat

  # Draw a 300 x 400 window
  size (300, 400) 
  # Draw a triangle with points (150, 150), (120, 80) and (180, 80)
  triangle(150, 50, 120, 80, 180, 80)
  # Draw a circle centered at (150, 200) with diameter of 40
  ellipse(150, 100, 40, 40)
  # Draw a 40 x 70 rectangle with top left 10 corner at (130, 120)
  rect(130, 120, 40, 70)
  # Draw line from (130, 140) to (100, 120)
  line(130, 140, 100, 120)
  # Draw line from (170, 140) to (200, 120)
  line(170, 140, 200, 120)
  # Draw line from (140, 190) to (130, 230)
  line(140, 190, 130, 230)
  # Draw line from (160, 190) to (170, 230) 
  line(160, 190, 170, 230)

run()