import colorama as c
from datetime import datetime

reset = c.Style.RESET_ALL

c.init()

def log(message):
  plain(message)

def plain(message):
  print (timestamp() + message)

def timestamp():
  currentTime = datetime.now()
  now = currentTime.strftime("%H:%M:%S")
  return c.Fore.LIGHTBLUE_EX + str(now) + c.Style.RESET_ALL + ' '

def bGreen(message):
  print(timestamp() + c.Back.GREEN + message + reset)

def bRed(message): 
  print(timestamp() + c.Back.RED + message + reset)

def bWhite(message):
  print(timestamp() + c.Back.WHITE + c.Fore.BLACK + message + reset)

def tRed(message):
  print(timestamp() + c.Fore.RED + message + reset)

def tGreen(message):
  print(timestamp() + c.Fore.LIGHTGREEN_EX + message + reset)

def bBlue(message):
  print(timestamp() + c.Back.BLUE + c.Fore.WHITE + message + reset)