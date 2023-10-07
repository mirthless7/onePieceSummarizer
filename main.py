from Summarizer_2 import summarize
from bryanhehe import arc_name

CATALOGUE = ["Romance Dawn", "Orange Town", "Syrup Village", "Baratie", "Arlong Park", "Logue Town","Reverse Mountain", "Whisky Peak", "Little Garden", "Drum Island", "Alabasta","Jaya", "Skypiea", "Long Ring Long Land", "Water 7", "Enies Lobby",
            "Post-Enies Lobby", "Thriller Bark","Sabaody Archipelago","Amazon Lily", "Impel Down","Marineford", "Post-War","Return to Sabaody",
            "Fish-Man Island","Punk Hazard","Dressrosa","Zou","Whole Cake Island", "Levely","Wano Country", "746"]

#https://dzone.com/articles/how-to-paraphrase-text-in-python-using-nlp-librari#:~:text=In%20Python%2C%20there%20are%20machine,are%20%E2%80%9CDeep%20learning%E2%80%9D%20models.

url='https://raw.githubusercontent.com/mirthless7/onePieceSummarizer/main/idkman.txt'



lowB=0
upB=1

print("-------------\nONE PIECE SUMMARIZER\n by Ronan Buck, Bryan Leyva, and Dmytro Moshkovskyi\n")


while True:
    try:
        lowB=int(input("What episode number to start from: "))
        if lowB<1 or lowB>1030:
            continue
        break
    except:
        print("That's not a valid episode number")
    
while True:
    try:
        upB=int(input("What episode number to end with: "))
        if upB<=lowB or upB<1 or upB>1031:
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

print("Loading the output, give it a minute...")
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

sumSize=0.01
if(upB-lowB<5):
    sumSize = 0.022
elif(upB-lowB<10):
    sumSize = 0.018
elif(upB-lowB<40):
    sumSize = 0.01
elif(upB-lowB<100):
    sumSize = 0.003
else:
    sumSize = 0.082

print(f'----------\n-- ONE PIECE SUMMARY\n-- ARCS: {lowArc} to {arc_name(upB)}\n-----------\n{summarize(output,sumSize)}\n------------\n')
            