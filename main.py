import pandas as pd
import numpy as npy
import scipy as spy
import pysrt
import requests
import os

#https://dzone.com/articles/how-to-paraphrase-text-in-python-using-nlp-librari#:~:text=In%20Python%2C%20there%20are%20machine,are%20%E2%80%9CDeep%20learning%E2%80%9D%20models.

url='https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/idkman.txt'

#page = requests.get(url)
#print(page.text)

import pandas as pd
import numpy as npy
import scipy as spy
import pysrt
import requests
import os

#https://dzone.com/articles/how-to-paraphrase-text-in-python-using-nlp-librari#:~:text=In%20Python%2C%20there%20are%20machine,are%20%E2%80%9CDeep%20learning%E2%80%9D%20models.

url='https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/idkman.txt'

#page = requests.get(url)
#print(page.text)


vs={'lowBound_page': 0, 'upBound_page': 1,
    'lowBound_saga': 0, 'lowBound_arc': 0,
    'upBound_saga': 0, 'upBound_arc':0}


print("ONE PIECE SUMMARIZER\n by Ronan Buck, Brian Leyva, and Dmytro Moshkovskyi\n")


while True:
    try:
        lowBound_page=int(input("Which episode number to start from: "))
        break
    except:
        print("That's not a valid episode number")
    
while True:
    try:
        upBound_page=int(input("Which episode number to end with: "))
        break
    except:
        print("That's not a valid episode number")





    