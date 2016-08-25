import re
from sets import Set
import random

# Create the catalogue of all of the words
# Empty dictionary to build
dictionary = set([]);

# A list of all of the text files we're going to use:
listT = ['aliceinwonderland.txt', 'aroundtheworldineightydays.txt', 'gulliverstravels.txt', 'history of ireland.txt', 'spacepirates.txt'];
stringT = [None]*100;

def dictLookup(word,wordlist):
	for i in range(len(wordlist)):
		if wordlist[i] == word:
			return i;

alltext = '';
for k in range(len(listT)):

	a = open(listT[k], 'r');
	stringT = a.read();
	
	# Prep it for human reading
	stringT = re.sub('\\n',' ',stringT);
	stringT = re.sub('\t',' ',stringT);
	stringT = re.sub('  ',' ',stringT);
	stringT = re.sub('   ',' ',stringT);
	stringT = re.sub('    ',' ',stringT);
	stringT = re.sub('     ',' ',stringT);
	stringT = re.sub('      ',' ',stringT);
	stringT = re.sub('       ',' ',stringT);
	stringT = re.sub('        ',' ',stringT);
	
	# Strip out words into a set, and OR it with the previously built dictionary
	dictionary = dictionary | set(stringT.split());
	
	#Mash together all of the texts for easy working:
	alltext = alltext + stringT + ' ';
	
	
#Set order is preserved...right?
dictionaryList = list(dictionary);
	
splitText = alltext.split();
freqdict = {};
for p in splitText:
	
	pIndex = dictLookup(p,dictionaryList);
	nextIndex = dictLookup(p,dictionaryList);# The next word in the text.
	if nextIndex in freqdict[pIndex]:# If the next word already exists as a key in the nested dictionary under the beginning word...
		# Add one to the count
		freqdict[pIndex][nextIndex]=freqdict[pIndex][nextIndex]+1;
	else:
		# Create the entry:
		freqdict[pIndex][nextIndex] = '0';
		


	
excerptLength = 100;# Number of words

# Based on how I've constructed this, make your sentences out of indices from the dictionaryList,
# and then at the very end turn it into human words.

# Start with a random word
startingWordind = random.randint(0,len(dictionaryList));
excerpt[0] = startingWordInd;

# Starting on the second word...
for j in range(1,excerptLength):
	# Roll the dice for this next word
	decisionlist = '';
	# Find the total sum count...
	for key in freqdict[excerpt[j-1]]:#For every word underneath the particular word
		decisionlist = decisionlist + freqdict[excerpt[j-1]][key]*key;# Elegant trick to make this work...
	excerpt[j] = random.choice(decisionlist);#jth excerpt now contains the index of the next word.
	
# Now turn it into an actual sentence:
excerptEnglish = '';
for q in excerpt:
	excerptEnglish = excerptEnglish + dictionaryList[q];

print excerptEnglish;