import re
from sets import Set
import random
import pickle

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
	stringT = re.sub('\\n',' ',stringT);# Hmm, I wonder what would happen if I left this in, it might actually work out and create paragraphs...
	stringT = re.sub('\t',' ',stringT);
	stringT = re.sub('  ',' ',stringT);
	stringT = re.sub('   ',' ',stringT);
	stringT = re.sub('    ',' ',stringT);
	stringT = re.sub('     ',' ',stringT);
	stringT = re.sub('      ',' ',stringT);
	stringT = re.sub('       ',' ',stringT);
	stringT = re.sub('        ',' ',stringT);
	
	# Strip out words into a set, and union it with the previously built dictionary
	dictionary = dictionary | set(stringT.split());
	
	# Mash together all of the texts for easy working:
	alltext = alltext + stringT + ' ';
	
	
#Set order is preserved...right?
dictionaryList = list(dictionary);
	
splitText = alltext.split();
freqdict = {};
count = 0;
splitlength = len(splitText)
viewStep = 100;# How often the count is to be displayed to the user

# It would be nice if this could be optimized:
for p in range(splitlength-1):
	count = count + 1;# Purely for the readout below
	if count%viewStep == 0:
		print 'Text Word ' + str(count) + '/' + str(splitlength) + ': ' + splitText[p]
	
	# Determine the index for the current word
	pIndex = dictLookup(splitText[p],dictionaryList);
	# Determine the index for the next word
	nextIndex = dictLookup(splitText[p+1],dictionaryList);
	
	# If the word doesn't have a freq table yet...
	if freqdict.get(pIndex,-1) == -1:
		# Give it a nested dict
		freqdict[pIndex] = {};
	
	# If the next word already exists as a key in the nested dictionary under the beginning word...
	if freqdict.get(pIndex).get(nextIndex,-1) != -1:
		# Add one to the count
		freqdict[pIndex][nextIndex]=freqdict[pIndex][nextIndex]+1;
	else:
		# Create the entry with it's first count:		
		freqdict[pIndex][nextIndex] = 1;
		
# Save this for use by the constructor.py
pickle.dump(freqdict,open("freqdict.p","wb"));

pickle.dump(dictionaryList,open("dictionaryList.p","wb"));

print 'There are ' + str(len(dictionaryList)) + ' unique words in these combined texts.'