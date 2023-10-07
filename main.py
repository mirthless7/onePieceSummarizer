from Summarizer_2 import summarize
from bryanhehe2 import arc_name

def init(): # initializes the program for recursion
    print("-------------\nONE PIECE SUMMARIZER\n by Ronan Buck, Bryan Leyva, and Dmytro Moshkovskyi\n")
    CATALOGUE = ["Romance Dawn", "Orange Town", "Syrup Village", "Baratie", "Arlong Park", "Loguetown","Reverse Mountain", "Whisky Peak", 
    "Little Garden", "Drum Island", "Alabasta","Jaya", "Skypiea", "Long Ring Long Land", "Water 7", "Enies Lobby","Post-Enies Lobby", 
    "Thriller Bark","Sabaody Archipelago","Amazon Lily", "Impel Down","Marineford", "Post-War","Return to Sabaody","Fish-Man Island",
    "Punk Hazard","Dressrosa","Zou","Whole Cake Island", "Levely","Wano Country", "the end"]
    
    #low and upper bound episodes
    lowB=0
    upB=1

    while True:
        try:
            lowB=int(input("What episode number to start from: "))
            if lowB<1 or lowB>1030:
                continue
            break
        except:
            pass
        
    while True:
        try:
            upB=int(input("What episode number to end with: "))
            if upB<=lowB or upB<1 or upB>1031:
                continue
            break
        except:
            pass

    #the name of the corresponding arcs
    lowArc=arc_name(lowB) 
    upArc=arc_name(upB)

    #the upper bound is the next arc after the inputted arc
    for i in range(0,32):
        if (upArc==CATALOGUE[i]):
            upArc=CATALOGUE[i+1]
            break
    

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

    sumSize=0.01 #how much to summarize, 0 to 1
    if(upB-lowB<5):
        sumSize = 0.026
    elif(upB-lowB<10):
        sumSize = 0.021
    else:
        sumSize = 0.004

    try:
        print(f'----------\n-- ONE PIECE SUMMARY\n-- ARCS: {lowArc} to {arc_name(upB)}\n-----------\n{summarize(output,sumSize)}\n------------\n')
    except (ValueError):
        print("\nERROR: Too much One Piece!\nTry to resize the amount of episodes.\nNote: some arcs are bigger than others.\n")
        init()

init() #executes the program, for recursion if need be
out = input("")