'''
Write code to generate a random password of 8 characters. The passwords generated will be 8 characters long 
and will have to include the following characters in any order:

2 uppercase letters from A to Z,
2 lowercase letters from a to z,
2 digits from 0 to 9,
2 punctuation signs such as !, “, # etc 
'''

import random

#Function to shuffle string
def shufflePassword(password):
  temp = list(password)
  random.shuffle(temp)
  return ''.join(temp)

#Function to create random uppercase letter
def getRandomUpperCaseLetter():
    return chr(random.randint(65,90))

#Function to create random lowercase letter
def getRandomLowerCaseLetter():
    return chr(random.randint(97,122))

#Function to create random digit
def getRandomDigit():
    return chr(random.randint(48,57))

#Function to create random special letter
def getRandomSpecialChar():
    return chr(random.randint(33,38))

def generatePassword():
    #Generate password using all the characters, in random order
    password = getRandomUpperCaseLetter() + getRandomUpperCaseLetter() + getRandomLowerCaseLetter() + getRandomLowerCaseLetter() + \
                getRandomDigit() + getRandomDigit() + getRandomSpecialChar() + getRandomSpecialChar()
    password = shufflePassword(password)
    return password

print(generatePassword())