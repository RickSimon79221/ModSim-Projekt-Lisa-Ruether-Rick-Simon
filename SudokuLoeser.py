import numpy as np                   # importiert Numpy um Matritzen nutzen zu koennen

################################################### EMPTY SUDOKU ###########################################################
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

################################################### CLUES #################################################################
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

################################################### CHECK LIST #############################################################
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

################################################### CHECK SQUARE ###########################################################
'''
Die folgende Funktion prueft fuer ein 3x3 Kaestchen wie viele Eintraege davon
ungleich Null sind und gibt diese aus. 
'''
def check_square(square):
    s = np.reshape(square,9)
    x = check_list(s)
    return(x)


########################################### CHECK DOUBLE ##################################################################    
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
        
############################################# CHECK NUMBER ################################################################
'''
Die folgende Funktion ueberprueft, ob in ein Feld im Sudoku im Konflikt 
mit einem anderen Feld in dem Sudoku steht. Es gibt beispielsweise False aus wenn die 
Zahl im betrachteten Feld, bereits in der gleichen Zeile, Spalte oder im selben 3x3 Kaestchen vorhanden ist.
'''
def check_number(sudoku,Number,x,y):
    k = 0
    check_zeile = sudoku[0,y,:]           # Lokalisiert Zeile in der sich das betroffene Feld befindet
    l = 0
    check_spalte = sudoku[0,:,x]          # Lokalisiert Spalte in der sich das betroffene Feld befindet
            
    if y in [0,1,2]:                      # Lokalisiert 3x3 Kaestchen in der sich das betroffene Feld befindet
        if x in [0,1,2]:
            square = sudoku[0,0:3,0:3]
            
        elif x in [3,4,5]:
            square = sudoku[0,0:3,3:6]
            
        elif x in [6,7,8]:
            square = sudoku[0,0:3,6:9]
        
    elif y in [3,4,5]:
        if x in [0,1,2]:
            square = sudoku[0,3:6,0:3]
        
        elif x in [3,4,5]:
            square = sudoku[0,3:6,3:6]
            
        elif x in [6,7,8]:
            square = sudoku[0,3:6,6:9]
        
    elif y in [6,7,8]:
        if x in [0,1,2]:
            square = sudoku[0,6:9,0:3]
            
        elif x in [3,4,5]:
            square = sudoku[0,6:9,3:6]
            
        elif x in [6,7,8]:
            square = sudoku[0,6:9,6:9]
            
    r = 0
    rechteck = np.reshape(square,9)
            
    for i in range(9):                  # Zaehlt wie oft die Zahl des betroffenen Feldes in Zeile, Spalte 
        if check_zeile[i] == Number:    # und 3x3 Kaestchen vorkommt
            k = k + 1
            
        if check_spalte[i] == Number:
            l = l + 1
            
        if rechteck[i] == Number:
            r = r + 1
            
    if k == 1 and l == 1 and r == 1:   # Nur wenn die Zahl des ueberprueften Feldes einzigartig in Zeile
                                       # Spalte und 3x3 Kaestchen ist.
        return(True)
    
    else:
        return(False)
    

#################################################### CHECK SUDOKU ##########################################################
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

##################################################### SUDOKU SOLVABLE ######################################################
'''
Die folgende Funktion ueberpruft ob ein Sudoku ueberhaupt loesbar ist.
Zunaechst wird mithilfe der check_number Funktion ueberprueft, ob eine Zahl
im Sudoku in Zeile, Spalte oder 3x3 Kaestchen mehrmals vorkommt.
Zugleich wird ueberprueft, ob es ein Feld gibt, welches leer ist, in das aber 
auch keine Zahl kommen kann. Auch in diesem Fall ist das Sudoku nicht loesbar
und sudoku_solvable gibt False zurueck.
Wenn die Funktion aber durchlaufen wird, ohne False zurueckzugeben, gibt sie True zurueck.
'''
def sudoku_solvable(sudoku):
    ################################################################################################
    # Ueberprueft ob im Sudoku in einer Zeile, Spalte oder einem Kaestchen eine Zahl mehrmals vorkommen
    for y in range(9):
        for x in range(9):
            if sudoku[0,y,x] != 0:
                c = check_number(sudoku,int(sudoku[0,y,x]),x,y)  # ueberprueft ob das Feld im Konflikt mit anderen  steht
                if c == False:
                    return(False)
                
    ################################################################################################
    # Ueberprueft ob es leere Felder gibt, in das auch keine weiteren Zahlen kommen koennen 
            
            else:
                reihe = sudoku[1:10,y,x]       
                pruef = check_list(reihe) # prueft wie viele Zahlen noch in ein Feld eingesetzt werden koennen
                if pruef == 0:
                    return(False)
    return(True)

############################################################################################################################
###############################  SUDOKU SOLVE  #############################################################################
############################################################################################################################
'''
Die folgende Funktion ist die, die fuer das Loesen des Sudokus zustaendig ist.
'''
def SudokuSolve(sudoku):
    run = 0             # Die Variable run zaehlt wie oft die folgende while-Schleife Durchlaufen wurde,
                        # ohne das das Sudoku veraendert wurde
    while True:
        run = run + 1   # run wird erhoeht, da die Schleife einen neuen Durchgang beginnt
        solvable = sudoku_solvable(sudoku)  # zunaechst wir uebrprueft ob das Sudoku ueberhaupt noch loesbar ist.
                                            # siehe die Funktion: sudoku_solvable
        
        if solvable == False:               # sollte das Sudoku nicht loesbar sein, soll das Sudoku in seinem 
            return(['Keine Lösung',sudoku]) # derzeitigen Zustand sowie die Information, dass das Sudoku nicht 
                                            # loesbar ist ausgegeben werden
        
        ### AUSSCHLUSS ##########################################################
        # Das folgende Stueck Code prueft nach dem Ausschlussprinzip, ob in ein Feld 
        # nur noch eine moegliche Zahl kommen kann, wenn ja, setzt es diese ein.
        
        for y in range(9):                # Zunaechst wird ueber alle Felder
            for x in range(9):            # des Sudokus iteriert
                
                reihe = sudoku[1:10,y,x]  # macht eine Liste der Zahlen die noch in ein Feld eingesetzt werden koennen.     
                pruef = check_list(reihe) # zaehlt wie viele Elemente die genannte Liste hat (die ungleich Null sind)    
                if pruef == 1:            # hat die Liste nur ein Element (das ungleich Null ist) kann dieses in das
                                          # leere Feld eingesetzt werden
                    sudoku = clues(sudoku,int(reihe[np.argmax(reihe)]),x+1,y+1) # setzt Zahl in das Feld des Sudokus ein
                    run = 0               # Sudoku wurde veraendert, run wird also 0  
        #########################################################################
        
        ### SQUARE-AUSSCHLUSS ###################################################
        # Das folgende Stueck Code prueft nach dem Ausschlussprinzip, ob in einem Kaestchen 
        # nur noch in ein Feld eine bestimmte Zahl eingesetzt werden kann, wenn ja, setzt es diese ein. 
        
        for n in range(1,10):        # iteriert über die verschiedenen Zahlen Ebenen
            for i in range(3):       # iteriert über die 9 verschieden moelichen Kaestchen
                for j in range(3):   # in einer Ebene
                    
                    square = sudoku[n,3*i:3*(i+1),3*j:3*(j+1)]   # erstellt das 3x3 Kaestchen
                    pruef = check_square(square)                 # prueft wie viele Elemente im Kaestchen 
                                                                 # ungleich Null sind.
                    
                    if pruef == 1:                               # Wenn nur ein Element ungleich Null ist,
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
                        
                        sudoku = clues(sudoku,n,(x + (3*j)),(y + (3*i)))  # Zahl wird eingesetzt
                        run = 0                                           # Sudoku wurde veraendert, run wird also 0 
        #########################################################################
        
        ### ZEILE/SPALTE - AUSSCHLUSS und Double ################################
        # Das folgende Stueck Code prueft nach dem Ausschlussprinzip, ob in einer Zeile oder Spalte 
        # nur noch in ein Feld eine bestimmte Zahl eingesetzt werden kann, wenn ja, setzt es diese ein.
        #
        # Ebenfalls wird ueberprueft ob in einer Zahlen Ebene Zeilen oder Spalten existieren mit der folgenden Eigenschaft:
        # Alle Moeglichkeiten die Entsprechende Zahl in dieser Zeile oder Spalte unterzubringen befinden sich
        # in einem 3x3 Kaestchen. Findet man eine Zeile oder Spalte mit dieser Eigenschaft, so koennen in dem
        # entsprechenden Kaestchen alle anderen Moeglichkeiten die Zahl zu setzen vernachlaessigt werden. 
        # Dies ist der Grund fuer die check_double Funktion.
        
        for n in range(1,10):    # iteriert ueber die verschiedenen Zahlen Ebenen
            for m in range(9):   # iteriert ueber Zeilen und Spalten in einer Zahlen Ebene
                zeile = sudoku[n,m,:]           # erstellt Zeile
                pruef_zeile = check_list(zeile) # prueft wie viele Elemente die Zeile hat
                                                # die ungleich Null sind
                
                if pruef_zeile == 1:            # Wenn die Anzahl der Element die ungleich Null sind, eins betraegt,
                                                # dann wird die Zahl, die nicht gleich Null ist, an der ueberprueften
                                                # Stelle im Sudoku eingesetzt
                    sudoku = clues(sudoku,n,int(np.argmax(zeile)) + 1,m + 1)    # Zahl wird eingesetzt                                         
                    run = 0                                                     # Sudoku wurde veraendert, run wird also 0
                
                
                elif pruef_zeile == 2 or pruef_zeile == 3:    # sind 2 oder 3 Elemente ungleich Null,
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

            
                
                spalte = sudoku[n,:,m]            # erstellt Spalte
                pruef_spalte = check_list(spalte) # prueft wie viele Elemente die Spalte hat
                                                  # die ungleich Null sind
                
                if pruef_spalte == 1:             # Wenn die Anzahl der Element die ungleich Null sind, eins betraegt,
                                                  # dann wird die Zahl, die nicht gleich Null ist, an der ueberprueften
                                                  # Stelle im Sudoku eingesetzt
                    sudoku = clues(sudoku,n,m + 1,int(np.argmax(spalte)) + 1)   # Zahl wird eingesetzt                               
                    run = 0                                                     # Sudoku wurde veraendert, run wird also 0
                    
                
                elif pruef_spalte == 2 or pruef_spalte == 3:      # sind 2 oder 3 Elemente ungleich Null,
                                                                  # wird fortgesetzt, andernfalls koennen sie nicht
                                                                  # in einem Kaestchen sein
                    doubles = check_double(spalte,pruef_spalte)   # prueft ob die Elemente im selben Kaestchen sind
                    if doubles[0] == True:
                        if m in [0,3,6]:                          # es wird nun ermittelt, welche Zeilen der Zahlen Ebene
                                                                  # gleich Null gesetzt werden koennen
                            sudoku[n,doubles[1]*3:(doubles[1]+1)*3,m+1:m+3] = 0
                               
                            
                        elif m in [1,4,7]:
                            sudoku[n,doubles[1]*3:(doubles[1]+1)*3,m-1] = 0
                            sudoku[n,doubles[1]*3:(doubles[1]+1)*3,m+1] = 0
                                
                            
                        else:
                            sudoku[n,doubles[1]*3:(doubles[1]+1)*3,m-2:m] = 0 
                        
        #########################################################################
        
        ### NAKED SUBSET ########################################################
        # Das folgende Stueck Code beschreibt eine Methode die sich Naked Subset nennt. Dabei geht es darum
        # das wenn man in einem 3x3 Kaestchen Felder findet in die, die gleichen Zahlen kommen koennen (Anzahl der m),
        # wobei die Anzahl der moeglichen Zahlen gleich der fraglichen Felder ist, dann kann man davon ausgehen, dass
        # die fraglichen Zahlen nur in eben jene Felder kommen koennen. Diese Moeglichkeiten koennen demnach
        # aus den anderen Feldern eleminiert werden. 
        
        for a in range(3):     # zunaechst wird ueber die verschieden 3x3 Kaestchen iteriert 
            for b in range(3): #
                
                square = sudoku[:,a*3:(a+1)*3,b*3:(b+1)*3]  # das 3x3 Kaestchen wird erstellt
                for c in range(3):      # dann wird ueber die einzelnen Kaestchen im 3x3 Kaestchen
                    for d in range(3):  # iteriert
                        
                        if square[0,c,d] == 0:              # ist das Feld leer wird fortgefahren
                            compare = square[:,c,d]         # alle moeglichen Zahlen die in das Feld kommen koennen
                                                            # werden in die Liste compare geschrieben
                            num = check_list(compare[1:10]) # es wird gezaehlt wie viele Element in compare 
                                                            # ungleich Null sind
                            sims = 0                        # Diese Variable zaehlt, wie viele Felder aehnliche (gleiche)
                                                            # Listen von Moeglichkeiten haben wie compare
                            
                            coor = []                       # In diese Liste kommen die Koordinaten der Felder die 
                                                            # aehnlich zu compare sind
                            
                            elem = []                       # In diese Liste kommen die Element der Moeglichkeiten
                                                            # die bei compare und den anderen aehnlichen Listen ungleich
                                                            # Null sind
                            
                            for i in range(3):              # es wird nun erneut ueber die einzelnen Felder des
                                for j in range(3):          # 3x3 Kaestchens iteriert, um sie mit compare zu vergleichen
                                    if square[0,i,j] == 0:  # sie werden nur verglichen, wenn das Feld leer ist
                                        test = square[:,i,j]# erstellt vergleichs Liste
                                        if np.array_equal(compare, test) == True: # wenn copare und die Vergleichsliste
                                            sims = sims + 1                       # gleich sind, wird sims um 1 erhoeht
                                            coor.append((i,j))                    # und coor um die Koordinaten erweitert
                                             
                            if num == sims:                     # es wird ueberprueft ob die Zahl der Felder und
                                                                # der Moeglichkeiten uebereinstimmt 
                                
                                for k in range(10):             # zunaechst werden alle Moeglichkeiten in elem geschrieben
                                    if compare[k] != 0:
                                        elem.append(compare[k])
                                    
                                for i in range(3):     # es wird erneut ueber die Koordinaten iteriert
                                    for j in range(3):
                                        if (i,j) not in coor and square[0,i,j] == 0: # Es werden bei allen anderen Feldern
                                            for n in elem:                           # die Moeglichkeiten aus elem eleminiert
                                                sudoku[int(n),int((a*3)+i),int((b*3)+j)] = 0
        #########################################################################
        
        ### FORCE CHAIN #########################################################
        # Dieses Stueck Code behandelt den Fall wenn man nur mit den Informationen ueber die Moeglichkeiten nicht
        # mehr weiter kommt und deshalb auf Trail and Error zurueckgreifen muss. Dieses Stueck wird deshalb
        # nur aktiv wenn das Programm bereit einmal ohne veraenderung Durchlaufen ist.
        
        if run >= 2:
            for y in range(9):      # iteriert ueber alle Felder 
                for x in range(9):  #
                                          
                    if sudoku[0,y,x] == 0:       # ueberprueft ob ein leeres Feld 
                        reihe = sudoku[1:,y,x]   # nur noch zwei verschiedene 
                        trys = check_list(reihe) # Moeglichkeiten zum ausfuellen hat
                        if trys == 2:            #
                            
                            elem = []                     #
                            for t in range(9):            # Schreibt Moeglickeiten
                                if reihe[t] != 0:         # in Liste elem
                                    elem.append(reihe[t]) #
                                    
                            first_try = int(elem[0])      # erstes Element von elem wird zuerst ausprobiert
                            second_try = int(elem[1])     # zweites Element von elem wird danach ausprobiert
                            TE_sudoku = np.copy(sudoku)   # erstellt Kopie von Sudoku die weiterverwendet wird 
                            TE_sudoku = clues(TE_sudoku,first_try,x+1,y+1) # setzt first_try in die Kopie ein
                            result_one = SudokuSolve(TE_sudoku)  # versucht mit dieser Information erneut das Sudoku
                                                                 # zu loesen
                            
                            if result_one[0] == 'Zwei Lösungen': # stellt sich heraus, dass das Sudoku zwei oder mehr
                                return(result_one)               # Loesungen hat, kann dies ohne weitere Ueberpruefungen
                                                                 # zurueckgegeben werden. Ist dies nicht der Fall,
                                                                 # wenn hier die Antwort keine Loesung oder eine Loesung
                                                                 # ist, kann sich spaeter immernoch herausstellen,
                                                                 # dass es eigentlich doch eine oder sogar mehrere Loesungen
                                                                 # gibt
                            
                            TE_sudoku = np.copy(sudoku)                     # sudoku wird erneut kopiert, diesmal 
                            TE_sudoku = clues(TE_sudoku,second_try,x+1,y+1) # wird second_try eingesetzt
                            result_two = SudokuSolve(TE_sudoku)             # und auf Loesbarkeit untersucht

                            if result_one[0] == 'Zwei Lösungen' or result_two[0] == 'Zwei Lösungen':  # Hat das Sudoku zwei oder
                                return(['Zwei Lösungen',result_two[1]])                               # mehr Loesungen, wird
                                                                                                      # mit Ergebnis ausgegeben
                            
                            elif result_one[0] == result_two[0]:                                     
                                if result_one[0] == 'Eine Lösung':                   # Sind beide Ergebnisse, dass es eine Loesung gibt
                                    if np.array_equal(result_one[1], result_two[1]): # wird ueberprueft ob diese Loesungen gleich sind
                                        return(result_one)                           # Falls ja, wird diese Loesung als einzigen
                                                                                     # zurueckgegeben
                                    else:                                            # Falls nicht, wird zuruckgegeben dass es
                                        return('Zwei Lösungen',result_one[1])        # zwei Loesungen gibt, sowie eine Loesung wird ausgegeben
                                
                                elif result_one[0] == 'Keine Lösung':                # Sind beide Ergebnisse, dass es keine Loesung gibt,
                                    return(result_one)                               # So wird dies mit aktuellem Stand ausgegeben 
                            
                            
                            elif result_one[0] == 'Eine Lösung' and result_two[0] == 'Keine Lösung': # sollte nur eines der Ergebnisse eine
                                return(result_one)                                                   # Loesung aufweisen, wird diese ausgegeben
                                                                                                     #
                            else:                                                                    # 
                                return(result_two)                                                   #
                            
            
            # Fuer den seltenen Fall, dass es kein Feld mit zwei oder weniger Moeglichkeiten gibt,
            # wird das ganze Prozedere erneut durchgefuehrt, nur dieses Mal mit drei Moeglichkeiten
            for y in range(9):            # iteriert ueber alle Felder     
                for x in range(9):        #
                    
                    if sudoku[0,y,x] == 0:           # ueberprueft ob ein leeres Feld
                        reihe = sudoku[1:,y,x]       # nur noch zwei verschiedene
                        trys = check_list(reihe)     # Moeglichkeiten zum ausfuellen hat
                        if trys == 3:                #
                            
                            elem = []                      #
                            for t in range(9):             # Schreibt Moeglickeiten
                                if reihe[t] != 0:          # in Liste elem
                                    elem.append(reihe[t])  #
                                    
                            first_try = int(elem[0])       # erstes Element von elem wird zuerst ausprobiert
                            second_try = int(elem[1])      # zweites Element von elem wird danach ausprobiert
                            third_try = int(elem[2])       # drittes Element von elem wird danach ausprobiert
                            TE_sudoku = np.copy(sudoku)    # erstellt Kopie von Sudoku die weiterverwendet wird
                            TE_sudoku = clues(TE_sudoku,first_try,x+1,y+1)  # setzt first_try in die Kopie ein
                            result_one = SudokuSolve(TE_sudoku)   # versucht mit dieser Information erneut das Sudoku
                                                                  # zu loesen
                            if result_one[0] == 'Zwei Lösungen':  # stellt sich heraus, dass das Sudoku zwei oder mehr
                                return(result_one)                # Loesungen hat, kann dies ohne weitere Ueberpruefungen
                                                                  # zurueckgegeben werden. Ist dies nicht der Fall,
                                                                  # wenn hier die Antwort keine Loesung oder eine Loesung
                                                                  # ist, kann sich spaeter immernoch herausstellen,
                                                                  # dass es eigentlich doch eine oder sogar mehrere Loesungen
                                                                  # gibt
                                                
                            TE_sudoku = np.copy(sudoku)                     # sudoku wird erneut kopiert, diesmal
                            TE_sudoku = clues(TE_sudoku,second_try,x+1,y+1) # wird second_try eingesetzt
                            result_two = SudokuSolve(TE_sudoku)             # und auf Loesbarkeit untersucht
                            
                            if result_two[0] == 'Zwei Lösungen':  # stellt sich heraus, dass das Sudoku zwei oder mehr
                                return(result_two)                # Loesungen hat, kann dies ohne weitere Ueberpruefungen
                                                                  # zurueckgegeben werden. Ist dies nicht der Fall,
                                                                  # wenn hier die Antwort keine Loesung oder eine Loesung
                                                                  # ist, kann sich spaeter immernoch herausstellen,
                                                                  # dass es eigentlich doch eine oder sogar mehrere Loesungen
                                                                  # gibt
                                                
                            TE_sudoku = np.copy(sudoku)                    # sudoku wird erneut kopiert, diesmal
                            TE_sudoku = clues(TE_sudoku,third_try,x+1,y+1) # wird third_try eingesetzt
                            result_three = SudokuSolve(TE_sudoku)          # und auf Loesbarkeit untersucht
                            
                            results = [result_one[0], result_two[0], result_three[0]] # alle Ergebnisse werden in eine Liste 
                                                                                      # geschrieben
                            ones = []                                                 # in diese Variable kommen die Nummern
                                                                                      # der Ergebnisse die eine Loesung haben
                            
                            if 'Zwei Lösungen' in results:                            # Ist eine Loesung, dass es zwei  
                                if result_one[0] == 'Zwei Lösungen':                  # Loesungen gibt, wird dies zusammen
                                    return(['Zwei Lösungen',result_one[1]])           # mit einer moeglichen Loesung ausgegeben
                                
                                elif result_two[0] == 'Zwei Lösungen':
                                    return(['Zwei Lösungen',result_two[1]])
                                
                                else:
                                    return(['Zwei Lösungen',result_three[1]])
                                
                            
                            elif 'Eine Lösung' in results:                            # hier wird ueberprueft, ob ein Ergebnis ist,
                                for n in range(2):                                    # das es eine Loesung gibt.
                                    if results[n] == 'Eine Lösung':                   # Ist es nur eine der Loesungen, wird diese
                                        ones.append(n)                                # ausgegeben.
                                                                                      # Ergeben jedoch mehrere Ergebnisse,
                                if len(ones) == 1:                                    # dass es eine Loesung gibt,
                                    if ones[0] == 0:                                  # wird ueberprueft ob sie zum selben Ergebnis
                                        return(result_one)                            # komme, falls ja, wird dieses als einziges 
                                    elif ones[0] == 1:                                # ausgegeben. Falls nicht,
                                        return(result_two)                            # wird eine Loesung und die Information, dass
                                    else:                                             # es zwei Loesungen gibt ausgegeben.
                                        return(result_three)
                                
                                elif len(ones) == 2:
                                    if 0 in ones:
                                        if 1 in ones:
                                            if np.array_equal(result_one[1], result_two[1]) == True:
                                                return(result_one)
                                            else:
                                                return(['Zwei Lösungen',result_one[1]])
                                        else:
                                            if np.array_equal(result_one[1], result_three[1]) == True:
                                                return(result_one)
                                            else:
                                                return(['Zwei Lösungen',result_one[1]])
                                    else:
                                        if np.array_equal(result_two[1], result_three[1]) == True:
                                            return(result_two)
                                        else:
                                            return(['Zwei Lösungen',result_two[1]])
                                        
                                else:
                                    if np.array_equal(result_one[1], result_two[1]) == True:
                                        if np.array_equal(result_one[1], result_three[1]) == True:
                                            return(result_one)
                                        else:
                                            return(['Zwei Lösungen',result_one[1]])
                                        
                                    else:
                                        return(['Zwei Lösungen',result_one[1]])
                                    
                            else:                    # Falls alle Ergebnisse sind, dass es keine Loesung gibt, so wird dieses ausgegeben
                                return(result_one)
                            
                            
            return(['Zwei Lösungen',sudoku])   # sollte es dau kommen, dass es keine Felder mit drei oder weniger
                                               # Moeglichkeiten gibt, so wird einfach ausgegeben, dass das Sudoku mehrere
                                               # Loesungen hat, denn um dies zu erreichen, muss das Sudoku eindeutig
                                               # weniger als 17 Hinweise haben, die aber notwendig sind, damit das sudoku
                                               # eindeutig loesbar sein koennte
        #########################################################################
        
        ### LAST CHECK ##########################################################
        # Hier wird das Sudoku geprueft, ist es geloest, wird die while-Schleife verlassen
        solvable = sudoku_solvable(sudoku)
        solved = check_sudoku(sudoku)
        if solvable == True and solved == True:
            break
        #########################################################################
        # Noch in while True
    # Ende von while True:
    return(['Eine Lösung',sudoku])   # Ist das Sudoku geloest, wird es ausgegeben
    
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