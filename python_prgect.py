f = open("E:\\wordsearch.txt","r")
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


                    