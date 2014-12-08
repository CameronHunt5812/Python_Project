f = open("F:\\wordsearch.txt","r")
direction = 0
i = 1
CheckAgen = True
#Find the height, width and how many words to look for in the file.
height = int(f.readline())
width = int(f.readline()) 
numOfWords = int(f.readline())
#make a list of lists filled with 0 to fill with the letters from the word search
position = [[0 for x in range(width)]for y in range(height)]
#look at each position in the list and replace the 0 with the correct letter from the word search
for y in range (len(position)):
    #store line of charitors in a string to pull each sequentially
    tempLine = f.readline()
    for x in range (len(position[y])):
        #pull reach charitor and incert it into the list
        letter = tempLine[x]
        position[y][x] = letter
print position
#make a list of the words that you are looking for
lookFor = [f.readline() for w in range(numOfWords)]
print lookFor
found = [0 for f in range (len(lookFor))]
def search(side,placesToCheck,position,y,x,):
    pDi = -1
    for di in (placesToCheck):
        pDi = pDi + 1
        if di == True:
                if pDi == 0:
                    for char in range (len(lookFor[word]) - 1):
                        if y-char != 0 and x-char != 0:
                            letter = lookFor[word][char]
                            if letter == position[y-char][x-char]:
                                print position[y-char][x-char]
                                if char == len(lookFor[word]):
                                    
                        placesToCheck[pDi] = 0
                if pDi == 1:
                    if position[y-1][x] == SecondLetter:
                        for char in range (len(lookFor[word]) - 1):
                            if y-char != 0:
                                letter = lookFor[word][char]
                                if letter == position[y-char][x]:
                                    print position[y-char][x]
                                    placesToCheck[pDi] = 0
                if pDi == 2:
                    if position[y-1][x+1] == SecondLetter:
                        for char in range (len(lookFor[word]) - 1):
                            if y-char != 0 and x+char != width:
                                letter = lookFor[word][char]
                                if letter == position[y-char][x+char]:
                                    print position[y-char][x+char]
                                    placesToCheck[pDi] = 0
                if pDi == 3:
                    if position[y][x-1] == SecondLetter:
                        for char in range (len(lookFor[word]) - 1):
                            if x-char != 0:
                                letter = lookFor[word][char]
                                if letter == position[y][x-1]:
                                    print position[y][x-1]
                                    placesToCheck[pDi] = 0
                if pDi == 4:
                    if position[y][x-1] == SecondLetter:
                        for char in range (len(lookFor[word]) - 1):
                            if x-char != 0:
                                letter = lookFor[word][char]
                                if letter == position[y][x-char]:
                                    print position[y][x-char]
                                    placesToCheck[pDi] = 0
                if pDi == 5:
                    print side
                    print str(y) + " " + str(x)
                    for char in range (len(lookFor[word]) - 1):
                        if x+char != width:
                            if position[y][x+1] == SecondLetter:
                                letter = lookFor[word][char]
                                if letter == position[y][x-char]:
                                    print position[y][x-char]
                                    placesToCheck[pDi] = 0
                if pDi == 6:
                    if position[y+1][x-1] == SecondLetter:
                        for char in range (len(lookFor[word]) - 1):
                            if y+char != height and x-char != 0:
                                letter = lookFor[word][char]
                                if letter == position[y+char][x-char]:
                                    print position[y+char][x-char]
                                    placesToCheck[pDi] = 0
                if pDi == 7:
                    if position[y+1][x] == SecondLetter:
                        for char in range (len(lookFor[word]) - 1):
                            if y+char != height:
                                letter = lookFor[word][char]
                                if letter == position[y+char][x]:
                                    print position[y+char][x]
                                    placesToCheck[pDi] = 0
                if pDi == 8:
                    if position[y+1][x+1] == SecondLetter:
                        for char in range (len(lookFor[word]) - 1):
                            if y+char != height and x+char != width:
                                letter = lookFor[word][char]
                                if letter == position[y+char][x+char]:
                                    print position[y+char][x+char]
                                    placesToCheck[pDi] = 0
        
        
        
        
                    
"""    
        if position[y-1][x-1] == SecondLetter:
            direction = "upL"
        elif position[y-1][x] == SecondLetter:
            direction = "up"
        elif position[y-1][x+1] == SecondLetter:
            direction = "upR"
        elif position[y][x-1] == SecondLetter:
            direction = "L"
        elif position[y][x+1] == SecondLetter:
            direction = "R"
        elif position[y+1][x-1] == SecondLetter:
            direction = "DL"
        elif position[y+1][x] == SecondLetter:
            direction = "D"
        elif position[y+1][x+1] == SecondLetter:
            direction = "DR"













    global direction
    if side == "top leaft":
        if position[y][x+1] == SecondLetter:
            direction = "R"
        elif position[y+1][x] == SecondLetter:
            direction = "D"
        elif position[y+1][x+1] == SecondLetter:
            direction = "DR"
    elif side == "top right":
        if position[y][x-1] == SecondLetter:
            direction = "L"
        elif position[y+1][x-1] == SecondLetter:
            direction = "DL"
        elif position[y+1][x] == SecondLetter:
            direction = "D"
    elif side == "botom leaft":
        if position[y-1][x] == SecondLetter:
            direction = "up"
        elif position[y-1][x+1] == SecondLetter:
            direction = "upR"
        elif position[y][x+1] == SecondLetter:
            direction = "R"
    elif side == "top":
        if position[y][x-1] == SecondLetter:
            direction = "L"
        elif position[y][x+1] == SecondLetter:
            direction = "R"
        elif position[y+1][x-1] == SecondLetter:
            direction = "DL"
        elif position[y+1][x] == SecondLetter:
            direction = "D"
        elif position[y+1][x+1] == SecondLetter:
            direction = "DR"
    elif side == "botom":
        if position[y-1][x-1] == SecondLetter:
            direction = "upL"
        elif position[y-1][x] == SecondLetter:
            direction = "up"
        elif position[y-1][x+1] == SecondLetter:
            direction = "upR"
        elif position[y][x-1] == SecondLetter:
            direction = "L"
        elif position[y][x+1] == SecondLetter:
            direction = "R"
    elif side == "leaft":
        if position[y-1][x] == SecondLetter:
            direction = "up"
        elif position[y-1][x+1] == SecondLetter:
            direction = "upR"
        elif position[y][x+1] == SecondLetter:
            direction = "R"
        elif position[y+1][x] == SecondLetter:
            direction = "D"
        elif position[y+1][x+1] == SecondLetter:
            direction = "DR"
    elif side == "right":
        if position[y-1][x] == SecondLetter:
            direction = "up"
        elif position[y-1][x-1] == SecondLetter:
            direction = "upL"
        elif position[y][x-1] == SecondLetter:
            direction = "L"
        elif position[y+1][x-1] == SecondLetter:
            direction = "DL"
        elif position[y+1][x] == SecondLetter:
            direction = "D"
    elif side == "middle":
        if position[y-1][x-1] == SecondLetter:
            direction = "upL"
        elif position[y-1][x] == SecondLetter:
            direction = "up"
        elif position[y-1][x+1] == SecondLetter:
            direction = "upR"
        elif position[y][x-1] == SecondLetter:
            direction = "L"
        elif position[y][x+1] == SecondLetter:
            direction = "R"
        elif position[y+1][x-1] == SecondLetter:
            direction = "DL"
        elif position[y+1][x] == SecondLetter:
            direction = "D"
        elif position[y+1][x+1] == SecondLetter:
            direction = "DR"
    return direction
"""
def searchDirection(direction,word,position,y,x):
        for char in range (len(lookFor[word]) - 1):
                letter = lookFor[word][char]
                if direction ==  "upL" and y-char != 0 and x+char != 0:
                    if letter == position[y-char][x-char]:
                        print position[y-char][x-char]
                    else:
                        direction = 0
                if direction == "up":
                    if letter == position[y-char][x]:
                        print position[y-char][x]
                    else:
                        direction = 0
                elif direction == "upR" and y-char != -1 and x+char != width:
                    if letter == position[y-char][x+char]:
                        print position[y-char][x+char]
                    else:
                        direction = 0
                elif direction == "L" and x-char != 0:
                    if letter == position[y][x-char]:
                        print position[y][x-char]
                    else:
                        direction = 0
                elif direction == "R" and x+char != width:
                    if letter == position[y][x+char]:
                        print position[y][x+char]
                    else:
                        direction = 0
                elif direction == "DL" and y+char != -1 and x-char:
                    if letter == position[y+char][x-char]:
                        print position[y+char][x-char]
                    else:
                        direction = 0
                elif direction == "D" and y+char != height:
                    if letter == position[y+char][x]:
                        print position[y+char][x]
                    else:
                        direction = 0
                elif direction == "DR" and y+char != height and x+char != width:
                    if letter == position[y+char][x+char]:
                        print position[y+char][x+char]
                    else:
                        direction = 0
                else:
                    direction = 0


for y in range (height):
    for x in range (width):
        for word in range (len(lookFor)):
            if position[y][x] == lookFor[word][0]:
                FirstLetter = lookFor[word][0]
                SecondLetter = lookFor[word][1]
                placesToCheck = []
                if y == 0 and x == 0:
                    side = "top leaft"
                    placesToCheck = [0,0,0,0,1,0,1,1]
                elif y == 0 and x == width-1:
                    side = "top right"
                    placesToCheck = [0,0,0,1,0,1,1,0]
                elif y == height-1 and x == 0:
                    side = "botom leaft"
                    placesToCheck = [0,1,1,0,1,0,0,0]
                elif y == height-1 and x == width-1:
                    side = "botom right"
                    placesToCheck = [1,1,0,1,0,0,0,0]
                elif y == 0:
                    side ="top"
                    placesToCheck = [0,0,0,1,1,1,1,1]
                elif y == height-1:
                    side = "botom"
                    placesToCheck = [1,1,1,1,1,0,0,0]
                elif x == 0:
                    side = "leaft"
                    placesToCheck = [0,1,1,0,1,0,1,1,]
                elif x == width-1:
                    side = "right"
                    placesToCheck = [1,1,0,1,0,1,1,0]
                else:
                    side = "middle"
                    placesToCheck = [1,1,1,1,1,1,1,1]
                #print side + " x=" + str(x+1) + " y=" + str(y*(-1)-1)
                direction = search(side,placesToCheck,position,y,x)
                searchDirection(direction,word,position,y,x)
                direction = 0