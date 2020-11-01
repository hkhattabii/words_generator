from __future__ import division
import random

# Return a string in lower case
def strToLower(str):
  return str.lower()
# Return a string by removing the delimiter
def removeDelimiter(line, delimiter):
  line = line.split(delimiter)[0]
  return strToLower(line)
# Return an element containing in a list by taking one regarding to a probability computed in advance
def getByProbability(list, probabilities, nbLetters):
  lettersArr = random.choices(list, weights=tuple(probabilities), k=nbLetters)
  return "".join(lettersArr)

#  Read a file and return a list of line
def fileToList(fileName):
  list = []
  with open(fileName) as file:
    for line in file:
      line = removeDelimiter(line, "\n")
      list.append(line)
  return list
# Initialize a dictionnary which contains all the informations
def initDictionnary():
  dictionnary = {
    "totalLetters": 0,
    "totalFrstLetters": 0,
    "letters": {}
  }
  for letter in ALPHABETS:
    dictionnary["letters"][letter] = {
      "total": 0,
      "frst": 0,
      "totalNeighbors": 0,
      "neighbors": {}
    }
  return dictionnary

# Get the neighors of a letter regarding to the deep inserted
def getNeighbors(word, pos):
  if len(word) > (pos + NEIGHBOR_DEEP):
    neighbors = word[pos + 1: (pos + NEIGHBOR_DEEP) + 1]
    return neighbors
  return None

# Count the number of occurence of each letter and also increment the total letters in the whole file for calcalting the relative occurence
def countFrequenciesTot(word):
  for letter in word:
    frequencies["totalLetters"] += 1
    frequencies["letters"][letter]["total"] += 1

# Cuunt the number of occurence of each first letter
def countFrequenciesFrst(letter):
  frequencies["totalFrstLetters"] += 1
  frequencies["letters"][letter]["frst"] += 1
# Count he number of occurence of each neighbor of a letter
def countFrequenciesNeighbor(word):
  letterCount = len(word)
  for i in range(letterCount):
    letter = word[i] # Get the letter
    neighbors = getNeighbors(word,i) # Get its neighbors
    if neighbors == None: #If there are no neighbors, do nothing
      continue
    frequencies["letters"][letter]["totalNeighbors"] += 1  # Increment by one the number of neighbors that he letter has
    neighborFrequencies = frequencies["letters"][letter]["neighbors"].get(neighbors, 0) # Get the current occurence of a neighbor, if it is not exisitng return 0
    frequencies["letters"][letter]["neighbors"][neighbors] = neighborFrequencies + 1 # Increment the occurence neighbors of a letter 

# Loop throught the file of word and count the occurence for the letters, the first letter and the neighbor of a letter
def countFrequencies(fileName):
  with open(fileName) as file:
    for line in file:
      word = removeDelimiter(line, "\n")
      frstLetter = word[0]
      countFrequenciesTot(word)
      countFrequenciesFrst(frstLetter)
      countFrequenciesNeighbor(word)

# Translate all the frequencies ( occurence ) to a relative number if %
def frequenciesToRelatives():
  totalLetters = frequencies["totalLetters"] # Get the total of letters in the file
  totalFrstLetters = frequencies["totalFrstLetters"]  # Get the total of first letter in the file
  for letter in frequencies["letters"]: # Loop through each letter to a - special character
    total = frequencies["letters"][letter]["total"] # Get the total occurence of that letter in the fille
    frst = frequencies["letters"][letter]["frst"] # Get the total occurence of that letter which is in a begining of a word
    frequencies["letters"][letter]["total"] = round((total / totalLetters) * 100, 8) # 
    frequencies["letters"][letter]["frst"] = round((frst / totalFrstLetters) * 100, 8)
    totalNeighbors = frequencies["letters"][letter]["totalNeighbors"] # Get the total of neighbor that the letter has
    for neighbor in  frequencies["letters"][letter]["neighbors"]:
      totalNeighbor = frequencies["letters"][letter]["neighbors"][neighbor] # Get the total occurence of that neighbor
      frequencies["letters"][letter]["neighbors"][neighbor] = round((totalNeighbor / totalNeighbors) * 100, 8)

# Translate dictionnary values into list of values. The type represent a sub dictionary ( frst, total, ...)
def MergeDicToList(type, dict):
  list = []
  #print('DICT', dict)
  for x in dict:
    list.append(dict[x][type]) if type != None else list.append(dict[x])
  return list

# Generate a word by taking a letter randomly with a probability and concat this letter with its neighbors with also a probabiity
# As we select the neighbor of a letter, I have to make some computation before entering to the Loop
# If we want 6 letters for exemple, we can't iterate 6x to get 6 letters because we have to concat the nighbors regarding to the deep. So if the deep is 2, The program has to iterate 2x 
# During the iteration, it verifies first if it is the first loop, so take a letter regardging to the probability of a first letter in a french word and concat it by its neighbors regarding also by the probability that the neighbor follows that letter
# Return the word generate by cutting the word to get the right size
def genWord(wordSize):
  letters = frequencies["letters"] # Get the letters dictionnary
  defaultLetterCount = 1 # Indicate that we select one letter by default
  letterWithNeighborCount = defaultLetterCount + NEIGHBOR_DEEP 
  rest = wordSize % letterWithNeighborCount
  iterateCount = wordSize if rest == 0 else (wordSize - rest) + letterWithNeighborCount
  newWord = ""
  for i in range(iterateCount // letterWithNeighborCount):
    firstPart = getByProbability(ALPHABETS, MergeDicToList("frst", letters), 1) if i == 0 else getByProbability(ALPHABETS, MergeDicToList("total", letters), 1)
    neighbors = list(frequencies["letters"][firstPart]["neighbors"].keys())
    secondPart = getByProbability(neighbors, MergeDicToList(None, frequencies["letters"][firstPart]["neighbors"]),1)
    newWord += firstPart + secondPart

  return newWord[0: wordSize]



userDeep = input("Insert a neighbor deep : ")
NEIGHBOR_DEEP = int(userDeep)
ALPHABETS = fileToList("./alphabets.txt")
frequencies = initDictionnary()
countFrequencies("./words.txt")
frequenciesToRelatives()


while True:
  userWordSize = input("Insert the size of the word : ")
  wordGenerated = genWord(int(userWordSize))
  print(wordGenerated)






