from random import randrange
import collections

# Get words
corpus = open("corpus.txt", "r")
wordLines = corpus.readlines()

for line in range(0, len(wordLines)-2):
	wordLines[line] = wordLines[line][:-1]

# Create graph of words
def createWordMap(wordLines):
	wordMap = dict()
	startWords = {}
	startIndex = 0

	for lyric in wordLines:
		line = lyric.split()
		startWords[startIndex] = [line[0], line[1]]
		startIndex += 1

		for index in range(0,len(line)-2):
			wordMap[(line[index], line[index + 1])] = line[index + 2]

	return [startWords, wordMap]

def calculateChars(array):
	char = 0
	for element in array:
		char += len(element)
	return char

# Returns true if the contents of the array is under Twitter's character limit
def underLimit(array):
	if calculateChars(array) < 140:
		return True
	else:
		return False

# Generate tweet
# array has two elements: startWords and wordMap
def genTweet(array):
	startWords = array[0]
	wordMap = array[1]

	index = randrange(len(startWords))
	nextWord = wordMap[(startWords[index][0], startWords[index][1])]
	tweetArray = [startWords[index][0], startWords[index][1], nextWord]

	currentIndex = 0

	while underLimit(tweetArray) is True:
		end = len(tweetArray)
		lastElements = [tweetArray[end-2], tweetArray[end-1]]

		clonedArray = list(tweetArray)
		
		if (lastElements[0], lastElements[1]) in wordMap:
			clonedArray.append(wordMap[(lastElements[0], lastElements[1])])
		else:
			return tweetArray

		if underLimit(clonedArray) is True:
			tweetArray = clonedArray
		else:
			return tweetArray


tweet = genTweet(createWordMap(wordLines))
print ' '.join(tweet)
