for y in range (len(position)):
    for x in range (len(position[y])):
        for word in range (len(lookFor)):
            if position[y][x] == lookFor[word][0]:
                if y == 0:
                    print "top" + str(lookFor[word][0])
                elif y == len(position):
                    print "botom" + str(lookFor[word][0])
                if x == 0:
                    print "left side" + str(lookFor[word][0])
                elif x == len(position[y]):
                    print "right side" + str(lookFor[word][0])
                if y == 0 and x == 0:
                    print "top left" + str(lookFor[word][0])
                elif y == 0 and x == len(position[y]):
                    print "top right" + str(lookFor[word][0]) 
                elif y == len(position) and x == 0:
                    print "botom leaft" + str(lookFor[word][0])
                elif y == len(position) and x == len(position[y]):
                    print "botom right" + str(lookFor[word][0])    for char in (len(lookFor[word])):
                    
                    

def chek(y,x):
    
















def check(y,x,p):
    if p == 0:
        if position[y-1][x-1] == char:
            
    elif p == 1:
        if position[y-1][x] == char:
    elif p == 2:
        if position[y-1][x+1] == char:
    elif p == 3:
        if position[y][x-1] == char:
    elif p == 4:
        if position[y][x+1] == char:
    elif p == 5:
        if position[y+1][x-1] == char:
    elif p == 6:
        if position[y+1][x] == char:
    elif p == 7:
        if position[y+1][x+1] == char:
