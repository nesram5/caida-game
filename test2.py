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

def repartir_mesa():
    global mesa_valor, mesa
    """"i = 0
    while i <= 3 :
        mesa.insert(i,maso_revuelto[i])
        i = i +1
    """
    
    #crear tabla mesa con solo valores de carta
    mesa_a_valor()
        
    newlist = [] 
    dup = 0
           
    
    for j in mesa_valor:
        if j not in newlist:
            newlist.append(j)
        else:
            dup = j # this method catches the first duplicate entries, and appends them to the list
    #Eliminar duplicados de ambas mesas
    if dup > 0:
        index_carta_dup = mesa_valor.index(dup)#Indice en mesa_valor
        copia_carta_dup = mesa[index_carta_dup]# Respaldo valor carta
        del(mesa_valor[index_carta_dup])
        del(mesa[index_carta_dup])
    
        
        #Escoger carta de reemplazo y confirmar que su valor no sea igual al resto
        while True:
            replace_carta = random.randint(4, 39)
            valor_replace_carta = valor_carta[replace_carta]
            if valor_replace_carta in mesa_valor:
                continue
            else:
                 break
           
                #Fin comprobacion
                
        mesa.append(replace_carta)
        
        maso_revuelto[replace_carta] = copia_carta_dup #Reemplazo de carta dup
       
        mesa_a_valor() #Actualizar mesa_valor
            
def mostrar_mesa():
    print("                     ")
    print("Cartas en la mesa")
    print("                     ")
    print("---------------------")
       
    for i in mesa:
        print("·", "(",valor_carta[i],")", nombre_carta[i])
        
    print("---------------------")

def mesa_a_valor():
    
    mesa_valor.clear()

    i = 0
    for j in mesa:
        mesa_valor.insert(i,valor_carta[j])
        i = i + 1
        
mesa = [0, 10, 12, 14]
repartir_mesa()
mostrar_mesa()
