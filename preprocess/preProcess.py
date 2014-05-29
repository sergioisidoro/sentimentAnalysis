import re
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
import csv
st = LancasterStemmer()

#values = [x[1]*y[1] for x in art_gram_list if x[0] in [y[0] for y in self.gram_list]]
#grams = [words[i:i+gram] for i in range(len(words)-gram)]


file = '../data/reddit_data'
output = '../data/processed_reddit'

wordDictionary = {}
globalWordCount = {}
wordIndex = 0



csvfileWrite = open('wordList.csv', 'wb')
csvfileWrite2 = open('worgeneral.csv', 'wb')
originalText = open('original.csv', 'wb')
originalTextRef = open('ref.csv', 'wb')

csvWriter = csv.writer(csvfileWrite, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvWriter2 = csv.writer(csvfileWrite2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvWriter3 = csv.writer(originalText, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvWriter4 = csv.writer(originalTextRef, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
with open(file, mode='r') as file: # b is important -> binary
	with open(output, mode='w') as out:
		text = file.read()
		textMatch = re.findall("\<UP\>(?P<upVotes>\d+)\</UP\>\n\<DOWN\>(?P<downVotes>\d+)\</DOWN\>\n(?P<document>.*)", text)
		textSeq=[]
		existVector=[]
		countVector=[]
		original = []
		
		for i in range(len(textMatch)):
			textSeq.append([])
			original.append([])
			existVector.append([0]*wordIndex)
			countVector.append([0]*wordIndex)
			w_list = (re.split('\W+', textMatch[i][2]))
			filtered_words = [w for w in w_list if not w in stopwords.words('english')]
			for x in filtered_words:
				word = st.stem(x)
				original[i].append(x)
				textSeq[i].append(word)
				if word in wordDictionary:
					existVector[i][wordDictionary[word]] = 1
					countVector[i][wordDictionary[word]] += 1
					globalWordCount[word] += 1
				else:
					globalWordCount[word] = 1
					wordDictionary[word] = wordIndex
					existVector[i].append(1)
					countVector[i].append(1)
					wordIndex += 1
		
		
		relativeCount = [[0.0]*wordIndex]*len(textMatch)
		
		wordRef = [0]*wordIndex
		for k in wordDictionary.keys():
			wordRef[wordDictionary[k]] = k
		
		csvWriter4.writerow(wordRef)
		
		for  i in range(len(textMatch)):
			a = [0]*(wordIndex - len(existVector[i]))
			b = [0]*(wordIndex - len(countVector[i]))
			existVector[i] = existVector[i] + a
			countVector[i] = countVector[i] + b
			csvWriter.writerow(countVector[i])
			csvWriter3.writerow(original[i])
			#print i
			
			#for k in wordDictionary.keys():
				##if i == 0:
					##print countVector[i][wordDictionary[k]]
					##print globalWordCount[k]
					##print "..."
					##print float(countVector[i][wordDictionary[k]]) / globalWordCount[k]
					##print "------------"
				#relativeCount[i][wordDictionary[k]] = float(countVector[i][wordDictionary[k]]) / globalWordCount[k]
				
		#print countVector[0]
		totalDictVector = [0]*wordIndex
		for k in wordDictionary.keys():
			totalDictVector[wordDictionary[k]] = globalWordCount[k]
		
		csvWriter2.writerow(totalDictVector)

		#a =  [[st.stem(x) for x in (re.split('\W+', textMatch[i][2]))] for i in range(len(textMatch))]
	
