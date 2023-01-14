import random
import pyautogui
import files
import logger as c
import constants as img


def moveTo(x, y, duration=0.1, precise=False, offsetRange=4):
  if not precise:
    x += random.randint(-offsetRange, offsetRange)
    y += random.randint(-offsetRange, offsetRange)

  tween = pyautogui.easeOutQuad
  tweenRand = random.randint(0,10)

  match tweenRand:
    case 0:
      tween = pyautogui.easeOutQuad
    case 1:
      tween = pyautogui.easeOutQuad
    case 2:
      tween = pyautogui.easeInOutQuad
    case 3:
      tween = pyautogui.easeInBounce  
    case 4:
      tween = pyautogui.easeInBounce
    case 5:
      tween = pyautogui.easeOutQuad
    case _:
      tween = pyautogui.easeInElastic

  pyautogui.moveTo(x=x,y=y, duration=duration, tween=tween)

def wakeAndFocus():
  pyautogui.moveRel(10, 0, duration=0.5)
  pyautogui.moveRel(0, 10, duration=0.5)
  pyautogui.moveRel(-10, 0, duration=0.5)
  pyautogui.moveRel(0, -10, duration=0.5)
  anchor = getAnchor()

  return anchor

def getAnchor():
  return getFromCollection(img.anchorAssets, confidence=0.9)

def getFromCollection(assetFolder, confidence=0.92):
  target = False
  for img in files.getImages(assetFolder):
    if not target:
      c.log('locating from collection: ' + str(img))
      target = locate(img, confidence=confidence) 

  return target

def locate(image, confidence=0.9):
  return pyautogui.locateOnWindow(image, 'Sunflower Land', confidence=confidence)
