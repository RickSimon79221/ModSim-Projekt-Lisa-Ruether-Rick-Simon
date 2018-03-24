import numpy as np

def empty_sudoku():              
    sudoku = np.zeros((10,9,9))
    for i in range(10):
        sudoku[i,:,:] = i
    
    return(sudoku)
    
def clues(sudoku, zahl, x, y):
    x = x - 1                        # Setzt X-Koordinate für Computer um
    y = y - 1                        # Setzt Y-Koordinate für Computer um
    sudoku[0,y,x] = zahl             # Setzt zahl auf oberste Ebene in gewuenschtes Feld
    sudoku[1:,y,x] = 0               # Setzt das Feld auf allen darunter liegenden Ebenen auf 0
    sudoku[zahl,:,x] = 0             # Setzt Spalte auf Ebene zahl auf 0
    sudoku[zahl,y,:] = 0             # Setzt Zeile auf Ebene zahl auf 0
    
    if x in [0,1,2]:                 # lokalisiert 3x3 Kaestchen in dem sich das Feld befindet und setzt es auf Ebene zahl gleich 0
        if y in [0,1,2]:             
            sudoku[zahl,0:3,0:3] = 0 
        
        elif y in [3,4,5]:
            sudoku[zahl,3:6,0:3] = 0
        
        elif y in [6,7,8]:
            sudoku[zahl,6:9,0:3] = 0
        
    elif x in [3,4,5]:
        if y in [0,1,2]:
            sudoku[zahl,0:3,3:6] = 0
        
        elif y in [3,4,5]:
            sudoku[zahl,3:6,3:6] = 0
        
        elif y in [6,7,8]:
            sudoku[zahl,6:9,3:6] = 0
    
    elif x in [6,7,8]:
        if y in [0,1,2]:
            sudoku[zahl,0:3,6:9] = 0
        
        elif y in [3,4,5]:
            sudoku[zahl,3:6,6:9] = 0
        
        elif y in [6,7,8]:
            sudoku[zahl,6:9,6:9] = 0
    
    return(sudoku)


def mkAnswer(sudoku):
    for Y in range(9):
        for X in range(9):
            if sudoku[Y,X] == 0:
                sudoku = setNumber(X,Y,sudoku)

            
    return(sudoku)


def setNumber(X,Y,sudoku,trys=[]):
    
    while True:
        sudoku[Y,X] = 0
        possibilitys = mklst(X,Y,sudoku)
        for t in trys:
            if t in possibilitys:
                possibilitys.remove(t)
        P = len(possibilitys)

        if P > 0:
            sudoku[Y,X] = np.random.choice(possibilitys,1)
            break

        else:
            break

    return(sudoku)


def mklst(X,Y,sudoku):
    lst = [1,2,3,4,5,6,7,8,9]
    zeile = sudoku[Y,0:9] 
    spalte = sudoku[0:9,X]
    
    if Y in [0,1,2]:
        if X in [0,1,2]:
            square = sudoku[0:3,0:3]
            
        elif X in [3,4,5]:
            square = sudoku[0:3,3:6]
            
        elif X in [6,7,8]:
            square = sudoku[0:3,6:9]
        
    elif Y in [3,4,5]:
        if X in [0,1,2]:
            square = sudoku[3:6,0:3]
        
        elif X in [3,4,5]:
            square = sudoku[3:6,3:6]
            
        elif X in [6,7,8]:
            square = sudoku[3:6,6:9]
        
    elif Y in [6,7,8]:
        if X in [0,1,2]:
            square = sudoku[6:9,0:3]
            
        elif X in [3,4,5]:
            square = sudoku[6:9,3:6]
            
        elif X in [6,7,8]:
            square = sudoku[6:9,6:9]
    
    rechteck = np.reshape(square,9)
    
    for s in spalte:
        if s in lst:
            lst.remove(s)
    
    for z in zeile:
        if z in lst:
            lst.remove(z)
            
    for r in rechteck:
        if r in lst:
            lst.remove(r)
            
    return(lst)

def check_sudoku(sudoku):
    s = np.reshape(sudoku[:,:],81)
    x = 0
    for i in range(81):
        if s[i] == 0:
            x = x + 1
    
    if x > 0:
        return(False)
    else:
        return(True)


def check_list(reihe):
    x = 0
    for i in range(81):
        if reihe[i] != 0:
            x = x + 1
    
    return(x)
    

def SudokuGen():
    solved = False
    while solved != True:
        sudoku = np.zeros((9,9))
        sudoku = mkAnswer(sudoku)
        solved = check_sudoku(sudoku)
        
    return(sudoku)

###### Verschiedene Generator Arten #######################

def take_sudoku(N):
    pos = [0,1,2,3,4,5,6,7,8]
    quest = SudokuGen()
    x = check_list(quest.reshape(81))
    while x != N:
        i = np.random.choice(pos)
        j = np.random.choice(pos)
        quest[i,j] = 0
        x = check_list(quest.reshape(81))
    

    sudoku = empty_sudoku()
    for n in range(1,10):
        for m in range(1,10):
            if quest[n-1,m-1] != 0:
                sudoku = clues(sudoku,int(quest[n-1,m-1]),m,n)
    
    return(sudoku)
    

def tot_rand_sudoku(N):
    pos = [1,2,3,4,5,6,7,8,9]
    sudoku = empty_sudoku()
    c = 0
    while c < N:
        x = np.random.choice(pos) - 1
        y = np.random.choice(pos) - 1
        z = np.random.choice(pos)
        if sudoku[0,y,x] == 0:
            sudoku = clues(sudoku,z,x,y)
            c = c + 1 
            
    return(sudoku)
    
def part_rand_sudoku(N):
    korr = [0,1,2,3,4,5,6,7,8]
    pos = [1,2,3,4,5,6,7,8,9]

    sudoku = empty_sudoku()
    c = 0
    regel = 0
    while c < N:
        x = np.random.choice(korr)
        y = np.random.choice(korr)
        z = np.random.choice(pos)
            
        if sudoku[0,y,x] == 0:
            sudoku = clues(sudoku,z,x + 1,y + 1)
            c = c + 1
            if regel < 8:
                pos.remove(z)
                regel = regel + 1
            else:
                pos = [1,2,3,4,5,6,7,8,9]
                
    return(sudoku)
    
def rules_rand_sudoku(N):

    korr = [0,1,2,3,4,5,6,7,8]
    pos = [1,2,3,4,5,6,7,8,9]

    sudoku = empty_sudoku()
    c = 0
    regel = 0
    while c < N:
        x = np.random.choice(korr)
        y = np.random.choice(korr)
        z = np.random.choice(pos)
            
        pruef = mklst(x,y,sudoku)
        if sudoku[0,y,x] == 0 and z in pruef:
            sudoku = clues(sudoku,z,x + 1,y + 1)
            c = c + 1
            if regel < 8:
                pos.remove(z)
                regel = regel + 1
            else:
                pos = [1,2,3,4,5,6,7,8,9]
                    
        elif sudoku[0,y,x] == 0 and pruef == []:
                sudoku = empty_sudoku()
                c = 0
                
    return(sudoku)
                
    
    

    

    
    
    
    
