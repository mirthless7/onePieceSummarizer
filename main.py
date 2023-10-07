import pandas as pd
import numpy as npy
import scipy as spy
import pysrt
import requests
import os

CATALOGUE = {
    "East Blue": ["Romance Dawn", "Orange Town", "Syrup Village", "Baratie", "Arlong Park", "Logue Town", "Buggy's Crew Adventure Chronicles", "Warship Island"],
    "Arabasta": ["Reverse Mountain", "Whisky Peak", "Diary of Koby-Meppo", "Little Garden", "Drum Island", "Arabasta", "Post-Arabasta"],
    "Sky Island": ["Goat Island", "Ruluka Island", "Jaya", "Skypiea", "G-8"],
    "Water 7": ["Long Ring Long Land", "Ocean's Dream", "Foxy's Return", "Water 7", "Enies Lobby", "Boss Luffy Historical", "Post-Enies Lobby"],
    "Thrillr Bark": ["Ice Hunter", "Chopper Man Special", "Thriller Bark", "Spa Island"],
    "Summit War": ["Sabaody Archipelago", "Amazon Lily", "Straw Hat's Separation Serial", "Impel Down", "Little East Blue", "Marineford", "Post-War", "Toriko Crossover"],
    "Fish-Man Island": ["Return to Sabaody", "Fish-Man Island", "Toriko Crossover"],
    "Dressrosa":  ["Z's Ambition", "Punk Hazard", "Toriko & Dragon Ball Crossover", "Caesar Retrieval", "Dressrosa"],
    "Whole Cake Island": ["Silver Mine", "Zou", "Marine Rookie", "Whole Cake Island", "Levely"],
    "Wano Country": ["Wano Country", "Cidre Guild", "Anime 20th Anniversary special", "Uta's Past"],
    "Final": ["Egghead"]
}

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
        

piece={"saga1":["arc1","arc2","arc3","arc4","arc5"],
       "saga2":["arc1","arc2","arc3","arc4","arc5"],
       "saga3":["arc1","arc2","arc3","arc4","arc5"],
       "saga4":["arc1","arc2","arc3","arc4","arc5"],
       "saga5":["arc1","arc2","arc3","arc4","arc5"]}

print(piece['saga1'][2])







    