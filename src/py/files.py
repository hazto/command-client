import os
import constants

def getGoblins():
  images = os.listdir(constants.goblinAssets)
  return [constants.goblinAssets + '/' + img for img in images]

def getClose():
  images = os.listdir(constants.closeAssets)
  return [constants.closeAssets + '/' + img for img in images]

def getChests():
  images = os.listdir(constants.chestAssets)
  return [constants.chestAssets + '/' + img for img in images]

def getAnchors():
  images = os.listdir(constants.anchorAssets)
  return [constants.anchorAssets + '/' + img for img in images]

def getImages(folder):
  images = os.listdir(folder)
  return [folder + '/' + img for img in images]
  