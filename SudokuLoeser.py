
import numpy as np       # importiert Numpy um Matritzen nutzen zu koennen 

'''
Die folgende Funktion empty sudoku erstellt ein leeres Sudoku Feld.
Dabei erstellt die Funktion eine drei-dimensionale Matrix. Die erste Ebene
ist dabei das richtige Sudoku. Auf dieser Ebene entspricht 0 einem leeren Feld.
Die Ebenen dahinter behandeln welche Zahlen von 1-9 in einem bestimmten 
Sudoku-Feld auftreten koennen. Sind fuer ein leeres Feld im richtigen Sudoku alle
darunter liegenden Ebenen ungleich 0, so koennen in dem leeren Feld alle Zahlen
von 1-9 stehen. Ist dagegen nur die Ebene mit der 4 ungleich 0, so kann im 
leeren Feld nur die 4 stehen.
'''

def empty_sudoku():              
    sudoku = np.zeros((10,9,9))
    for i in range(10):
        sudoku[i,:,:] = i
    
    return(sudoku)

'''
Die Folgende Funktion clues nimmt ein Sudoku und setzt eine Zahl ein, sowie
beeinflusst die darunter liegenden Ebenen. Die Argumente die clues nimmt sind
    
    sudoku = die 3-D Matrix des Sudokus
    zahl = Die Zahl die im Sudoku-Feld hinzugefügt werden soll
    x = Die X-Koordinate des Feldes in welches die Zahl eingefügt wird von 1-9
    y = Die Y-Koordinate des Feldes in welches die Zahl eingefügt wird von 1-9
    
    
Die Funktion setzt nicht nur die Zahl in das leere Feld ein, sondern
manipuliert auch die restlichen Ebenen der 3-D Matrix um zu zeigen, welche 
Zahlen noch in welche Felder koennen.

Beispiel
    Setzt clues in das allererste Feld die Zahl 4, so setzt es nicht nur die 
    4 in die oberste Ebene, sondern auf allen darunterliegenden Ebenen wird 
    das erste Feld 0, da es ja nun schon besetzt ist.
    Weiterhin wird auf der fuenften Ebene (die Ebene für die Zahl 4) werden
    die erste Zeile und die erste Spalte Null, da in jeder Zeile und Spalte
    jede Zahl nur einmal vorkommen darf. Ebenso wird das 3x3 Feld in dem sich 
    das Feld findet auf der fuenften Ebene Null, da auch in diesen Feldern 
    jede Zahl nur einmal vorkommen darf.

'''

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
    
'''
Die folgende Funktion prueft fuer ein Liste mit 9 Eintraegen wie viele davon
ungleich Null sind und gibt diese aus. 
'''

def check_list(reihe):
    x = 0
    for i in range(9):
        if reihe[i] != 0:
            x = x + 1
    
    return(x)

'''
Die folgende Funktion prueft fuer ein 3x3 Kaestchen wie viele Eintraege davon
ungleich Null sind und gibt diese aus. 
'''

def check_square(square):
    s = np.reshape(square,9)
    x = check_list(s)
    return(x)

'''
Die folgende Funktion prueft fuer ein Sudoku ob alle Faelder ungleich 0 
sind oder nicht. Gibt True aus falls alle ungleich 0 sind, andernfalls gibt
die Funktion False aus.
'''

def check_sudoku(sudoku):
    s = np.reshape(sudoku[0,:,:],81)
    x = 0
    for i in range(81):
        if s[i] == 0:
            x = x + 1
    
    if x > 0:
        return(False)
    else:
        return(True)
        

'''
Diese Funktion ueberprueft, falls in einer Zeile oder Spalte nur 2 bzw. 3
Eintraege sind, ob diese auch in demselben 3x3 Kaestchen sind.
Gibt eine Liste mit einzig und allein dem Element False zurueck, falls sie nicht in einem Kästchen sind.
Gibt eine Liste mit True und der Nummer des Kaestchens zurueck.
Beispiel:
    Hat Spalte 4 auf Ebene 7 nur zwei Eintraege und ergibt check_double = [True,1],
    so sind alle Eintraege auf Spalte 4 auf Ebene 7 in dem mittleren Kaestchen.

Die Wichtigkeit dieser Funktion wird spaeter weiter erlautert.
'''
def check_double(line, number):
    if number == 2:            # hat die Zeile oder Spalte 2 Elemente
        inds = np.nonzero(line) # finde die Indizes der Elemente die nicht 0 sind
        if inds[0][0] in [0,1,2] and inds[0][1] in [0,1,2]: # ueberprueft o sie im selben Kaestchen sind 
            return([True,0])
        
        elif inds[0][0] in [3,4,5] and inds[0][1] in [3,4,5]:
            return([True,1])
        
        elif inds[0][0] in [6,7,8] and inds[0][1] in [6,7,8]:
            return([True,2])
        
        else:
            return([False]) 
        
    elif number == 3:           # hat die Zeile oder Spalte 3 Elemente
        inds = np.nonzero(line) # finde die Indizes der Elemente die nicht 0 sind
        if inds[0][0] in [0,1,2] and inds[0][1] in [0,1,2] and inds[0][2] in [0,1,2]: # ueberprueft o sie im selben Kaestchen sind
            return([True,0]) 
         
        elif inds[0][0] in [3,4,5] and inds[0][1] in [3,4,5] and inds[0][2] in [3,4,5]:
            return([True,1])
        
        elif inds[0][0] in [6,7,8] and inds[0][1] in [6,7,8] and inds[0][2] in [6,7,8]:
            return([True,2])
        
        else:
            return([False])
    
def SudokuSolve(sudoku):

    run = 0     # Bestimmt, in dem wievielten durchlauf der Schleife sich das Pogramm befindet.
                # Diese Variable wird immer auf 0 zurueckgesetzt, wenn eine neue Zahl in das
                # Sudoku eingesetzt wird
    solved = check_sudoku(sudoku)  # ueberprueft ob das Sudoku geloest wurde. 
    while solved != True:          # solange das Sudoku nicht geloest ist, soll er veruchen es zu loesen
        run = run + 1              # run variable wird um 1 erhoeht

# Das folgende Stueck Code prueft nach dem Ausschlussprinzip, ob in ein Feld 
# nur noch eine moegliche Zahl kommen kann, wenn ja, setzt es diese ein.

        for i in range(9):           # iteriert ueber x- und y- Koordinaten des Sudokus
            for j in range(9):       # um alle Felder zu ueberpruefen
                reihe = sudoku[1:10,i,j]       # speichert die Liste der moeglichen Zahlen fuer ein Feld mit
                                               # Koordinaten (x,y) in reihe
                pruef = check_list(reihe)      # prueft wie viele Elemente in reihe ungleich Null sind.
            
                if pruef == 1:            # Wenn die Anzahl der Element die ungleich Null sind, eins betraegt,
                                          # dann wird die Zahl, die nicht gleich Null ist, an der ueberprueften
                                          # Stelle im Sudoku eingesetzt
                    sudoku = clues(sudoku,int(reihe[np.argmax(reihe)]),j+1,i+1) # Setzt Zahl ein
                    run = 0               # Sudoku wurde veraendert, run wird also 0



# Das folgende Stueck Code prueft nach dem Ausschlussprinzip, ob in einem Kaestchen 
# nur noch in ein Feld eine bestimmte Zahl eingesetzt werden kann, wenn ja, setzt es diese ein.    
    
        for n in range(1,10):        # iteriert über die verschiedenen Zahlen Ebenen
        
            for m in range(3):       # iteriert über die 9 verschieden moelichen Kaestchen
                for o in range(3):   # in einer Ebene
                
                    square = sudoku[n,3*m:3*(m+1),3*o:3*(o+1)]    # erstellt das Kaestchen
                    pruef = check_square(square)                  # prueft wie viele Elemente im Kaestchen 
                                                                  # ungleich Null sind.
                
                    if pruef == 1:                           # Wenn nur ein Element ungleich Null ist,
                                                             # werden die Koordinaten des Elements im Sudoku
                                                             # ermittelt
                        if int(np.argmax(square)) in [0,1,2]:
                            y = 1
                        
                        elif int(np.argmax(square)) in [3,4,5]:
                            y = 2
                        
                        elif int(np.argmax(square)) in [6,7,8]:
                            y = 3
                    
                    
                        if int(np.argmax(square)) in [0,3,6]:
                            x = 1
                        
                        elif int(np.argmax(square)) in [1,4,7]:
                            x = 2
                    
                        elif int(np.argmax(square)) in [2,5,8]:
                            x = 3
                        
                        sudoku = clues(sudoku,n,(x + (3*o)),(y + (3*m))) # Zahl wird eingesetzt
                        run = 0                                          # Sudoku wurde veraendert, run wird also 0

        
# Das folgende Stueck Code prueft nach dem Ausschlussprinzip, ob in einer Zeile oder Spalte 
# nur noch in ein Feld eine bestimmte Zahl eingesetzt werden kann, wenn ja, setzt es diese ein.
                    
        for n in range(1,10):  # iteriert ueber die verschiedenen Zahlen Ebenen 
            for m in range(9): # iteriert ueber Zeilen und Spalten in einer Zahlen Ebene
            
                zeile = sudoku[n,m,:]  # erstellt Zeile
                pruef_zeile = check_list(zeile)  # prueft wie viele Elemente die Zeile hat
                                                 # die ungleich Null sind
            
                if pruef_zeile == 1:      # Wenn die Anzahl der Element die ungleich Null sind, eins betraegt,
                                          # dann wird die Zahl, die nicht gleich Null ist, an der ueberprueften
                                          # Stelle im Sudoku eingesetzt
                
                    sudoku = clues(sudoku,n,int(np.argmax(zeile)) + 1,m + 1)  # Zahl die ungleich Null ist, wird
                                                                              # an entsprechender Stelle im Sudoku eingesetzt
                    run = 0               # Sudoku wurde veraendert, run wird also 0

            
                spalte = sudoku[n,:,m] # erstellt Spalte
                pruef_spalte = check_list(spalte)  # prueft wie viele Elemente die Spalte hat
                                                   # die ungleich Null sind
                if pruef_spalte == 1:     # Wenn die Anzahl der Element die ungleich Null sind, eins betraegt,
                                          # dann wird die Zahl, die nicht gleich Null ist, an der ueberprueften
                                          # Stelle im Sudoku eingesetzt
                
                    sudoku = clues(sudoku,n,m + 1,int(np.argmax(spalte)) + 1)  # Zahl die ungleich Null ist, wird
                                                                               # an entsprechender Stelle im Sudoku eingesetzt
                    run = 0               # Sudoku wurde veraendert, run wird also 0


# Das folgende Stueck Code kommt erst zum Einsatz, wenn das Programm bereits im dritten Durchlauf
# ist und keine weiteren Zahlen zum Sudoku hinzufuegen konnte, obwohl das Sudoku noch nicht geloest ist.
# Dies ist so, da diese Methode nur bei wenigen schweren Sudokus ueberhaupt zum loesen benoetigt wird. 
# Dabei wird ueberprueft ob in einer Zahlen Ebene Zeilen oder Spalten existieren mit der folgenden Eigenschaft:
# Alle Moeglichkeiten die Entsprechende Zahl in dieser Zeile oder Spalte unterzubringen befinden sich
# in einem 3x3 Kaestchen. Findet man eine Zeile oder Spalte mit dieser Eigenschaft, so koennen in dem
# entsprechenden Kaestchen alle anderen Moeglichkeiten die Zahl zu setzen vernachlaessigt werden. 
# Dies ist der Grund fuer die check_double Funktion.
    
        if run >= 3:                                   # wird nur im dritten Durchlauf ausgefuehrt
            for n in range(1,10):                      # iteriert ueber die verschiedenen Zahlen Ebenen
                for m in range(9):                     # iteriert ueber die Zeilen und Spalten
                
                    zeile = sudoku[n,m,:]                   # erstellt Zeile
                    pruef_zeile = check_list(zeile)         # ueberprueft wieviele Elemente in Zeile ungleich Null sind
                
                    if pruef_zeile == 2 or pruef_zeile == 3:  # sind 2 oder 3 Elemente ungleich Null,
                                                              # wird fortgesetzt, andernfalls koennen sie nicht
                                                              # in einem Kaestchen sein
                    
                        doubles = check_double(zeile,pruef_zeile) # prueft ob die Elemente im selben Kaestchen sind 
                        if doubles[0] == True:                    # Falls ja, wird fortgesetzt
                        
                            if m in [0,3,6]:                      # es wird nun ermittelt, welche Zeilen der Zahlen Ebene
                                                              # gleich Null gesetzt werden muessen
                                                              
                                sudoku[n,m+1:m+3,doubles[1]*3:(doubles[1]+1)*3] = 0
                            
                            elif m in [1,4,7]:
                                sudoku[n,m-1,doubles[1]*3:(doubles[1]+1)*3] = 0
                                sudoku[n,m+1,doubles[1]*3:(doubles[1]+1)*3] = 0
                            
                            else:
                                sudoku[n,m-2:m,doubles[1]*3:(doubles[1]+1)*3] = 0
                            
                            
                    spalte = sudoku[n,:,m]              # erstellt Spalte
                    pruef_spalte = check_list(spalte)   # ueberprueft wieviele Elemente in Zeile ungleich Null sind

                    if pruef_spalte == 2 or pruef_spalte == 3:      # sind 2 oder 3 Elemente ungleich Null,
                                                                # wird fortgesetzt, andernfalls koennen sie nicht
                                                                # in einem Kaestchen sein
                                                                
                        doubles = check_double(spalte,pruef_spalte) # prueft ob die Elemente im selben Kaestchen sind 
                        if doubles[0] == True:
                            if m in [0,3,6]:                  # es wird nun ermittelt, welche Zeilen der Zahlen Ebene
                                                              # gleich Null gesetzt werden koennen
                                sudoku[n,doubles[1]*3:(doubles[1]+1)*3,m+1:m+3] = 0
                            
                            elif m in [1,4,7]:
                                sudoku[n,doubles[1]*3:(doubles[1]+1)*3,m-1] = 0
                                sudoku[n,doubles[1]*3:(doubles[1]+1)*3,m+1] = 0
                            
                            else:
                                sudoku[n,doubles[1]*3:(doubles[1]+1)*3,m-2:m] = 0 

    
    
        # Zuletzt wird erneut ueberprueft ob das Sudoku geloest wurde     
        solved = check_sudoku(sudoku)
                            
    # gibt das fertige Sudoku aus
    return(a[0,:,:])


####### Beispiel Sudoku #######################################################################################

# Erstelle leeres Sudoku   
a = empty_sudoku()

# 1. Hinweis manuell einfuegen
a[0,0,0] = 7
a[1:,0,0] = 0
a[7,:,0] = 0
a[7,0,:] = 0
a[7,0:3,0:3] = 0

# 2. Hinweis manuell einfuegen
a[0,1,0] = 5
a[1:,1,0] = 0
a[5,:,0] = 0
a[5,1,:] = 0
a[5,0:3,0:3] = 0

# restlichen Hinweise mit Funktion clues einfuegen
a = clues(a,4,4,1)
a = clues(a,9,5,1)
a = clues(a,2,7,2)
a = clues(a,6,8,2)
a = clues(a,8,4,4)
a = clues(a,3,8,4)
a = clues(a,5,9,4)
a = clues(a,1,2,5)
a = clues(a,3,4,5)
a = clues(a,6,3,6)
a = clues(a,6,5,7)
a = clues(a,9,7,7)
a = clues(a,3,1,8)
a = clues(a,4,9,8)
a = clues(a,2,6,9)    

# Loesen mit SudokuSolve Funktion
print(SudokuSolve(a))