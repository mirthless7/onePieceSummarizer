import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

import requests


#IT WORKS
url='https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/idkman.txt'

page = requests.get(url)
print(page.text)
