import markovify
import requests
import hashlib
import os

from emojikeygen.shorteners import util
from emojikeygen import config

def generate(*argv):
	"""Generates sentence-key and private key"""
	# Download corpus and generate markov model if one doesn't exist yet
	if not os.path.exists('markov_model.json'):
		corpus = requests.get(config.MARKOV_CORPUS_URL)
		text = corpus.text
		text_model = markovify.Text(text, well_formed = False)
		f = open('markov_model.json', 'w')
		f.write(text_model.to_json())
	else:
		model = open('markov_model.json', 'r').read()
		text_model = markovify.Text.from_json(model)
	key = text_model.make_short_sentence(100)
	return key, util.generate_key(key)
