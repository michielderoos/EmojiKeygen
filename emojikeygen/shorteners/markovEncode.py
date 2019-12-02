import markovify
import os
import requests
import random
import bisect
import operator
import baseconvert

"""Generates sentence-key and private key"""
# Download corpus and generate markov model if one doesn't exist yet
if not os.path.exists('markov_model.json'):
	corpus = requests.get('http://www.gutenberg.org/cache/epub/345/pg345.txt')
	text = corpus.text
	text_model = markovify.Text(text, well_formed = False)
	f = open('markov_model.json', 'w')
	f.write(text_model.to_json())
else:
	model = open('markov_model.json', 'r').read()
	text_model = markovify.Text.from_json(model)
prefix = []


BEGIN = '___BEGIN__'
END = '___END__'

def accumulate(iterable, func=operator.add):
	"""
	Cumulative calculations. (Summation, by default.)
	Via: https://docs.python.org/3/library/itertools.html#itertools.accumulate
	"""
	it = iter(iterable)
	total = next(it)
	yield total
	for element in it:
		total = func(total, element)
		yield total

def convert_variable_base(key, input_base, output_base):
	bc = baseconvert.BaseConverter(input_base=input_base, output_base=output_base)
	converted = list(bc(key))
	return converted

def move(chain, state, key, key_base):
	if state == tuple([ BEGIN ] * chain.state_size):
		choices = chain.begin_choices
		cumdist = chain.begin_cumdist
	else:
		choices, weights = zip(*chain.model[state].items())
		cumdist = list(accumulate(weights))

	if len(choices) > 1:
		if key:
			base_n_key = convert_variable_base(key, key_base, len(choices))
			return choices[base_n_key[0]], base_n_key, len(choices)
		else:
			r = random.random() * cumdist[-1]
			return choices[bisect.bisect(cumdist, r)], None, None
	else:
		return choices[0], key, key_base


def gen(key, chain, key_base = 16):
	state = (BEGIN,) * chain.state_size
	encoded_key_ints = []
	complete = False
	sentences = []
	sentence = []
	while True:
		next_word, key, key_base = move(chain, state, key, key_base)
		if key:
			encoded_key_ints.append(key.pop(0))
		else:
			complete = True

		if next_word == END and complete: 
			sentences += sentence
			return sentences
		if next_word == END and not complete:
			sentences += sentence
			sentence = []
			state = (BEGIN,) * chain.state_size
		else:
			sentence.append(next_word)
			state = tuple(state[1:]) + (next_word,)
	return sentences


def decodeStep(state, chain, ):
	choices, weights = zip(*chain.model[state].items())
	return choices

def decode(key, chain):
	newSentence = True
	for word in key:
		if newSentence:
			newSentence = False
			firstIndex = chain.begin_choices.index(word)
			state = (BEGIN, word)
			continue
		choices = decodeStep(state, chain)
		state = (state[1], word)
		print(word)
		if markovify.splitters.is_sentence_ender(word):
			print(word)
			print('ENDER!')
			newSentence = True
		if len(choices) <= 1:
			continue
		print(choices.index(word))

	#for word in key:
	#	state = (state[1], word)
	#	try:
	#		choices = decodeStep(state, chain)
	#		allChoices.append(allChoices)
	#	except:
	#		print('ALL CHOICES!')
	#		for line in allChoices:
	#			print(line)
word_to_encode = '130b3d5871767881bf93a0fdb5cc9e14130b3d5871767881bf93a0fdb5cc9e14'.upper()
phrase = gen(word_to_encode, text_model.chain)
print(phrase)
print('AAAZZZZZZZZZ-------------------------')
print(decode(phrase, text_model.chain))
print('AAAZZZZZZZZZ-------------------------')


#k = "DEADBEEF"
#o, bits = shorten_using_variable_base(k, 16, 9000)
#o, bits = shorten_using_variable_base(o, 9000, 14, bits)
#o, bits = shorten_using_variable_base(o, 14, 13, bits)
#o, bits = shorten_using_variable_base(o, 13, 12, bits)
#o, bits = shorten_using_variable_base(o, 12, 11, bits)
#o, bits = shorten_using_variable_base(o, 11, 10, bits)
#o, bits = shorten_using_variable_base(o, 11, 10, bits)
#o, bits = shorten_using_variable_base(o, 10, 11, bits)
#
#print('ZZZZZZZZZZZZZZZZZZZZZZZZZZ')

