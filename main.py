import pandas as pd
import numpy as npy
import scipy as spy
import pysrt
import requests
import os

CATALOGUE = ["Romance Dawn", "Orange Town", "Syrup Village", "Baratie", "Arlong Park", "Logue Town", "Buggy's Crew Adventure Chronicles", "Warship Island", 
            "Reverse Mountain", "Whisky Peak", "Diary of Koby-Meppo", "Little Garden", "Drum Island", "Alabasta", "Post-Arabasta", 
            "Goat Island", "Ruluka Island", "Jaya", "Skypiea", "G-8","Long Ring Long Land", "Ocean's Dream", "Foxy's Return", "Water 7", "Enies Lobby",
            "Boss Luffy Historical", "Post-Enies Lobby", "Ice Hunter", "Chopper Man Special", "Thriller Bark", "Spa Island", "Sabaody Archipelago",
            "Amazon Lily", "Straw Hat's Separation Serial", "Impel Down", "Little East Blue", "Marineford", "Post-War", "Toriko Crossover", "Return to Sabaody",
            "Fish-Man Island", "Toriko Crossover", "Z's Ambition", "Punk Hazard", "Toriko & Dragon Ball Crossover", "Caesar Retrieval", "Dressrosa", "Silver Mine", 
            "Zou", "Marine Rookie", "Whole Cake Island", "Levely","Wano Country", "Cidre Guild", "Anime 20th Anniversary special", "Uta's Past", "Egghead"]


#https://dzone.com/articles/how-to-paraphrase-text-in-python-using-nlp-librari#:~:text=In%20Python%2C%20there%20are%20machine,are%20%E2%80%9CDeep%20learning%E2%80%9D%20models.

url='https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/one-piece-the-book.txt'

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
        








    