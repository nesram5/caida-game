import random
import time
import os

nombre_carta = (
					('Uno de picas'),
					('Dos de picas'),
					('Tres de picas'),
					('Cuatro de picas'),
					('Cinco de picas'),
					('Seis de picas'),
					('Siete de picas'),
					('Diez de picas'),
					('Once de picas'),
					('Doce de picas'),
					('Uno de bastos'),
					('Dos de bastos'),
					('Tres de bastos'),
					('Cuatro de bastos'),
					('Cinco de bastos'),
					('Seis de bastos'),
					('Siete de bastos'),
					('Diez de bastos'),
					('Once de bastos'),
					('Doce de bastos'),
					('Uno de copas'),
					('Dos de copas'),
					('Tres de copas'),
					('Cuatro de copas'),
					('Cinco de copas'),
					('Seis de copas'),
					('Siete de copas'),
					('Diez de copas'),
					('Once de copas'),
					('Doce de copas'),
					('Uno de monedas'),
					('Dos de monedas'),
					('Tres de monedas'),
					('Cuatro de monedas'),
					('Cinco de monedas'),
					('Seis de monedas'),
					('Siete de monedas'),
					('Diez de monedas'),
					('Once de monedas'),
					('Doce de monedas')
				)
valor_carta = (1,2,3,4,5,6,7,10,11,12,1,2,3,4,5,6,7,10,11,12,1,2,3,4,5,6,7,10,11,12,1,2,3,4,5,6,7,10,11,12)

#revolver_cartas
maso_revuelto = random.sample(range(0,40),40)

#Definir variables
mesa = []
mesa_valor = []
jug1 = []
jug2 = []
jug3 = []
jug4 = []
maso_jugador1 = 0
maso_jugador2 = 0
maso_jugador3 = 0
maso_jugador4 = 0
pts1 = 0
pts2 = 0
pts3 = 0
pts4 = 0
canto_jug1 = [0,0,0,0]
canto_jug2 = [0,0,0,0]
canto_jug3 = [0,0,0,0]
canto_jug4 = [0,0,0,0]


id_player = 0 #identidad del ultimo en agarrar cartas

bak_valor_ultima_carta = 0 #Respaldo para hacer caida
#############################################################################################################################
def agregar_a_mesa(carta, turno_id):
    
    global bak_valor_ultima_carta, ultimo_dejar_carta_mesa_id, mesa, mesa_valor, ultimo_agarrar_carta_id, pts1, pts2, pts3, pts4
   
    maso = 0
    newlist = [] # empty list to hold unique elements from the list
    index = 0
    
    mesa.append(carta)
    #crear tabla mesa con solo valores de carta
   
    mesa_a_valor()
    
    #Buscar duplicados y Eliminar duplicados de ambas mesas    
    k=0
    dup = 0

    for k in mesa_valor:
           if k not in newlist:
                newlist.append(k)
           else:
               dup = k #bak duplicado
               index = mesa_valor.index(k) #return index
               del mesa[index] #Borar elemento duplicado de mesa
               mesa_valor.remove(k)
               ultimo_agarrar_carta_id= turno_id
               maso = maso + 1
            
    if dup != 0:        
        index = mesa_valor.index(dup)
        del mesa[index] #Borar elemento duplicado de mesa
        mesa_valor.remove(dup)
        maso = maso + 1
        
    if maso >= 2:  
            
            if dup != 7:
                dup = dup + 1
            else:
                dup = dup + 3 #Si la carta es 7 le sigue el 10
           
            k = 0
            j = 0
            while True:
                             
                for i in mesa_valor:
                    if dup == i:
                        index = mesa_valor.index(i) #return index
                        del mesa[index] #Borar elemento duplicado de mesa
                        mesa_valor.remove(i)
                        maso = maso + 1
                        if dup != 7:
                            dup = dup + 1
                        else:
                            dup = dup + 3 #Si la carta es 7 le sigue el 10
                        
                  
                if dup not in mesa_valor:
                    break
    else:
        if maso == 0:
           bak_valor_ultima_carta = mesa_valor[-1]
           ultimo_dejar_carta_mesa_id = turno_id
           return int(maso)
    
    if len(mesa) == 0:
        print(f"El jugador{turno_id} ha hecho 4 en mesa +4 pts")
        if turno_id == 1:
            pts1 = pts1 + 4
        elif turno_id == 2:
            pts2 = pts2 + 4
        elif turno_id == 2:
            pts3 = pts3 + 4
        elif turno_id == 2:
            pts3 = pts3 + 4               
    return int(maso)

def mesa_a_valor():
    
    mesa_valor.clear()

    i = 0
    for j in mesa:
        mesa_valor.insert(i,valor_carta[j])
        i = i + 1
        
mesa = [0,1]
maso = agregar_a_mesa(10, 1)
print (mesa)
print (maso)
print (pts1)
