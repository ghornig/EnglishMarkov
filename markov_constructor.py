import re
from sets import Set
import random
import pickle

# Open up the files previously created by the parser
freqdict = pickle.load(open("freqdict.p","rb"));
dictionaryList = pickle.load(open("dictionaryList.p","rb"));

# Number of words
excerptLength = 600;

# Based on how I've constructed this, make your sentences out of indices from the dictionaryList,
# and then at the very end turn it into human words.

# Start with a random word
startingWordInd = random.randint(0,len(dictionaryList));
excerpt = ['']*excerptLength;
excerpt[0] = startingWordInd;

# Starting on the second word...
for j in range(1,excerptLength):
	#print str(excerpt[j-1])
	decisionlist = [];
	# Find the total sum count...
	#print 'Here: ' + str(freqdict.get(excerpt[j-1]))
	for key in freqdict.get(excerpt[j-1]):#For every word underneath the particular word
		decisionlist.extend(freqdict.get(excerpt[j-1]).get(key)*[key]);# Elegant trick to make this work...
	excerpt[j] = random.choice(decisionlist);#jth excerpt now contains the index of the next word.
	
# Now turn it into an actual sentence:
excerptEnglish = '';
for q in excerpt:
	excerptEnglish = excerptEnglish + ' ' + dictionaryList[q];

print excerptEnglish;

text_file = open("Output.txt", "w")
text_file.write(excerptEnglish)
text_file.close()