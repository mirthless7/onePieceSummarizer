import pandas as pd
import os
import spacy
from Summarizer_2 import summarize
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

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
        

#   LOOP TO ITERATE THROUGH TEXT

tempLowArc='Orange Town' #PLACEHOLDER
tempUpArc= 'Arlong Park'

output=' '
with open('one-piece-the-book.txt', 'r', encoding="utf-8") as book:
    add = False
    for line in book:
        if add == True: 
            if (tempLowArc or '\n') in line[0:20]:
                continue
            output = output + line + '\n'

        if tempLowArc in line[0:20]:
            add = True 
        elif tempUpArc in line[0:20]:
            break

print(summarize(output,0.01))
            
        

            

#print(output)

def arc_name(ep_number):
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
    
    


    
    






    