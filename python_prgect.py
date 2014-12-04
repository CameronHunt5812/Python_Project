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
def serch(edge,position,direction):
    


for y in range (height):
    for x in range (width):
        for word in range (len(lookFor)):
            if position[y][x] == lookFor[word][0]:
                FirstLetter = lookFor[word][0]
                SecondLetter = lookFor[word][1]
                if y == 0 and x == 0:
                    print "top left" + str(FirstLetter)
                    if position[y][x+1] == SecondLetter:
                        direction = 5
                    elif position[y+1][x] == SecondLetter:
                        direction = 7
                    elif position[y+1][x+1] == SecondLetter:
                        direction = 8
                elif y == 0 and x == width-1:
                    print "top right" + str(FirstLetter)
                    if position[y][x-1] == SecondLetter:
                        direction = 4
                    elif position[y+1][x-1] == SecondLetter:
                        direction = 6
                    elif position[y+1][x] == SecondLetter:
                        direction = 7
                elif y == height-1 and x == 0:
                    print "botom leaft" + str(FirstLetter)
                    if position[y-1][x] == SecondLetter:
                        direction = 2
                    elif position[y-1][x+1] == SecondLetter:
                        direction = 3
                    elif position[y][x+1] == SecondLetter:
                        direction = 5
                elif y == height-1 and x == width-1:
                    print "botom right" + str(FirstLetter)
                    if position[y-1][x] == SecondLetter:
                        direction = 1
                    elif position[y-1][x-1] == SecondLetter:
                        direction = 2
                    elif position[y][x-1] == SecondLetter:
                        direction = 4
                elif y == 0:
                    print "top" + str(FirstLetter)
                    if position[y][x-1] == SecondLetter:
                        direction = 4
                    elif position[y][x+1] == SecondLetter:
                        direction = 5
                    elif position[y+1][x-1] == SecondLetter:
                        direction = 6
                    elif position[y+1][x] == SecondLetter:
                        direction = 7
                    elif position[y+1][x+1] == SecondLetter:
                        direction = 8
                elif y == height-1:
                    print "botom" + str(FirstLetter)
                    if position[y-1][x-1] == SecondLetter:
                        direction = 1
                    elif position[y-1][x] == SecondLetter:
                        direction = 2
                    elif position[y-1][x+1] == SecondLetter:
                        direction = 3
                    elif position[y][x-1] == SecondLetter:
                        direction = 4
                    elif position[y][x+1] == SecondLetter:
                        direction = 5
                elif x == 0:
                    print "left side" + str(FirstLetter)
                    if position[y-1][x] == SecondLetter:
                        direction = 2
                    elif position[y-1][x+1] == SecondLetter:
                        direction = 3
                    elif position[y][x+1] == SecondLetter:
                        direction = 5
                    elif position[y+1][x] == SecondLetter:
                        direction = 6
                    elif position[y+1][x+1] == SecondLetter:
                        direction = 7
                elif x == width-1:
                    print "right side" + str(FirstLetter)
                    if position[y-1][x] == SecondLetter:
                        direction = 1
                    elif position[y-1][x-1] == SecondLetter:
                        direction = 2
                    elif position[y][x-1] == SecondLetter:
                        direction = 4
                    elif position[y+1][x-1] == SecondLetter:
                        direction = 6
                    elif position[y+1][x] == SecondLetter:
                        direction = 7