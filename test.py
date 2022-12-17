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
def mano_a_valor(mano):
    i = 0
    mano_valor = []
    
    for j in mano:
        mano_valor.insert(i,valor_carta[j])
        i = i + 1
    return mano_valor

#Funcion Comprobar Canto
def comprobar_canto_jug(cartas_jug, turno_id):
    
    cartas_jug_valor = mano_a_valor(cartas_jug)
    pts_canto = 0
    canto = [0,0,0,0]
    
    #Llamada a patrulla
    canto, pts_canto = patrulla(cartas_jug_valor, turno_id)
    
    #Llamada a Registro
    if canto[0] == 0:
        canto, pts_canto = registro(cartas_jug_valor, turno_id)
        
    #Llamada a ronda_vigia_tribilin
    if canto[0] == 0:
        canto, pts_canto = ronda_vigia_tribilin(cartas_jug_valor, turno_id)
    
    return canto

#Funcion Ronda_Vigia_Tribilin    
def ronda_vigia_tribilin(cartas_jug_valor, turno_id):
    
    pts_canto = 0
    canto = [0,0,0,0]
    
    cartas_jug_valor.sort()
    
    valor_carta_canto = 0
    #Comprobar tribilin
    if cartas_jug_valor[0] == cartas_jug_valor[1] and cartas_jug_valor[0] == cartas_jug_valor[2] and cartas_jug_valor[1] == cartas_jug_valor[2]:
        pts_canto = 24
        nombre_canto = 'Triblin mata partida'
        i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
        canto = [pts_canto,i,turno_id,nombre_canto]
        print(f"Jugador{turno_id} tiene {nombre_canto}")
        return canto, pts_canto
    
    #Comprobar vigia
    if cartas_jug_valor[0] == cartas_jug_valor[1] or cartas_jug_valor[1] == cartas_jug_valor[2]:
        
        if cartas_jug_valor[0] == cartas_jug_valor[1]:
            valor_carta_canto = cartas_jug_valor[0]
            index_carta_canto = 0
        
        elif cartas_jug_valor[1] == cartas_jug_valor[2]:
            valor_carta_canto = cartas_jug_valor[1]
            index_carta_canto = 1
        
        valor_carta_canto_mas = valor_carta_canto + 1
        valor_carta_canto_menos = valor_carta_canto - 1
        
        if index_carta_canto == 0:
            if valor_carta_canto_mas == cartas_jug_valor[2]:
                pts_canto = 7
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Vigia'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"Jugador{turno_id} tiene {nombre_canto}")
                return canto, pts_canto
            
        elif index_carta_canto == 1:
            if valor_carta_canto_mas == cartas_jug_valor[0]:
                pts_canto = 7
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Vigia'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"Jugador{turno_id} tiene {nombre_canto}")
                return canto, pts_canto
             
        elif index_carta_canto == 0:
            if valor_carta_canto_menos == cartas_jug_valor[2]:
                pts_canto = 7
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Vigia'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"Jugador{turno_id} tiene {nombre_canto}")
                return canto, pts_canto
            
        elif index_carta_canto == 1:
            if valor_carta_canto_menos == cartas_jug_valor[0]:
                pts_canto = 7
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Vigia'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"Jugador{turno_id} tiene {nombre_canto}")
                return canto, pts_canto
                
        #Si no es vigia Comprobando pts de la ronda
        if canto[0] == 0 and valor_carta_canto > 0:   
            if valor_carta_canto >= 1 and valor_carta_canto <= 7:
                pts_canto = 1
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Ronda'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"Jugador{turno_id} tiene {nombre_canto}")
                return canto, pts_canto
            
            elif valor_carta_canto == 10:
                pts_canto = 2
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Ronda'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"Jugador{turno_id} tiene {nombre_canto}")
                return canto, pts_canto 
            
            elif valor_carta_canto == 11:
                pts_canto = 3
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Ronda'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"Jugador{turno_id} tiene {nombre_canto}")
                return canto, pts_canto
           
            elif valor_carta_canto == 12:
                pts_canto = 4
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Ronda'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"Jugador{turno_id} tiene {nombre_canto}")
                return canto, pts_canto
    #No hay ronda_vigia_tribilin
    else:
        return canto, pts_canto
        
    
#Funcion Patrulla
def patrulla(cartas_jug_valor, turno_id):
    pts_canto = 0
    canto = [0,0,0,0]
    
    cartas_jug_valor.sort()
    
    carta_1 = cartas_jug_valor[1]
    carta_0 = carta_1 - 1
    carta_2 = carta_1 + 1
    
    if carta_0 == cartas_jug_valor[0] and carta_2 == cartas_jug_valor[2]:
        pts_canto = 6
        i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
        nombre_canto = 'Patrulla'
        canto = [pts_canto,i,turno_id,nombre_canto]
        print(f"Jugador{turno_id} tiene {nombre_canto}")
        return canto, pts_canto
    else:
        return canto, pts_canto

#Funcion Registro
def registro(cartas_jug_valor, turno_id):
    pts_canto = 0
    canto = [0,0,0,0]
    
    cartas_jug_valor.sort()
    
    if cartas_jug_valor[0] == 1 and cartas_jug_valor[1] == 11 and cartas_jug_valor[2] == 12:
        pts_canto = 12
        i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
        nombre_canto = 'Registro'
        canto = [pts_canto,i,turno_id,nombre_canto]
        print(f"Jugador{turno_id} tiene {nombre_canto}")
        return canto, pts_canto
    else:#No hay registro
        return canto, pts_canto
    
#Canto Ganador o Mayor   
def canto_mayor(repartidor):
    global canto_jug1, canto_jug2, canto_jug3, canto_jug4
    
    #Comprobacion por pts de canto
    
    orden_pts = [canto_jug1[0], canto_jug2[0], canto_jug3[0], canto_jug4[0]]
    orden_sumvalor = [canto_jug1[1], canto_jug2[1], canto_jug3[1], canto_jug4[1]]
    orden_id = [canto_jug1[2], canto_jug2[2], canto_jug3[2], canto_jug4[2]]
    orden_nombre_canto = [canto_jug1[3], canto_jug2[3], canto_jug3[3], canto_jug4[3]]
    pts = 0
    id_ganador = 0
    
    #Buscar puntuaje mas alto
   
    max_pts = max(orden_pts)
    
    #Buscar si hay otro canto del mismo puntuaje
    dup = 0
    for i in orden_pts:
        if max_pts == i:
            dup = dup + 1
    
    if dup == 1:
        j = orden_pts.index(max_pts)
        id_ganador = j + 1
        nombre_canto = orden_nombre_canto[j]
        pts = max_pts #Sumar pts al ganador
        print(f"El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts")
        return pts, id_ganador
    elif dup == 2:
        #Hay 2 jugadores con el mismo canto se elige el ganador por la suma de las 3 cartas
        max_sumvalor = max(orden_sumvalor)
        #comprobar que la suma de cartas no sea igual a la del 2do jug
        dup = 0
        for i in orden_pts:
            if max_sumvalor == i:
                dup = dup + 1
        if dup == 0:
            j = orden_sumvalor.index(max_sumvalor)
            id_ganador = j + 1
            nombre_canto = orden_nombre_canto[j]
            pts = max_pts #Sumar pts al ganador
            print(f"El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts")
            return pts, id_ganador
        else:
        #Hay 2 jug con el mismo canto y la misma suma de cartas
        #Desenpate por posicion con respecto al repartidor
            rep = repartidor + 1
            orden_id.append(rep)
            orden_id.sort()
            
            #Eliminar ceros de la lista
            k = 0
            while k <= len(orden_id):
                for i in orden_id:
                    if i == 0:
                        orden_id.remove(0)
                k = k + 1
            #Eliminar duplicados       
            newlist = []
            dup = 0
            for i in orden_id:
                if i not in newlist:
                    newlist.append(i)
                else:
                    dup = i
            #Si no hay duplicados y el rep es menor a posicion 3
            if dup == 0 and rep <= 3:
                id_ganador = orden_id[-1]
                j = id_ganador - 1
                nombre_canto = orden_nombre_canto[j]
                pts = max_pts #Sumar pts al ganador
                print(f"El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts")
                return pts, id_ganador
            elif dup == rep: #Si uno de los jugadores es el repartidor pero no es posicion 4
                
                orden_id.remove(rep)
                if rep == orden_id[0]:
                    id_ganador = orden_id[-1]
                    j = id_ganador - 1
                    nombre_canto = orden_nombre_canto[j]
                    pts = max_pts #Sumar pts al ganador
                    print(f"El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts")
                    return pts, id_ganador
                else:
                    id_ganador = orden_id[0]
                    j = id_ganador - 1
                    nombre_canto = orden_nombre_canto[j]
                    pts = max_pts #Sumar pts al ganador
                    print(f"El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts")
                    return pts, id_ganador
                    
    return pts, id_ganador #no hubo cantos      
    




