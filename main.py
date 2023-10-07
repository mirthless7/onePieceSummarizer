import pandas as pd
import numpy as npy
import scipy as spy
import pysrt
import requests
import os
import Summarizer_2.py as summa
import spacy
import requests
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

CATALOGUE = ["Romance Dawn", "Orange Town", "Syrup Village", "Baratie", "Arlong Park", "Logue Town", "Buggy's Crew Adventure Chronicles", "Warship Island", 
            "Reverse Mountain", "Whisky Peak", "Little Garden", "Drum Island", "Alabasta","Jaya", "Skypiea", "Long Ring Long Land", "Water 7", "Enies Lobby",
            "Post-Enies Lobby", "Thriller Bark","Sabaody Archipelago","Amazon Lily", "Impel Down","Marineford", "Post-War","Return to Sabaody",
            "Fish-Man Island","Punk Hazard","Dressrosa","Zou","Whole Cake Island", "Levely","Wano Country"]


#https://dzone.com/articles/how-to-paraphrase-text-in-python-using-nlp-librari#:~:text=In%20Python%2C%20there%20are%20machine,are%20%E2%80%9CDeep%20learning%E2%80%9D%20models.

url='https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/idkman.txt'

#page = requests.get(url)
#print(page.text)

lowB=0;
upB=1;

print("ONE PIECE SUMMARIZER\n by Ronan Buck, Bryan Leyva, and Dmytro Moshkovskyi\n")


while True:
    try:
        lowB=int(input("Which episode number to start from: "))
        break
    except:
        print("That's not a valid episode number")
    
while True:
    try:
        upB=int(input("Which episode number to end with: "))
        break
    except:
        print("That's not a valid episode number")
        
tempLowArc='Orange Town'
tempUpArc= 'Arlong Park'

output=' '
with open('one-piece-the-book.txt', 'r', encoding="utf-8") as book:
    add = False
    for line in book:
        if add == True: 
            if tempLowArc in line[0:20]:
                continue
            output = output + line + '\n'

        if tempLowArc in line[0:20]:
            add = True 
        elif tempUpArc in line[0:20]:
            break

print(output)
            
        

            

#print(output)

def twice(ep_number):
    if(ep_number>0 and ep_number<4):
        return "Romance Dawn"
    elif (ep_number>3 and ep_number<9):
        return "Orange Town"
    elif (ep_number>8 and ep_number<19):
        return "Syrup Village"
    elif (ep_number>3 and ep_number<9):
        return "Baratie"
    elif (ep_number>8 and ep_number<19):
        return "Arlong Park"
    elif (ep_number>3 and ep_number<9):
        return "Loguetown"
    elif (ep_number>3 and ep_number<9):
        return "Reverse Mountain"
    elif (ep_number>8 and ep_number<19):
        return "Whisky Peak"
    elif (ep_number>8 and ep_number<19):
        return "Little Garden"
    elif (ep_number>3 and ep_number<9):
        return "Drum Island"
    elif (ep_number>8 and ep_number<19):
        return "Alabasta"
    elif (ep_number>3 and ep_number<9):
        return "Jaya"
    elif (ep_number>8 and ep_number<19):
        return "Skypiea"
    elif (ep_number>3 and ep_number<9):
        return "Long Ring Long Land"
    elif (ep_number>8 and ep_number<19):
        return "Water 7"
    elif (ep_number>3 and ep_number<9):
        return "Enies Lobby"
    elif (ep_number>8 and ep_number<19):
        return "Post-Enies Lobby"
    elif (ep_number>8 and ep_number<19):
        return "Thriller Bark"
    elif (ep_number>8 and ep_number<19):
        return "Sabaody Archipelago"
    elif (ep_number>8 and ep_number<19):
        return "Amazon Lily"
    elif (ep_number>8 and ep_number<19):
        return "Impel Down"
    elif (ep_number>8 and ep_number<19):
        return "Marineford"
    elif (ep_number>8 and ep_number<19):
        return "Post-War"
    elif (ep_number>8 and ep_number<19):
        return "Return to Sabaody"
    elif (ep_number>8 and ep_number<19):
        return "Fishman Island"
    elif (ep_number>8 and ep_number<19):
        return "Punk Hazard"
    elif (ep_number>8 and ep_number<19):
        return "Dressrosa"
    elif (ep_number>8 and ep_number<19):
        return "Zou"
    elif (ep_number>8 and ep_number<19):
        return "Whole Cake Island"
    elif (ep_number>8 and ep_number<19):
        return "Levely"
    elif (ep_number>8 and ep_number<19):
        return "Wano Country"
    
    


    
    






    