##coding=UTF8
import random
def controllovincita(tipoGriglia,lista):
        contatore1=0
        contatore2=1
        somma=0


#controllo per righe
        while contatore1<=tipoGriglia*contatore2:
                if somma==3:
                        return "Croce ha vinto!"
                if somma==30:
                        return "Cerchio ha vinto!"

                if contatore1==tipoGriglia*contatore2+1:                  #se è finita la riga
                        somma=0                                         #resetta la variabile somma
                        contatore2=contatore2+1                         #e passa alla riga successiva

                if tipoGriglia*tipoGriglia<=tipoGriglia*contatore2:      #se la griglia è terminata
			break			                         #passa al controllo successivo
                somma=somma+lista[contatore1]

                contatore1=contatore1+1                                 #incremento contatore1 per controllare la casella successiva


#controllo per colonne
        contatore1=0	#resetto i contatori
        contatore2=1    #per poterli riutilizzare
    
        while contatore1<=tipoGriglia*tipoGriglia:
            if somma==3:
                        return "Croce ha vinto!"
            if somma==30:
                        return "Cerchio ha vinto!"
                        
            if contatore1==tipoGriglia*tipoGriglia:                  	#se è finita la colonna
                        print somma                                   #usato per debug, non necessario una volta risolti i problemi
			somma=0                                                         #resetta la variabile somma
			contatore1=contatore2                                         
                        contatore2=contatore2+1                     #e passa alla colonna successiva
                        
            if tipoGriglia*tipoGriglia<=contatore2*contatore2:      #se la griglia è terminata
                        return "Nessun vincitore :( "                   #nessuno ha vinto
            somma=somma+lista[contatore1]
            contatore1=contatore1+tipoGriglia                                 #incremento contatore1 per controllare la casella successiva
	print "uscito"                                                       #usato per debug, non necessario una volta risolti i problemi

#controllo prima diagonale (angolo in alto sx-->in basso dx)
#	contatore1=0		#resetto i contatori
#	contatore2=0		#per poterli riutilizzare
#
#	while contatore1<=tipoGriglia*contatore2:
#		if somma==3:
#                        return "Croce ha vinto!"
#            	if somma==30:
#                        return "Cerchio ha vinto!"
#		if 




def mossarandom(tipoGriglia,giocatore,lista):		#fa fare mosse casuali al giocatore ma se la griglia è piena non termina mai
	if giocatore=='x':
		 valore=1
	if giocatore=='cerchio':
		 valore=10
	while(1):
		indicecasuale=random.randint(0,tipoGriglia*tipoGriglia -1)
		if lista[indicecasuale]!=1 and lista[indicecasuale]!=10:	#una volta trovata una casella vuota la riempie ed esce
			lista[indicecasuale]=valore
			break
			
			
def ia(tipoGriglia,lista):		#fa fare mosse "intelligenti" alla X ma se la griglia è piena non termina mai (perchè richiama mossarandom())

        contatore1=0
        contatore2=1
        somma=0
	contatoreduplicato1=0
	contatoreduplicato2=1


#controllo per righe
        while contatore1<=tipoGriglia*contatore2:
		if somma==20:
                        contatoreduplicato1=contatore1
                        contatoreduplicato2=contatore2
                        while (contatoreduplicato1<tipoGriglia*contatoreduplicato2):
                                if lista[contatoreduplicato1]!=10:
                                        lista[contatoreduplicato1]=1
                                contatoreduplicato1=contatoreduplicato1+1
                        contatoreduplicato1=contatore1                  #resetto le variabili
                        conatoreduplicato2=contatore2                   #per riutilizza
       
                if somma==2:
			contatoreduplicato1=contatore1
			contatoreduplicato2=contatore2
                        while contatoreduplicato1<tipoGriglia*contatoreduplicato2:
				if lista[contatoreduplicato1]!=1:
					lista[contatoreduplicato1]=1
				contatoreduplicato1=contatoreduplicato1+1
			contatoreduplicato1=contatore1			#resetto le variabili
			contatoreduplicato2=contatore2			#per riutilizzarle
                        

                if contatore1==tipoGriglia*contatore2:                  #se è finita la riga
                        somma=0                                         #resetta la variabile somma
                        contatore2=contatore2+1                         #e passa alla riga successiva

                if tipoGriglia*tipoGriglia<=tipoGriglia*contatore2:      #se la griglia è terminata
                        break			                        #passo al controllo successivo
                somma=somma+lista[contatore1]

                contatore1=contatore1+1                                 #incremento contatore1 per controllare la casella successiva


#controllo per colonne
        contatore1=0    #resetto i contatori
        contatore2=1    #per poterli riutilizzare
	contatoreduplicato1=0
        contatoreduplicato2=1


        while contatore1<=tipoGriglia*contatore2:
	    if somma==20:
                       contatoreduplicato1=contatore1
                       contatoreduplicato2=contatore2
                       while (contatoreduplicato1<tipoGriglia*contatoreduplicato2):
                                if lista[contatoreduplicato1]!=10:
                                        lista[contatoreduplicato]=1
                                contatoreduplicato1=contatoreduplicato1+1
                       contatoreduplicato1=contatore1                  #resetto le variabili
                       conatoreduplicato2=contatore2                   #per riutilizza
            if somma==2:
                       contatoreduplicato1=contatore1
                       contatoreduplicato2=contatore2
                       while (contatoreduplicato1<tipoGriglia*contatoreduplicato2):
                                if lista[contatoreduplicato1]!=1:
                                        lista[contatoreduplicato]=1
		       		contatoreduplicato1=contatoreduplicato1+1
                       contatoreduplicato1=contatore1                  #resetto le variabili
                       contatoreduplicato2=contatore2                  #per riutilizzarle



            if contatore1==tipoGriglia*contatore2:                      #se è finita la colonna
 			somma=0                                         #resetta la variabile somma
                        contatore2=contatore2+1                         #e passa alla colonna successiva 
                        if tipoGriglia*tipoGriglia<tipoGriglia*contatore2:      #se la griglia è terminata
                            mossarandom(tipoGriglia,'x',lista)                    #fa una mossa casuale
                            break						 #ed esce
	    somma=somma+lista[contatore1]
            contatore1=contatore1+tipoGriglia                                 #incremento contatore1 per controllare la casella successiva

	

