import random
import time
import pyautogui
import logger as c
import move

plotOffsetX = 45
plotOffsetY = 45

field1AnchorOffsetX = 305
field1AnchorOffsetY = -315

fieldOffset_1 = (305, -315)
fieldOffset_2 = (56, -142)

field1 = (fieldOffset_1 ,2, 2)
field2 = (fieldOffset_2, 3, 3)

fields = (field1, field2)

def harvest(anchor, suppressMessage=False): 
  print('harvesting!')
  if not suppressMessage:
    c.bGreen('harvest')
  # locate starting point
  
  if not anchor:
    c.log('cant find anchor!')
    return

  for field in fields:
    start = getFieldStart(anchor, field[0][0], field[0][1])
    doField(start, field[1], field[2])

  print('harvesting! done')

def getFieldStart(anchor, xOffset, yOffset):
  x = anchor.left + xOffset
  y = anchor.top + yOffset

  return pyautogui.position(x, y)

def doField(start, width, height):
  for i in range(height):
    for n in range(width):  
      x = start.x + plotOffsetX * n
      y = start.y + plotOffsetY * i
      moveTo(x, y, 0.08)
      time.sleep(0.05)
      click()

def click():
  delay = random.randint(0, 100) * 0.001
  time.sleep(delay)
  pyautogui.click()

def moveTo(x, y, duration=0.1, precise=False, offsetRange=4):
  move.moveTo(x, y, duration, precise, offsetRange)

anchor = move.wakeAndFocus()
if not anchor:
  time.sleep(1)
  anchor = move.getAnchor()

harvest(anchor)
