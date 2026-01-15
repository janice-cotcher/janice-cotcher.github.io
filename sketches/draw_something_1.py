# student example

from processing import *

def draw():
  size(480, 270)
  # Screen
  rect(5, 5, 470, 260)
  # Taskbar
  rect(5, 245, 470, 20)
  # - Start Button
  rect(5, 245, 25, 20)
  line(12, 252, 12, 258)
  line(23, 250, 23, 260)
  line(16, 251, 16, 259)
  line(12, 255, 23, 255)
  line(12, 252, 23, 250)
  line(12, 258, 23, 260)
  # - Search Box
  rect(30, 245, 115, 20)
  ellipse(43, 253, 6, 6)
  line(41, 255, 36, 259)
  fill(0,0,0)
  textSize(9)
  text("Type here to search", 52, 259)
  fill(255,255,255)
  # - Pinned Icons
  ellipse(158, 255, 8, 8)
  rect(172, 251, 8, 8)
  rect(190, 251, 8, 8)
  rect(208, 251, 8, 8)
  rect(226, 251, 8, 8)
  # - Right Corner
  line(387, 258, 391, 254)
  line(391, 254, 395, 258)
  rect(400, 253, 5, 5)
  rect(410, 253, 5, 5)
  fill(0,0,0)
  textSize(8)
  text("12:00 AM", 427, 253)
  text("14-Sep-2021", 422, 262)
  fill(255,255,255)
  rect(472, 245, 3, 20)
  # Google Toolbar
  # - Arrows
  rect(5, 20, 470, 20)
  line(10, 30, 20, 30)
  line(10, 30, 15, 25)
  line(10, 30, 15, 35)
  line(25, 30, 35, 30)
  line(35, 30, 30, 25)
  line(35, 30, 30, 35)
  # - Reload and Home Buttons
  ellipse(50, 30, 10, 10)
  fill(0,0,0)
  triangle(52, 28, 55, 25, 55, 28)
  fill(255,255,255)
  rect(64, 27, 7, 7)
  line(63, 28, 68, 24)
  line(68, 24, 73, 28)
  # - URL
  rect(80, 22, 360, 16)
  fill(0,0,0)
  text("google.com", 85, 33)
  fill(255,255,255)
  # - Right Side
  ellipse(455, 30, 10, 10)
  point(467, 26)
  point(467, 30)
  point(467, 34)
  # Tabs
  # - First Tab
  rect(5, 5, 80, 15)
  ellipse(13, 13, 6, 6)
  fill(0,0,0)
  text("Trinket", 20, 16)
  fill(255,255,255)
  line(75, 11, 79, 15)
  line(75, 15, 79, 11)
  # - Second Tab
  rect(85, 5, 80, 15)
  ellipse(93, 13, 6, 6)
  fill(0,0,0)
  text("Google", 100, 16)
  fill(255,255,255)
  line(155, 11, 159, 15)
  line(155, 15, 159, 11)
  # - Plus Sign
  line(175, 9, 175, 15)
  line(172, 12, 178, 12)
  # Minimize, Window, and Close Boxes
  rect(455, 5, 20, 15)
  rect(435, 5, 20, 15)
  rect(415, 5, 20, 15)
  # Minimize, Window, and Close Symbols
  line(462, 10, 468, 16)
  line(462, 16, 468, 10)
  rect(443, 9, 5, 5)
  rect(441, 11, 5, 5)
  line(423, 12, 428, 12)
  # Main Page
  fill(0,0,0)
  textSize(30)
  text("Google", 190, 125)
  fill(255,255,255)
  rect(140, 140, 200, 20)
  ellipse(148, 148, 6, 6)
  line(150, 150, 155, 155)
  line(160, 145, 160, 155)
  
run()