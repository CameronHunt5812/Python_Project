f = open("E:\\wordsearch.txt","r")
direction = 0
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
for y in range (len(position)):
    for x in range (len(position[y])):
        for word in range (len(lookFor)):
            if position[y][x] == lookFor[word][0]:
                if y == 0 and x == 0:
                    print "top left" + str(lookFor[word][0])
                    if position[y][x+1] == lookFor[word][1]:
                        direction = 5
                    elif position[y+1][x] == lookFor[word][1]:
                        direction = 7
                    elif position[y+1][x+1] == lookFor[word][1]:
                        direction = 8
                    else:
                        print "not here"
                elif y == 0 and x == len(position[y]):
                    print "top right" + str(lookFor[word][0])
                    if position[y][x-1] == lookFor[word][1]:
                        direction = 4
                    elif position[y+1][x-1] == lookFor[word][1]:
                        direction = 6
                    elif position[y+1][x] == lookFor[word][1]:
                        direction = 7
                    else:
                        print "not here"
                elif y == len(position) and x == 0:
                    print "botom leaft" + str(lookFor[word][0])
                    if position[y-1][x] == lookFor[word][1]:
                        direction = 2
                    elif position[y-1][x+1] == lookFor[word][1]:
                        direction = 3
                    elif position[y][x+1] == lookFor[word][1]:
                        direction = 5
                    else:
                        print "not here"
                elif y == len(position) and x == len(position[y]):
                    print "botom right" + str(lookFor[word][0])
                    if position[y-1][x] == lookFor[word][1]:
                        direction = 1
                    elif position[y-1][x-1] == lookFor[word][1]:
                        direction = 2
                    elif position[y][x-1] == lookFor[word][1]:
                        direction = 4
                    else:
                        print "not here"  
                elif y == 0 and x+1 <= len(position[y]):
                    print "top" + str(lookFor[word][0])
                    if position[y][x-1] == lookFor[word][1]:
                        direction = 4
                    elif position[y][x+1] == lookFor[word][1]:
                        direction = 5
                    elif position[y+1][x-1] == lookFor[word][1]:
                        direction = 6
                    elif position[y+1][x] == lookFor[word][1]:
                        direction = 7
                    elif position[y+1][x+1] == lookFor[word][1]:
                        direction = 8
                elif y == len(position):
                    print "botom" + str(lookFor[word][0])
                    if position[y-1][x-1] == lookFor[word][1]:
                        direction = 1
                    elif position[y-1][x] == lookFor[word][1]:
                        direction = 2
                    elif position[y-1][x+1] == lookFor[word][1]:
                        direction = 3
                    elif position[y][x-1] == lookFor[word][1]:
                        direction = 4
                    elif position[y][x+1] == lookFor[word][1]:
                        direction = 5
                    else:
                        print "not here"
                elif x == 0:
                    print "left side" + str(lookFor[word][0])
                    if position[y-1][x] == lookFor[word][1]:
                        direction = 2
                    elif position[y-1][x+1] == lookFor[word][1]:
                        direction = 3
                    elif position[y][x+1] == lookFor[word][1]:
                        direction = 5
                    elif position[y+1][x] == lookFor[word][1]:
                        direction = 6
                    elif position[y+1][x+1] == lookFor[word][1]:
                        direction = 7
                    else:
                        print "not here"
                elif x == len(position[y]):
                    print "right side" + str(lookFor[word][0])
                    if position[y-1][x] == lookFor[word][1]:
                        direction = 1
                    elif position[y-1][x-1] == lookFor[word][1]:
                        direction = 2
                    elif position[y][x-1] == lookFor[word][1]:
                        direction = 4
                    elif position[y+1][x-1] == lookFor[word][1]:
                        direction = 6
                    elif position[y+1][x] == lookFor[word][1]:
                        direction = 7
                    else:
                        print "not here"
                #print "it got here"
                #for char in range (len(lookFor[word])):