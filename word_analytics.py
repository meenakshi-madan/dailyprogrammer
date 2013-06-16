"""
Developer: Meenakshi Madan

Solution to http://www.reddit.com/r/dailyprogrammer/comments/1e97ob/051313_challenge_125_easy_word_analytics/

"""



import sys
from collections import defaultdict
import string
from operator import itemgetter



# - - - get all the data - - -

try:
  file_name = sys.argv[1]
	text = open(file_name).read()
except:
	print "Enter an existing text file location."
	
#print text
	
word = ''
new_parah = True
new_line = True
all_chars = defaultdict(lambda: 0)
all_words = defaultdict(lambda: 0)
first_words = defaultdict(lambda: 0)

for char in text:
	if not char.isspace():
		all_chars[char.lower()] += 1
		word += char
		new_line = False
	else:
		if word:
			all_words[word.lower()] += 1
			if new_parah:
				first_words[word.lower()] += 1
				new_parah = False
		if char == '\n':
			if new_line:
				new_parah = True
			new_line = True
		word = ''

if word:
	all_words[word.lower()] += 1
	if new_parah:
		first_words[word.lower()] += 1


#- - - Calculate all the statistics - - -

all_words = all_words.items()
all_chars = all_chars.items()
first_words = first_words.items()
#print all_words, all_chars
#Number of words		
n = len(all_words)
if n > 0:
	print "\n\n%d words"%n

#Number of letters	
n = reduce(lambda x,y: x+y, [c[1] for c in all_chars if c[0] in string.letters], 0)
if n > 0:
	print "\n\n%d letters"%n
	
#Number of symbols (any non-letter and non-digit character, excluding white spaces)
n = reduce(lambda x,y: x+y, [c[1] for c in all_chars if c[0] not in string.letters and c[0] not in string.digits], 0)
if n > 0:
	print "\n\n%d symbols"%n
	
#Top three most common words (you may count "small words", such as "it" or "the")	
n = sorted(all_words, key = itemgetter(1), reverse = True)[:3]
print "\n\nTop three most common words: %r, %r, %r"%(n[0][0], n[1][0], n[2][0])

#Top three most common letters
n = sorted([c for c in all_chars if c[0] in string.letters], key = itemgetter(1), reverse = True)[:3]
if n:
	print "\n\nTop three most common letters: %r, %r, %r"%(n[0][0], n[1][0], n[2][0])


#Most common first word of a paragraph (paragraph being defined as a block of text with an empty line above it) (Optional bonus)	
n = sorted(first_words, key = itemgetter(1), reverse = True)[0]
print "\n\n%r is the most common first word of all paragraphs"%(n[0])


#Number of words only used once (Optional bonus)
n = [w[0] for w in all_words if w[1] == 1]
if n:
	print "\n\nWords only used once: %s"%', '.join(n)


#All letters not used in the document (Optional bonus)
n = set(list(string.letters.lower())).difference([c[0] for c in all_chars if c[0] in string.letters])
if n:
	print "\n\nLetters not used in the document: %s"%', '.join(n)

