import pandas as pd
import os
import spacy
from Summarizer_2 import summarize
from bryanhehe import arc_name
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

nlp = spacy.load("en_core_web_sm")
nlp.Defaults.stop_words.add('\n')

CATALOGUE = ["Romance Dawn", "Orange Town", "Syrup Village", "Baratie", "Arlong Park", "Logue Town","Reverse Mountain", "Whisky Peak", "Little Garden", "Drum Island", "Alabasta","Jaya", "Skypiea", "Long Ring Long Land", "Water 7", "Enies Lobby",
            "Post-Enies Lobby", "Thriller Bark","Sabaody Archipelago","Amazon Lily", "Impel Down","Marineford", "Post-War","Return to Sabaody",
            "Fish-Man Island","Punk Hazard","Dressrosa","Zou","Whole Cake Island", "Levely","Wano Country", "746"]

#https://dzone.com/articles/how-to-paraphrase-text-in-python-using-nlp-librari#:~:text=In%20Python%2C%20there%20are%20machine,are%20%E2%80%9CDeep%20learning%E2%80%9D%20models.

url='https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/idkman.txt'



lowB=0
upB=1

print("ONE PIECE SUMMARIZER\n by Ronan Buck, Bryan Leyva, and Dmytro Moshkovskyi\n")


while True:
    try:
        lowB=abs(int(input("Which episode number to start from: ")))
        break
    except:
        print("That's not a valid episode number")
    
while True:
    try:
        upB=abs(int(input("Which episode number to end with: ")))
        if upB<=lowB:
            continue
        break
    except:
        print("That's not a valid episode number")
        

#   LOOP TO ITERATE THROUGH TEXT

lowArc=arc_name(lowB) #PLACEHOLDER
upArc=arc_name(upB)

for i in range(0,32):
    if (upArc==CATALOGUE[i]):
        upArc=CATALOGUE[i+1]
        break

if (lowArc=='Not Found' or upArc=='Not Found'):
    print("Episode not found")
    exit()

output=' '
with open('one-piece-the-book.txt', 'r', encoding="utf-8") as book:
    add = False
    for line in book:
        if add == True: 
            if lowArc in line[0:20]:
                continue
            output = output + line 

        if lowArc in line[0:20]:
            if (add==True):
                continue
            add = True 

        elif upArc in line[0:20]:
            break


print(f'----------\nONE PIECE SUMMARY:\n\n-- ARCS: {lowArc} to {arc_name(upB)}\n-----------\n{summarize(output,0.01)}\n\n')
            