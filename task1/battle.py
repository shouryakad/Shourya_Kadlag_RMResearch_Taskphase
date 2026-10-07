import random
battle = [[0 for i in range(8)] for i in range(8)]


z = random.choice([True, False])#Aircraft
if(z):
    x = random.randint(0,7)
    y = random.randint(0,2)
    for i in range(y,y+6):
        battle[x][i] = 1
else:
    x = random.randint(0,2)
    y = random.randint(0,7)
    for i in range(x, x+6):
        battle[i][y] = 1

z = random.choice([True, False])#Destroyer
if(z):
    while True:
        x = random.randint(0,7)
        y = random.randint(0,4)
        check = 0
        for i in range(y, y+4):
            if(battle[x][i] == 1):
                check = 1
            else:
                continue
        if(check==0):
            for j in range(y, y+4):
                battle[x][j] = 1
            break          
        else:
            continue
else:
    while True:
            x = random.randint(0,4)
            y = random.randint(0,7)
            check = 0
            for i in range(y, y+4):
                if(battle[i][y] == 1):
                    check = 1
                else:
                    continue
            if(check==0):
                for j in range(y, y+4):
                    battle[j][y] = 1
                break    
            else:
                continue

z = random.choice([True, False])#Frigate
if(z):
    while True:
        x = random.randint(0,7)
        y = random.randint(0,6)
        check = 0
        for i in range(y, y+2):
            if(battle[x][i] == 1):
                check = 1
            else:
                continue
        if(check==0):
            for j in range(y, y+2):
                battle[x][j] = 1
            break          
        else:
            continue
else:
    while True:
            x = random.randint(0,6)
            y = random.randint(0,7)
            check = 0
            for i in range(y, y+2):
                if(battle[i][y] == 1):
                    check = 1
                else:
                    continue
            if(check==0):
                for j in range(y, y+2):
                    battle[j][y] = 1
                break    
            else:
                continue
for i in range(8):
    print(battle[i])
while True:
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    if(battle[x][y]==1):
        battle[x][y]=0
        print("Hit")
        continue
    else:
        print("Miss")
        
    check = 0
    for i in range(0,7):
        for j in range(0,7):
            if(battle[i][j]==1):
                check = 1
    if(check==0):
        print("Destroyed all")
        break

for i in range(8):
    print(battle[i])
