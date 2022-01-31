import time    

print("*"*100)
print("CONNECT 4 Pog".center(100))
print("Instructions::".center(100))
print("Try to build a row of four checkers while keeping your opponent from doing the same".center(100))
print("*"*100)

grid1 = [0,0,0,0] # bottom row
grid2 = [0,0,0,0]
grid3 = [0,0,0,0]
grid4 = [0,0,0,0]

print ("",grid4,"\n",grid3,"\n",grid2,"\n",grid1)


grids = [grid1,grid2,grid3,grid4]

check = []

user = 1

class fullSlot_error (Exception):
    pass
def hasWon_def():
    print ("player "+str(user)+" has won")
    time.sleep(3)

def grid_def():
    print ("",grid4,"\n",grid3,"\n",grid2,"\n",grid1)

def user_def():
    global user
    if user < 2:
        user = 2
    else:
        user = 1
    return user

def slotFull_def():
   while True:
        try:
            if grid4[userInput -1] != 0:
                raise fullSlot_error
            else:
                break
        except fullSlot_error:
            print ("slot is full try again")
            confirm_def()

def confirm_def():
    looop= True
    while looop== True:
        try:
            global userInput
            userInput = int(input("\nenter column : player "+str(user)+"(1,4)\n"))
            if userInput < 5 and 0 < userInput:   
                looop = False
            else:
                print ("invalid int")
        except ValueError:
            print ("invalid input")

def placement_def():
    counter = 0
    for i in range (0,4):
        slotFull_def()
        if (grids[i][userInput -1] == 0):
            grids [i][userInput - 1] = int(user)
            grid_def()
            break


def check_def():
    global loop
    global check
    for i in range(0,4):
        for a in range(0,4):
            check.append(grids[i][a])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            hasWon_def()
            loop = False
            return loop
            break
        else:
            check = []
    for i in range(0,4):
        for a in range(0,4):
            check.append(grids[a][i])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            hasWon_def()
            loop = False
            return loop
            break
        else:
            check = []

def checkEmpty_def():
    global check
    for i in range (0,4):
        for a in range (0,4):
            check.append(grids[i][a])
    if 0 not in check:
        print ("full")

def checks_def():
    check_def()
    checkEmpty_def()
    diagcheck_def()

def diagcheck_def():
    global loop
    global check
    check = []
    diag = 0
    for i in range (0,4):
        check.append (grids[diag][diag])
        diag = diag +1
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            hasWon_def()
            loop = False
            return loop
            break
    check = []
    diag = 3
    diag2 = 0
    for i in range (0,4):
        check.append (grids[diag][diag2])
        if (check == [1,1,1,1] or check == [2,2,2,2]):
            hasWon_def()
            loop = False
            return loop
            break


loop = True

while loop == True:
    check_def()
    confirm_def()
    placement_def()
    checks_def()
    if loop == False:
        break
    user_def()
