from __future__ import division
import random



# Translate None varialbe into zero integer
def NoneToZero(frequencies):
  frequenciesCount = len(frequencies)
  for i in range(frequenciesCount):
    if frequencies[i] == None:
      frequencies[i] = 0
  return frequencies

# Remove delimiter of a string variable
def removeDelimiter(line, delimiter):
    return line.split(delimiter)[0]

# Translate a file into a list of word
# Also append all the possibilities of the first two letter after a letter
def fileToList(fileName):
    list = []
    twoLetterslist = []
    with open(fileName) as file:
        for line in file:
            word = removeDelimiter(line, "\n")
            list.append(word)
            for i in range(len(word)):
              if len(word) > (i+1) and len(word) > (i+2):
                twoLetter = word[i+1] + word[i+2]
                if twoLetter not in twoLetterslist:
                  twoLetterslist.append(twoLetter.lower())
    return list, twoLetterslist

# Initiliaze an array of frequencies by default with NONE Frequency
def initFrequency():
  frequencies = [None] * LETTER_COUNT
  lettersTotalCount = 0;
  return frequencies, lettersTotalCount

# Increase the frequency of a letter
def increaseFrequency(frequencies, letterPos):
  currentFrequency = frequencies[letterPos]
  if currentFrequency == None:
    frequencies[letterPos] = 1
  else:
    frequencies[letterPos] += 1
  
# Return the relative frequencies of the letters of all words in the file
def countFrequencyTot():
  frequenciesTot, lettersTotalCount = initFrequency()
  for word in words:
    for letter in word:
      letterPos = ALPHABETS.index(letter.lower())
      increaseFrequency(frequenciesTot, letterPos)
      lettersTotalCount += 1
  return frequencyToRelative(frequenciesTot, lettersTotalCount)

# Return the relative frequencies of the first letter of all words in the file
def countFrequencyFrstLetter():
  frequenciesFrst, lettersTotalCount = initFrequency()

  for word in words:
    frstLetter = word[0]
    frstLetterPos = ALPHABETS.index(frstLetter.lower())
    increaseFrequency(frequenciesFrst, frstLetterPos)
    lettersTotalCount += 1
  
  frequenciesFrst = NoneToZero(frequenciesFrst)
  return frequencyToRelative(frequenciesFrst, lettersTotalCount)

# Return the relative frequencies of the two first letter following a specific letter
# The idea is to store the relative frequencies in a second dimensional array
# Each position of the first array is the position of the letter in the alphabet
# And on all of that position there is an array of frequencies which could be follow the specific letter
def countFrequencyScndLetter():
  frequenciesScnd = [[None] * len(twoLetters) for _ in range(LETTER_COUNT)]

  for word in words:
    for i in range(len(word)):
      letter = word[i].lower()
      letterPos = ALPHABETS.index(letter)
      if len(word) > (i+1) and len(word) > (i+2):
        firstSndLetter = word[i + 1].lower()
        sndSndLetter = word[i + 2].lower()
        twoLetter = firstSndLetter + sndSndLetter
        twoLetterPos = twoLetters.index(twoLetter)
        currentFrequency = frequenciesScnd[letterPos][twoLetterPos]
        if currentFrequency == None:
          frequenciesScnd[letterPos][twoLetterPos] = 1
        else:
          frequenciesScnd[letterPos][twoLetterPos] += 1

  frequenciesScndCount = len(frequenciesScnd)
  for i in (range(frequenciesScndCount)):
    frequenciesScnd[i] = NoneToZero(frequenciesScnd[i])
    frenquenciesCount = len(frequenciesScnd[i])
    frequenciesSum = sum(frequenciesScnd[i])
    for j in range(frenquenciesCount):
      frequency = frequenciesScnd[i][j]
      if frequenciesSum == 0:
        frequenciesScnd[i][j] = 0.0
        continue

      frequenciesScnd[i][j] = round((frequency / frequenciesSum ) * 100, 8)

  return frequenciesScnd
    

# Translate the frequency number into a relative frequency regarding to the total possibly letters
def frequencyToRelative(frequencies, lettersTotalCount):
  frequenciesCount = len(frequencies)
  for i in range(frequenciesCount):
    frequency = frequencies[i]
    if frequency != None:
        frequencies[i] = round((frequency / lettersTotalCount) * 100, 8)
  return frequencies


def getByProbability(list, probabilites, nbrLetters): 
  lettersArr = random.choices(list, weights=tuple(probabilites), k=nbrLetters)
  return "".join(lettersArr)


# Generate the word of wordSize size
# Iterate n time if the n has no rest. If there is a rest iterate x time which x is the first multiple
# Take in the alphabets regarding to the relative frequency ONE letter
# Take the second first letter following this specific letter
# In the end, slice the string by keeping the right size
def genWord(wordSize):
  rest = wordSize % 3
  iterateCount = wordSize if rest == 0 else (wordSize - rest) + 3
  newWord = ""
  for i in range (iterateCount // 3 ):
    firstPart = getByProbability(ALPHABETS, frequenciesFrst, 1) if i == 0 else getByProbability(ALPHABETS, frequenciesTot,1)
    firstPartPos = ALPHABETS.index(firstPart)
    FirstPartSndFreqencies = frequenciesScnd[firstPartPos]
    secondPart = getByProbability(twoLetters, FirstPartSndFreqencies, 1)
    newWord += firstPart + secondPart
  
  return newWord[0:wordSize]



# Initialize variables
ALPHABETS = fileToList("./alphabets.txt")[0];
LETTER_COUNT = len(ALPHABETS)
words = []
frequenciesTot = []
frequenciesFrst = []
frequenciesScnd = []
twoLetters = []


print("The file is converting into array of lines ...")
words, twoLetters = fileToList("./words.txt")
print("Done !")
print("Compute the frequency of each letters ...")
frequenciesTot = countFrequencyTot()
print("Done !")
print("Compute the frequency of first letter of each word ...")
frequenciesFrst = countFrequencyFrstLetter()
print("Done !")
print("Compute the frequency of the first second letter of each letter of each word")
frequenciesScnd = countFrequencyScndLetter()

print("Sum tot : ", sum(frequenciesTot))
print("Sum First : ", sum(frequenciesFrst))
print("Surm second : ", sum(frequenciesScnd[0]))


while (True):
  letterNbr = input("Introduce the size of the word : ")
  newWord = genWord(int(letterNbr))
  print(newWord)


        
    
            





