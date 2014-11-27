string = "hello"
print string[0]

for y in range (len(position)):
    for x in range (len(position[y])):
        if position[y][x] == lookFore[0]:
            for char in (len(lookFore)):
                if y == 0 and x == 0:
                    p = 4,6,7
                elif y == 0 and x == (len(position[y])):
                    p = 3,5,6
                elif y == (len(position)) and x == 0:
                    p = 1,2,4
                elif y == (len(position)) and x == (len(position[y])):
                    p = 0,1,3,
                elif x == 0:
                    p = 1,2,4,6,7
                elif x == (len(position[y])):
                    p = 0,1,3,5,6
                elif y == 0:
                    p = 3,4,5,6,7
                elif y = (len(position)):
                    p = 0,1,2,3,4

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
