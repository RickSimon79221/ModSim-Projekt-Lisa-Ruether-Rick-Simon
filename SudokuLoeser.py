# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:17:45 2018

@author: Rick
"""

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
    
# Beispiel Sudoku

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

# stelle Sudoku dar
print(a)