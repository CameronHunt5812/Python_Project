f = open("E:\\wordsearch.txt","r")
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
def search(side,position,y,x,):
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
    return direction

def searchDirection(direction,word,position,y,x):
    CheckAgen = True
    while CheckAgen == True:
        for char in range (word - 2):
            letter = lookFor[word][char]
            if direction ==  "upL":
                print "got here"
                if letter == position[y-char][x-char]:
                    CheckAgen = True
            elif direction == "up":
                if letter == position[y-char][x]:
                    CheckAgen = True
            elif direction == "upR":
                if letter == position[y-char][x+char]:
                    CheckAgen = True
            elif direction == "L":
                if letter == position[y][x-char]:
                    CheckAgen = True
            elif direction == "R":
                if letter == position[y][x+char]:
                    CheckAgen = True
            elif direction == "DL":
                if letter == position[y+char][x-char]:
                    CheckAgen = True
            elif direction == "D":
                if letter == position[y+char][x]:
                    CheckAgen = True
            elif direction == "DR":
                if letter == position[y+char][x+char]:
                    CheckAgen = True
            else:
                CheckAgen = False
            
for y in range (height):
    for x in range (width):
        for word in range (len(lookFor)):
            if position[y][x] == lookFor[word][0]:
                FirstLetter = lookFor[word][0]
                SecondLetter = lookFor[word][1]
                if y == 0 and x == 0:
                    print "top leaft" + str(FirstLetter)
                    side = "top leaft"
                elif y == 0 and x == width-1:
                    print "top right" + str(FirstLetter)
                    side = "top right"
                elif y == height-1 and x == 0:
                    print "botom leaft" + str(FirstLetter)
                    side = "botom leaft"
                elif y == height-1 and x == width-1:
                    print "botom right" + str(FirstLetter)
                    side = "botom leaft"
                elif y == 0:
                    print "top" + str(FirstLetter)
                    side ="top"
                elif y == height-1:
                    print "botom" + str(FirstLetter)
                    side = "botom"
                elif x == 0:
                    print "leaft side" + str(FirstLetter)
                    side = "leaft side"
                elif x == width-1:
                    print "right side" + str(FirstLetter)
                    side = "right side"
                else:
                    print "middle" + str(FirstLetter)
                direction = search(side,position,y,x)
                searchDirection(direction,word,position,y,x)