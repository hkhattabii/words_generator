from __future__ import division
import random


def strToLower(str):
  return str.lower()

def removeDelimiter(line, delimiter):
  line = line.split(delimiter)[0]
  return strToLower(line)

def noneToZero(frequencies):
  frequenciesCount = len(frequencies)
  for i in range(frequenciesCount):
    if frequencies[i] == None:
      frequencies[i] = 0


def fileToList(fileName):
  list = []
  with open(fileName) as file:
    for line in file:
      word = removeDelimiter(line, "\n")
      list.append(word)
  return list

def initFrequenciesArr():
  frequencies = [None] * LETTER_COUNT
  return frequencies

def increaseFrequency(frequencies, letterPos):
  print(frequencies)
  currentFrequency = frequencies[letterPos]
  if currentFrequency == None:
    frequencies[letterPos] = 1
    return
  frequencies[letterPos] += 1


def getNeighbors(word, pos):
  if len(word) > (pos + NEIGHBOR_DEEP):
    neighbors = strToLower(word[pos + 1: pos + NEIGHBOR_DEEP +1])
    return neighbors
  return None
  

def countFrequenciesTot(word):
  for letter in word:
    letterPos = ALPHABETS.index(letter)
    increaseFrequency(frequenciesTot, letterPos)

def countFrequenciesFrstLetter(letter):
  frstLetterPos =  ALPHABETS.index(letter)
  increaseFrequency(frequenciesFrst, frstLetterPos)

def countPossibleNeighbors(word):
  for letter in word:
    letterPosRelative = word.index(letter)
    letterPosAbsolute = ALPHABETS.index(letter)
    neighbors = getNeighbors(word, letterPosRelative)
    if neighbors == None:
      continue
      
    arrOfNeighbors = possibleNeighbors[letterPosAbsolute]
    
    if arrOfNeighbors == None:
      possibleNeighbors[letterPosAbsolute] = [neighbors]
      continue
    if neighbors not in arrOfNeighbors:
      arrOfNeighbors.append(neighbors)
      possibleNeighbors[letterPosAbsolute] = arrOfNeighbors

def countFrequenciesNeighbors(word):
  for letter in word:
    letterPosRelative = word.index(letter)
    letterPosAbsolute = ALPHABETS.index(letter)
    neighbors = getNeighbors(word, letterPosRelative)
    if neighbors == None:
      continue

    neigborPos = possibleNeighbors[letterPosAbsolute].index(neighbors)

def frequenciesToRelative(frequencies):
  noneToZero(frequencies)
  frequenciesCount = len(frequencies)
  totalLetters = sum(frequencies)
  for i in range(frequenciesCount):
    frequency = frequencies[i]
    frequencies[i] = round((frequency / totalLetters) * 100, 8)

def countFrequencies(fileName):
  with open(fileName) as file:
    for line in file:
      word = removeDelimiter(line, "\n")
      # frstLetter = strToLower(word[0])
      # countFrequenciesTot(word)
      # countFrequenciesFrstLetter(frstLetter)
      countPossibleNeighbors(word)
      countFrequenciesNeighbors(word)



  print(frequenciesNeighbors[0])
  # frequenciesToRelative(frequenciesTot)
  # frequenciesToRelative(frequenciesFrst)


NEIGHBOR_DEEP = 2
ALPHABETS = fileToList("./alphabets.txt")
LETTER_COUNT = len(ALPHABETS)
possibleNeighbors = initFrequenciesArr()
frequenciesTot = initFrequenciesArr() 
frequenciesFrst = initFrequenciesArr()
frequenciesNeighbors = initFrequenciesArr()
print("The file is converting into array of lines ...")
countFrequencies("./words.txt")







