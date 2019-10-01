import json
import os
# import random
# from string import ascii_lowercase
import sys
from time import time

USER = 'specs'
LANG = 'Python 3'
NOTES = 'inefficient'
DATA = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data')

# def get_random_letters():
#     letters = LETTERS
#     word_length = random.randint(4, 10)
#     word = ''

#     while len(word) < word_length:
#         l = random.choice(ascii_lowercase)
#         if letters[l]['occurrence'] > 0:
#             word += l
#             letters[l]['occurrence'] -= 1

#     vowel_check = [l for l in 'aeiouy' if l in word]
#     if not vowel_check:
#         return get_random_letters()
#     else:
#         return word

# start timer
start = time() * 1000

# load data
with open(os.path.join(DATA, 'dictionary.txt')) as f:
    w = f.read()
WORDS = w.splitlines()

with open(os.path.join(DATA, 'letters.json'))as f:
    LETTERS = json.load(f)

# check input
if len(sys.argv) > 1:
    input_letters = sys.argv[1]
else:
    # input_letters = get_random_letters()
    input_letters = ''


def combine(word, prefix, items):
    for i, l in enumerate(word):
        items.append(prefix + l)
        temp = word[:i] + word[i + 1:]
        items = combine(temp, prefix + l, items)
    return items


combined_words = combine(input_letters, '', [])
solutions = sorted(
    [
        {
            'word': w,
            'score': sum(LETTERS.get(l, {}).get('score', 0) for l in w)
        }
        for w in combined_words
        if w in WORDS
    ],
    key=lambda k: k['score'],
    reverse=True
)
if solutions:
    winner = solutions[0]['word']
    score = solutions[0]['score']
else:
    winner = ''
    score = 0

duration = (time() * 1000) - start

print(f'{USER}, {LANG}, {winner}, {score}, {duration}, {NOTES}')
