import numpy as np                    # importiert numpy
from random import shuffle            # importiert die Funktion Elemente einer liste zufaellig zu mischen
import SudokuLoeser as sl             # importiert unser Sudoku-Loesungsprogramm

################################################################################################################
### Ueberprueft, ob keine Nullen mehr im Sudoku sind

def check_sudokuG(sudoku):
    s = np.reshape(sudoku[:,:],81)
    x = 0
    for i in range(81):
        if s[i] == 0:
            x = x + 1
    
    if x > 0:
        return(False)
    else:
        return(True)

################################################################################################################
### Ueberprueft, wie viele Elemente in einer gegebenen Reihe ungleich Null sind

def check_listG(reihe):
    x = 0
    for i in range(81):
        if reihe[i] != 0:
            x = x + 1
    
    return(x)

################################################################################################################
### Erstellt den Versuch eines vollstaendigen Sudokus  

def mkAnswer(sudoku):                          
    for Y in range(9):                           # iteriert ueber alle leeren Felder 
        for X in range(9):                       #               
            sudoku = setNumber(X,Y,sudoku)       # Setzt Zahlen in die leeren Felder ein

            
    return(sudoku)

################################################################################################################
### Diese Funktion setzt in mkAnswer die Zahlen in das Sudoku ein

def setNumber(X,Y,sudoku):
    possibilitys = mklst(X,Y,sudoku)                    # erstellt Liste von Moeglichen Zahlen fuer das leere Feld
    P = len(possibilitys)                               # speichert die Laenge der Liste in P
    if P > 0:                                           # sollte die Liste nicht leer sein, 
        sudoku[Y,X] = np.random.choice(possibilitys,1)  # wird ein zufaelliges Element der Liste in das leere 
                                                        # Feld eingsetzt. Sollte die Liste leer sein,
                                                        # bleibt das Feld Null
    return(sudoku)           # gibt das veraenderte Sudoku zurueck

################################################################################################################
### Die Funktion erstellt in setNumber die Liste moeglicher Zahlen

def mklst(X,Y,sudoku):
    lst = [1,2,3,4,5,6,7,8,9]            # Zahle die in ein leeres Feld kommen koennten
    zeile = sudoku[Y,0:9]                # Zeile in der sich das leere Feld im Sudoku befindet
    spalte = sudoku[0:9,X]               # Spalte in der sich das leere Feld im Sudoku befindet
    
    if Y in [0,1,2]:                     # lokalisiert das 3x3 Kaestchen in welchem sich das leere Feld befindet
        if X in [0,1,2]:                 #
            square = sudoku[0:3,0:3]     #
                                         #
        elif X in [3,4,5]:               #
            square = sudoku[0:3,3:6]     #
                                         #  
        elif X in [6,7,8]:               #
            square = sudoku[0:3,6:9]     #
                                         #
    elif Y in [3,4,5]:                   #
        if X in [0,1,2]:                 #
            square = sudoku[3:6,0:3]     #
                                         #
        elif X in [3,4,5]:               #
            square = sudoku[3:6,3:6]     # 
                                         #
        elif X in [6,7,8]:               #
            square = sudoku[3:6,6:9]     #
                                         #
    elif Y in [6,7,8]:                   #
        if X in [0,1,2]:                 #
            square = sudoku[6:9,0:3]     #
                                         #
        elif X in [3,4,5]:               #
            square = sudoku[6:9,3:6]     #
                                         #
        elif X in [6,7,8]:               #
            square = sudoku[6:9,6:9]     #
    
    rechteck = np.reshape(square,9)      # formt das 2D-array des 3x3 Kaestchens in ein eindimensionales um
    
    for s in spalte:       # alle Zahlen die in der Spalte sind, werden aus der Liste lst entfernt
        if s in lst:       # 
            lst.remove(s)  #
    
    for z in zeile:        # alle Zahlen die in der Zeile sind, werden aus der Liste lst entfernt
        if z in lst:       #
            lst.remove(z)  #
            
    for r in rechteck:     # alle Zahlen die im 3x3 Kaestchen sind, werden aus der Liste lst entfernt
        if r in lst:       #
            lst.remove(r)  #
            
    return(lst)  # die Liste moeglicher Zahlen wird zurueckgegeben

################################################################################################################
### Erstellt vollstaendig ausgefuelltes Sudoku     

def SudokuGen():
    solved = False                          # solange im generierten Sudoku Nullen sind,
    while solved != True:                   # soll erneut ein Sudoku generiert werden
        sudoku = np.zeros((9,9))               # erstellt leeres Sudoku
        sudoku = mkAnswer(sudoku)              # generiert Sudoku
        solved = check_sudokuG(sudoku)         # ueberprueft ob im Sudoku Nullen sind. Wird True, falls nicht
                                               # wird also True wenn Sudoku widerspruchslos gefuellt ist
    return(sudoku)             # gibt Sudoku zurueck

################################################################################################################
### Gibt eine Liste, von sogenannten unavoidable squares (UAS) fuer ein gegebenes Sudoku zurueck

def find_unavoidable_squares(sudoku):
    squares = []                          # definiert die Liste die spaeter zurueckgegeben wird
    for y in range(8):                    # iteriert ueber alle Felder, bis auf die in der letzten 
        for x in range(8):                # Zeile oder Spalte
            # Sucht zunaechst zeilenweise nach UAS
            #   X X
            #
            #   X X
            #
            num = sudoku[y,x]             # Zahl die im zubetrachtenden Feld steht wird in num gespeichert 
            if num != 0:                        # ist num != 0:
                numRight = sudoku[y,x+1]        # Speichert die Zahl rechts von num in numRight
                for n in range(y+1,9):          # geht Spalte von num aus durch
                    counterRight = sudoku[n,x]                          # Wenn eine Zahl in der weiteren
                    counterNum = sudoku[n,x+1]                          # Spalte gleich numRight ist und   
                    if counterRight == numRight and counterNum == num:  # die Zahl rechts davon gleich Num:
                        UAS = [(x,y),(x+1,y),(x,n),(x+1,n)]    # Die Koordinaten der vier Felder werden als Liste
                        squares.append(UAS)                    # zu squares hinzugefuegt
            
            # Sucht dann Spaltenweise nach UAS
            #   X    X 
            #   X    X
                numDown = sudoku[y+1,x]         # Speichert die Zahl unter num in numDown
                for m in range(x+1,9):          # geht Zeile von num aus durch
                    counterDown = sudoku[y,m]                         # Wenn eine Zahl in der weiteren
                    counterNum = sudoku[y+1,m]                        # Zeile gleich numDown ist und
                    if counterDown == numDown and counterNum == num:  # die Zahl darunter gleich Num:
                        UAS = [(x,y),(x,y+1),(m,y),(m,y+1)]      # Die Koordinaten der vier Felder werden als Liste
                        squares.append(UAS)                      # zu squares hinzugefuegt
            
    return(squares)     # gibt Liste der UAS zurueck
     
################################################################################################################               
###### Verschiedene Generator Arten ############################################################################

################################################################################################################
### Die folgende Funktion generiert ein Sudoku mit N Hinweisen durch zufaellige Entnahme 
### von Zahlen aus einem vollstaendigen Sudoku
    
def take_sudoku(N):
    pos = [0,1,2,3,4,5,6,7,8]                  # Liste moeglicher Koordinaten
    quest = SudokuGen()                        # generiert vollstaendiges Sudoku
    x = check_listG(quest.reshape(81))       # speichert die Anzahl der gefuellten Felder in x 
    while x != N:                              # solange die Zahl an gefuellten Feldern nicht N ist:
        i = np.random.choice(pos)                  # werden zufaellig x- und y-Koordinaten gewaehlt
        j = np.random.choice(pos)                  # und
        quest[i,j] = 0                             # das entsprechende Feld geleert
        x = check_listG(quest.reshape(81))       # x wird aktualisiert
    

    sudoku = sl.empty_sudoku()                                    # schließlich wird
    for n in range(1,10):                                         # das Sudoku in eine Form
        for m in range(1,10):                                     # gebracht, mit der unser Loeser
            if quest[n-1,m-1] != 0:                               # arbeiten kann
                sudoku = sl.clues(sudoku,int(quest[n-1,m-1]),m,n) #
    
    return(sudoku)    # gibt Sudoku zurueck
    
################################################################################################################
### Die folgende Funktion generiert ein Sudoku mit N Hinweisen durch zufaellige Entnahme 
### von Zahlen aus einem vollstaendigen Sudoku. Dabei wird darauf geachtet, dass niemals
### mehr als 3 Felder eines UAS leer sind

def make_uas_sudoku(N):
    no_sudoku = True            # Variable speichert ob ein Sudoku-Puzzle gefunden wurde
    while no_sudoku == True:    # Solange kein Sudoku-Puzzle gefunden wurde:
        sudoku = SudokuGen()    # Generiert vollstaendiges Sudoku
        shuffs = 0              # Variable speichert wie oft neu gemischt wurde
        while shuffs != 25:     # Es soll hoechstens 25 al neu gemischt werden
            pairs = [[x,y] for x in range(9) for y in range(9)]  # Liste aller moeglichen Koordinatenpaare
            squares = find_unavoidable_squares(sudoku)           # Liste von UAS
            shuffle(pairs)                                       # mischt Elemente von pairs
            shuffs = shuffs + 1                                  # erhoeht shuffs um 1
            pairs = np.array(pairs)                              # macht pairs zu array
            runs = 0                                             # Anzahl der Durchlaeufe der folgenden Schleife
            copyshuff = np.copy(sudoku)                          # Kopie des Sudokus, die bearbeitet wird
                                                                 # Jedes Sudoku soll mit 25 verschieden gemischten
                                                                 # Liste pairs bearbeitet werden
            
            while len(pairs) != N:                               # Solange Anzahl der Hinweise N nicht erreicht ist:
                copy = np.copy(copyshuff)                        # erstellt eine Kopie der Kopie.
                check_squares = False                            # ueberprueft ob das Element mit Indiz run aus pairs
                for n in squares:                                # einziges Teil eines UAS ist
                    for m in n:                                                    #
                        if np.array_equal(m,pairs[runs]) == True and len(n) == 1:  #
                            check_squares = True                                   # Wenn ja, wird check_squares = True
                        
                
                runs = runs + 1                       # run wird erhoeht, dadurch wird sichergestellt,
                                                      # dass zwar jedes neue Feld zufaellig ist, niemals aber
                                                      # eines welches schon eimal probiert wurde
                
                if check_squares == False:                       # Ist check_squares nicht True, kann das Feld mit 
                    copy[pairs[runs][1],pairs[runs][0]] = 0      # den Koordinaten pairs[runs] in der Kopie der Kopie 
                    copyshuff = np.copy(copy)                    # gleich Null gesetzt werden copyshuff wird Kopie
                    pairs = np.delete(pairs,runs-1,0)            # von copy die Koordinaten werden aus pairs geloescht
                    runs = 0                                     # und runs wird zu Null zurueckgesetzt
                    
                if (runs+1) == len(pairs):                                # sollten keine neuen Zahlen eingesetzt werden
                    break                                                 # koennen, wird aus der Schleife ausgebrochen
            
            if len(pairs) == N:                      # wurde die Schleife verlassen, weil das gewuenschte Sudoku
                sudoku = np.copy(copyshuff)          # generiert wurde, wird hier sudoku zur Kopie von copyshuff
                break                                # und die Schleife zum Mischen verlassen
            
        if len(pairs) == N:                # wurde die Schleife verlassen, weil das gewuenschte Sudoku
            no_sudoku = False              # generiert wurde und nicht weil 25 mal mischen nicht zum Ergebnis gefuehrt
                                           # hat, wird no_sudoku = False und somit der weg frei zur Ausgabe des Sudokus
    
    return(sudoku)    # gibt Sudoku aus
    
################################################################################################################
### Die folgende Funktion generiert ein Sudoku mit N Hinweisen durch zufaelliges Einsetzen 
### von Zahlen in ein leeres Sudoku
    
def tot_rand_sudoku(N):
    pos = [0,1,2,3,4,5,6,7,8]                 # Liste moeglicher Koordinaten
    sudoku = sl.empty_sudoku()                # erstellt leeres Sudoku
    c = 0                                     # Speichert Anzahl an Hinweisen
    while c < N:                                 # Solange die Zahl der Hinweise kleiner N ist:
        x = np.random.choice(pos)                # werden Koordinaten und 
        y = np.random.choice(pos)                # Fuellungen zufaellig ausgewaehlt 
        z = np.random.choice(pos) + 1            #
        if sudoku[0,y,x] == 0:                      # Ist diese Stelle des Sudokus leer:
            sudoku = sl.clues(sudoku,z,x,y)         # wird z bei den Koordinaten x,y eingesetzt
            c = c + 1                               # und c aktualisiert
            
    return(sudoku)
    
################################################################################################################
### Die folgende Funktion generiert ein Sudoku mit N Hinweisen durch zufaelliges Einsetzen 
### von Zahlen in ein leeres Sudoku. Dabei wird sichergestellt, dass mindestens 8 von 9 Zahlen
### als Hinweise im Sudoku vorhanden sind.
    
def part_rand_sudoku(N):
    korr = [0,1,2,3,4,5,6,7,8]               # Liste der moeglichen Koordinaten
    pos = [1,2,3,4,5,6,7,8,9]                # Liste der moeglichen Zahlen
    
    sudoku = sl.empty_sudoku()       # erstellt leeres Sudoku
    c = 0                            # Variable speichert die Zahl der Hinweise im Sudoku
    while c < N:                                     # Solange die Anzahl der Zahlen, kleiner als die Anzahl 
        x = np.random.choice(korr)                   # der gewuenschten Hinweise ist, sollen Zahlen eingesetzt werden.
        y = np.random.choice(korr)                   # Koordinaten werden zufaellig aus korr gewaehlt
        z = np.random.choice(pos)                    # einzusetzende Zahl wird aus pos gewaehlt
        if sudoku[0,y,x] == 0:                       # ist das Feld der gewaehlten Koordinaten leer:
            sudoku = sl.clues(sudoku,z,x + 1,y + 1)  # wird die Zahl eingesetzt
            c = c + 1                                # Also auch die Vriable c erhoeht
            if c < 8:                                # Sollte c kleiner als 8 sein, wird z aus der Liste der moeglichen
                pos.remove(z)                        # Zahlen pos entfernt, so wird sicher gestellt, dass mindestens
                                                     # 8 von 9 Zahlen im Sudoku-Puzzle verwendet werden
                
            else:                                    # Ist die Zahl der Hinweise im Sudoku 8 oder groeßer, ist die                
                pos = [1,2,3,4,5,6,7,8,9]            # Auswahl der Zahlen frei
                
    return(sudoku)
    
################################################################################################################
### Die folgende Funktion generiert ein Sudoku mit N Hinweisen durch zufaelliges Einsetzen 
### von Zahlen in ein leeres Sudoku. Dabei wird sichergestellt, dass mindestens 8 von 9 Zahlen
### als Hinweise im Sudoku vorhanden sind und wenn immer das Einsetzen einer Zahl zu Widerspruechen
### fuehren wuerde, wird das Sudoku geleert und erneut versucht.

def rules_rand_sudoku(N):
    pos = [1,2,3,4,5,6,7,8,9]                # Liste der moeglichen Zahlen
    sudoku = sl.empty_sudoku()               # erstellt leeres Sudoku
    c = 0                                    # Variable speichert die Zahl der Hinweise im Sudoku
    pairs = [[x,y] for x in range(9) for y in range(9)]  # erstellt Liste aller moeglichen Koordinatenpaare
    shuffle(pairs)                                       # mischt diese Liste
    while c < N:                                  # Solange die Anzahl der Zahlen, kleiner als die Anzahl 
        koor = pairs[0]                           # der gewuenschten Hinweise ist, sollen Zahlen eingesetzt werden.
        x = koor[0]                               # Koordinaten werden als erstes Element aus pairs gewaehlt.
        y = koor[1]                               # z(Inhalt des Feldes) wird zufaellig aus pos gewaehlt
        z = np.random.choice(pos)                 # 
            
        pruef = sudoku[1:,y,x]                       # macht Liste von Zahlen die noch in das Feld kommen kann.
        if sudoku[0,y,x] == 0 and z in pruef:        # Falls das gewaehlte Feld leer und die einzusetzende Zahl
            sudoku = sl.clues(sudoku,z,x + 1,y + 1)  # in der Liste der Moeglichkeiten ist, wird die Zahl eingesetzt,
            pairs.remove(koor)                       # das Koordinatenpaar aus pairs entfernt,
            c = c + 1                                # c wird erhoeht und falls c unter 8 liegt
            
            if c < 8:                                # wird z wieder aus pos entfernt.
                pos.remove(z)                        # Fuer c >= 8 ist pos wieder die liste der Zahlen von 1 bis 9
                                                     #
            else:                                    #
                pos = [1,2,3,4,5,6,7,8,9]            #
                    
        elif sudoku[0,y,x] == 0 and pruef == []:     # Sollte ein Feld, sowie die Liste der Moeglichkeiten in diesem Feld
            sudoku = sl.empty_sudoku()               # Null sein, wird das Sudoku geleert, c auf Null zurueckgesetzt
            c = 0                                    # pairs zurueckgesetzt und neu gemischt                                 
            pairs = [[x,y] for x in range(9) for y in range(9)] #
            shuffle(pairs)
    
    return(sudoku)

################################################################################################################
### Die folgende Funktion generiert ein Sudoku mit N Hinweisen durch zufaellige Entnahme 
### von Zahlen aus einem vollstaendigen Sudoku. Dabei wird darauf geachtet, dass niemals
### mehr als 3 Felder eines UAS leer sind. Zudem wird jedesmal wenn eine Zahl entfernt werden soll
### zunaechst ueberprueft, ob das entfernen dazu fuehren wuerde, dass das Sudoku zwei oder mehr Loesungen bekommt
            
def final_sudoku_generator(N):
    no_sudoku = True            # Variable speichert ob ein Sudoku-Puzzle gefunden wurde
    while no_sudoku == True:    # Solange kein Sudoku-Puzzle gefunden wurde:
        sudoku = SudokuGen()    # Generiert vollstaendiges Sudoku
        shuffs = 0              # Variable speichert wie oft neu gemischt wurde
        while shuffs != 25:     # Es soll hoechstens 25 al neu gemischt werden
            pairs = [[x,y] for x in range(9) for y in range(9)]  # Liste aller moeglichen Koordinatenpaare
            squares = find_unavoidable_squares(sudoku)           # Liste von UAS
            shuffle(pairs)                                       # mischt Elemente von Pairs
            shuffs = shuffs + 1                                  # erhoeht shuffs um 1
            pairs = np.array(pairs)                              # macht pairs zu array
            runs = 0                                             # Anzahl der Durchlaeufe der folgenden Schleife
            copyshuff = np.copy(sudoku)                          # Kopie des Sudokus, die bearbeitet wird
                                                                 # Jedes Sudoku soll mit 25 verschieden gemischten
                                                                 # Liste pairs bearbeitet werden
            
            while len(pairs) != N:                               # Solange Anzahl der Hinweise N nicht erreicht ist:
                copy = np.copy(copyshuff)                        # erstellt eine Kopie der Kopie.
                check_squares = False                            # ueberprueft ob das Element mit Indiz run aus pairs
                for n in squares:                                # einziges Teil eines UAS ist
                    for m in n:                                                    #
                        if np.array_equal(m,pairs[runs]) == True and len(n) == 1:  #
                            check_squares = True                                   # Wenn ja, wird check_squares = True
                        
                if check_squares == False:                       # Ist check_squares nicht True, kann das Feld mit 
                    copy[pairs[runs][1],pairs[runs][0]] = 0      # den Koordinaten pairs[runs] in der Kopie der Kopie 
                                                                 # gleich Null gesetzt werden
                        
                        
                test = sl.empty_sudoku()                                  # Kopie der Kopie des Sudokus wird nun
                for y in range(1,10):                                     # zur Loesung mit dem Sudoku-Loeser
                    for x in range(1,10):                                 # vorbereitet
                        if copy[y-1,x-1] != 0:                            #
                            test = sl.clues(test,int(copy[y-1,x-1]),x,y)  #
                        
            
                SUSO = sl.SudokuSolve(test)                               # Nun wird die Kopie der Kopie auf
                                                                          # Loesbarkeit getestet
                runs = runs + 1                       # run wird erhoeht, dadurch wird sichergestellt,
                                                      # dass zwar jedes neue Feld zufaellig ist, niemals aber
                                                      # eines welches schon eimal probiert wurde
                if SUSO[0] == 'Eine Lösung' and check_squares == False:   # Ist copy eindeutig loesbar und 
                                                                          # verschieden zu copyshuff:
                    copyshuff = np.copy(copy)                             # wird copyshuff zur Kopie von copy.
                    pairs = np.delete(pairs,runs-1,0)                     # wird das verwendete Koordinatenpaar
                                                                          # aus pairs entfernt.
                    runs = 0                    # run wird wieder Null, denn das erste Element aus pairs
                                                # ist nun ein anderes
                    
                if SUSO[0] == 'Zwei Lösungen' and (runs+1) == len(pairs): # Ist copy nicht eindeutig loesbar
                    break                                                 # und wurden alle Koordinatenpaare in
                                                                          # pairs ausprobiert, ohne, dass das Entfernen
                                                                          # zu einem anderen eindeutig loesbaren
                                                                          # Sudoku fuehrt, wird aus dieser 
                                                                          # Schleife ausgebrochen und damit eine
                                                                          # neue Reihenfolge von pairs oder ein
                                                                          # komplett neues Sudoku versucht.
            
            if SUSO[0] == 'Eine Lösung':             # wurde die Schleife verlassen, weil das gewuenschte Sudoku
                sudoku = np.copy(copyshuff)          # generiert wurde, wird hier sudoku zur Kopie von copyshuff
                break                                # und die Schleife zum Mischen verlassen
            
        if SUSO[0] == 'Eine Lösung':       # wurde die Schleife verlassen, weil das gewuenschte Sudoku
                no_sudoku = False          # generiert wurde und nicht weil 25 mal mischen nicht zum Ergebnis gefuehrt
                                           # hat, wird no_sudoku = False und somit der weg frei zur Ausgabe des Sudokus
    
    return(sudoku)    # gibt Sudoku aus
    

###################################### Beispiel ###############################################################

sudoku = final_sudoku_generator(24) # erstellt eindeutig loesbares Sudoku mit 24 Hinweisen
print(sudoku)

    
    
    
    
