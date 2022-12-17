from random import sample, randint, choice
from os import system
from time import sleep
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
maso_revuelto = sample(range(0,40),40)

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
equipo1_pts = 0
equipo2_pts = 0
ultimo_dejar_carta_mesa_id = 0 #identidad del ultimo en dejar carta en mesa
ultimo_agarrar_carta_id =  0 #identidad del ultimo en agarrar cartas
bak_valor_ultima_carta = 0 #Respaldo para hacer caida
nombre_jug1 = ''

#############################################################################################################################

#Funcion Cambio de mesa a mesa_valor
def mesa_a_valor():
    
    mesa_valor.clear()

    i = 0
    for j in mesa:
        mesa_valor.insert(i,valor_carta[j])
        i = i + 1

#Funcion Repartir Mesa
def repartir_mesa():
    global mesa_valor, mesa
    i = 0
    while i <= 3 :
        mesa.insert(i,maso_revuelto[i])
        i = i +1
    
    
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
            
            replace_carta = randint(4, 39)
            valor_replace_carta = valor_carta[replace_carta]
            
            if valor_replace_carta in mesa_valor:
                
                continue
            
            else:
                
                 break
           
                #Fin comprobacion
                
        mesa.append(replace_carta)
        
        maso_revuelto[replace_carta] = copia_carta_dup #Reemplazo de carta dup
       
        mesa_a_valor() #Actualizar mesa_valor
        

#Funcion Repartir cartas a jugadores
def repartir_jug(i):

        jug1.insert(0,maso_revuelto[i])
        i=i+1
        jug1.insert(1,maso_revuelto[i])
        i=i+1
        jug1.insert(2,maso_revuelto[i])
        i=i+1
        jug2.insert(0,maso_revuelto[i])
        i=i+1
        jug2.insert(1,maso_revuelto[i])
        i=i+1
        jug2.insert(2,maso_revuelto[i])
        i=i+1
        jug3.insert(0,maso_revuelto[i])
        i=i+1
        jug3.insert(1,maso_revuelto[i])
        i=i+1
        jug3.insert(2,maso_revuelto[i])
        i=i+1
        jug4.insert(0,maso_revuelto[i])
        i=i+1
        jug4.insert(1,maso_revuelto[i])
        i=i+1
        jug4.insert(2,maso_revuelto[i])
  

#Funcion ronda 
def ronda(cuenta_ronda):
    
    if cuenta_ronda == 1:
        
        repartir_jug(4)
        
    elif cuenta_ronda == 2:
        
        repartir_jug(16)
        
    elif cuenta_ronda == 3:
        
        repartir_jug(28)       

#Funcion Elegir Repartidor
def elegir_repartidor():
    
    global nombre_carta, valor_carta, nombre_jug1
    baraja_repartidor = []
    baraja_repartidor_valor = []
    maso_revuelto = sample(range(0,40),40)
    
    i=0
    
    while i <= 3:
        
        for j in maso_revuelto:
            
            aux = valor_carta[j]
            
            if aux not in baraja_repartidor_valor:
                
                baraja_repartidor.append(j)
                baraja_repartidor_valor.append(aux)
                
                if i <=2:
                    
                    i+=1
                    
                else:
                    
                    break
                
        if i == 3:
            
            break
    
    copy_baraja_repartidor_valor = baraja_repartidor_valor.copy()
    copy_baraja_repartidor_valor.sort()
    carta_alta = copy_baraja_repartidor_valor[-1]
    index = baraja_repartidor_valor.index(carta_alta)
    num_carta = baraja_repartidor[index] 
    
   
    while True:
        
        try:
            
            system('cls')
            print("")
            print("###############################################################################")
            print("#                                                                             #")
            print("#                                                                             #")
            print("#                  Elige un numero del 1 al 4 y pulsa Enter:                  #")
            print("#                                                                             #")
            print("#                                                                             #")
            print("###############################################################################")
            print(" ")
            opcion = int(input("                                      "))

            if opcion == 1:
                
                list_id = ['el Jugador 1','el Jugador 2', 'el Jugador 3', 'el Jugador 4']
                list_id[0] = nombre_jug1
                list_id2 = [0,1,2,3]
                break
            
            elif opcion == 2:
                
                list_id = ['el Jugador 4','Jugador 1','el Jugador 2', 'el Jugador 3' ]
                list_id[1] = nombre_jug1
                list_id2 = [3,0,1,2]
                break
            
            elif opcion == 3:
                
                list_id = ['el Jugador 3','el Jugador 4','Jugador 1','el Jugador 2' ]
                list_id[2] = nombre_jug1
                list_id2 = [2,3,0,1]
                break
            
            elif opcion == 4:
                
                list_id = ['el Jugador 2','el Jugador 3','el Jugador 4','el Jugador 1', ]
                list_id[3] = nombre_jug1
                list_id2 = [1,2,3,0]
                break
            
        except:
            
            continue
    opcion = opcion - 1
    
    if opcion == index:
        
        id_ganador = list_id2[opcion]
        
    else:
        
        id_ganador = list_id2[index]

    
    i=0
    
    while i <= 4:
        
        system('cls')    
        print("")
        print("###############################################################################")
        print("")                                                                    
        print("")
        
        print(f"        1.-({valor_carta[baraja_repartidor[0]]}) {nombre_carta[baraja_repartidor[0]]}        ")
            
        if i>=1:
            
            print(f"        2.-({valor_carta[baraja_repartidor[1]]}) {nombre_carta[baraja_repartidor[1]]}        ")
            
        if i>=2:
            
            print(f"        3.-({valor_carta[baraja_repartidor[2]]}) {nombre_carta[baraja_repartidor[2]]}        ")
            
        if i>=3:
            
            print(f"        4.-({valor_carta[baraja_repartidor[3]]}) {nombre_carta[baraja_repartidor[3]]}        ")
            
        if i>=4:
            
            print("______________________________________________________________________________")
            print("")
            print(f"   El repartidor sera {list_id[index]} con la carta alta ({carta_alta}) {nombre_carta[num_carta]}")
            print("")
            print("______________________________________________________________________________")

            print("")
            print("")
            print("###############################################################################")
        i += 1
        sleep(1)
        
    print("")
    print("Pulse Enter para continuar")
    input()
    return id_ganador
    
#Funcion incrementear letra   
def incrementar_letra(letra):
    
    return chr(ord(letra)+1)

#Funcion Mostrar mesa
def mostrar_mesa():
    
    global mesa
    system('cls')
    banner_pts()
    print("###############################################################################")
    print("#                                                                             #")
    print("#                                  Cartas                                     #")
    print("#                                en la mesa                                   #")
    print("#                                                                             #")
    print("###############################################################################")
       
    for i in mesa:
        
        print(f"         · ({valor_carta[i]})  {nombre_carta[i]}                         ")
    
    
#Funcion Mostrar cartas Jug 1
def mostrar_cartas():
    
    global jug1
    print("")
    print("                           Estas son tus cartas                               ")
    print("")
    letra = 'a'
    for i in jug1:
        
          print(" ",letra, ".", "(",valor_carta[i],")", nombre_carta[i])
          letra = incrementar_letra(letra)
          
#Funcion Mecanica de Juego
def juego(repartidor):
    
    global pts1, pts2, pts3, pts4, canto_jug1, canto_jug2, canto_jug3, canto_jug4, nombre_jug1
    
    cuenta_ronda = 1
    
    while cuenta_ronda <= 3:
        
        ronda(cuenta_ronda)
        pasada = 0
        if repartidor == 0:
                        
            while pasada <= 2:
                
                if pasada == 0:
                    
                    ronda_splash(cuenta_ronda)
                    
                mostrar_mesa()
                print("")
                print(" Pulsa Enter para continuar...") 
                input()
                system('cls')
                print(" ")
                print("                               Turno Jugador 2                            ")
                print(" ")         
                turno_cpu(2)
                mostrar_mesa()
                print(" ")
                print("                               Turno Jugador 3                            ")
                print(" ")
                turno_cpu(3)
                mostrar_mesa()
                print(" ") 
                print("                               Turno Jugador 4                            ")
                print(" ")                 
                turno_cpu(4)
                system('cls')
                mostrar_mesa()
                print(" ")
                print("                                Turno {nombre_jug1}                            ")
                print(" ")
                turno_jug1()
                system('cls')
                mostrar_mesa()
                ganador_en_juego = revisar_pts()
                
                if ganador_en_juego == True:
                    
                    return ganador_en_juego
                
                else:
                    
                    pasada = pasada + 1
                    pts, id_ganador = canto_mayor(repartidor)
                    if id_ganador == 1:
                        
                        pts1 = pts1 + pts
                        
                    elif id_ganador == 2:
                        
                        pts2 = pts2 + pts
                        
                    elif id_ganador == 3:
                        
                        pts3 = pts3 + pts
                        
                    elif id_ganador == 4:
                        
                        pts4 = pts4 + pts
                        
                    cuenta_ronda = cuenta_ronda + 1
                    print(" Pulsa Enter para continuar...") 
                    input()
                    if cuenta_ronda != 4:
                        
                        ronda_splash(cuenta_ronda)
            
        elif repartidor == 1:
            
            while pasada <= 2:
                
                if pasada == 0:
                    
                    ronda_splash(cuenta_ronda)
                    
                mostrar_mesa()
                print("")
                print(" Pulsa Enter para continuar...") 
                input()
                print(" ")
                print("                              Turno Jugador 3                            ")
                print(" ")
                turno_cpu(3)
                mostrar_mesa()
                print(" ")
                print("                              Turno Jugador 4                            ")
                print(" ")                
                turno_cpu(4)
                system('cls')
                mostrar_mesa()
                 #Mostrar Cartas Jugador 1
                print(" ")
                print("                              Turno {nombre_jug1}                            ")
                print(" ")
                turno_jug1()
                system('cls')
                mostrar_mesa()
                print(" ")
                print("                              Turno Jugador 2                            ")
                print(" ")
                turno_cpu(2)
                mostrar_mesa()
                ganador_en_juego = revisar_pts()
                if ganador_en_juego == True:
                    
                    return ganador_en_juego
                
                else:
                    
                    pasada = pasada + 1
                    
                if pasada == 3:
                    
                    pts, id_ganador = canto_mayor(repartidor)
                    
                    if id_ganador == 1:
                        
                        pts1 = pts1 + pts
                        
                    elif id_ganador == 2:
                        
                        pts2 = pts2 + pts
                        
                    elif id_ganador == 3:
                        
                        pts3 = pts3 + pts
                        
                    elif id_ganador == 4:
                        
                        pts3 = pts4 + pts
                        
                    cuenta_ronda = cuenta_ronda + 1
                    print(" Pulsa Enter para continuar...") 
                    input()
                    
                    if cuenta_ronda != 4:
                        
                        ronda_splash(cuenta_ronda)
        
        elif repartidor == 2:
            
            while pasada <= 2:
                
                if pasada == 0:
                    
                    ronda_splash(cuenta_ronda)
                    
                mostrar_mesa()
                print("")
                print(" Pulsa Enter para continuar...") 
                input()
                system('cls')
                print(" ")
                print("                             Turno Jugador 4                            ")
                print(" ")                 
                turno_cpu(4)
                system('cls')
                mostrar_mesa()
                #Mostrar Cartas Jugador 1
                print(" ")
                print("                              Turno {nombre_jug1}                            ")
                print(" ")
                turno_jug1()
                system('cls')
                mostrar_mesa()
                print(" ")
                print("                              Turno Jugador 2                            ")
                print(" ")
                turno_cpu(2)
                mostrar_mesa()
                print(" ")
                print("                              Turno Jugador 3                            ")
                print(" ")
                turno_cpu(3)
                mostrar_mesa()
                ganador_en_juego = revisar_pts()
                
                if ganador_en_juego == True:
                    
                    return ganador_en_juego
                
                else:
                    
                    pasada = pasada + 1
                    
                if pasada == 3:
                    
                    pts, id_ganador = canto_mayor(repartidor)
                    
                    if id_ganador == 1:
                        
                        pts1 = pts1 + pts
                        
                    elif id_ganador == 2:
                        
                        pts2 = pts2 + pts
                        
                    elif id_ganador == 3:
                        
                        pts3 = pts3 + pts
                        
                    elif id_ganador == 4:
                        
                        pts4 = pts4 + pts
                        
                    cuenta_ronda = cuenta_ronda + 1
                    print(" Pulsa Enter para continuar...") 
                    input()
                    
                    if cuenta_ronda != 4:
                        
                        ronda_splash(cuenta_ronda)
        
        elif repartidor == 3:
            
            while pasada <= 2:
                
                if pasada == 0:
                    
                    ronda_splash(cuenta_ronda)
                    
                mostrar_mesa()
                print("")
                print(" Pulsa Enter para continuar...") 
                input()
                system('cls')
                #Mostrar Cartas Jugador 1
                print(" ")
                print("                              Turno {nombre_jug1}                            ")
                print(" ")
                turno_jug1()
                system('cls')
                mostrar_mesa()
                print(" ")
                print("                              Turno Jugador 2                            ")
                print(" ")
                turno_cpu(2)
                mostrar_mesa()
                print(" ")
                print("                              Turno Jugador 3                            ")
                print(" ")                 
                turno_cpu(3)
                mostrar_mesa()
                print(" ") 
                print("                              Turno Jugador 4                            ")
                print(" ")
                turno_cpu(4)
                system('cls')
                mostrar_mesa()
                ganador_en_juego = revisar_pts()
                
                if ganador_en_juego == True:
                    
                    return ganador_en_juego
                
                else:
                    
                    pasada = pasada + 1
                    
                if pasada == 3:
                    
                    pts, id_ganador = canto_mayor(repartidor)
                    
                    if id_ganador == 1:
                        
                        pts1 = pts1 + pts
                        
                    elif id_ganador == 2:
                        
                        pts2 = pts2 + pts
                        
                    elif id_ganador == 3:
                        
                        pts3 = pts3 + pts
                        
                    elif id_ganador == 4:
                        
                        pts4 = pts4 + pts
                        
                    cuenta_ronda = cuenta_ronda + 1
                    print("")
                    print(" Pulsa Enter para continuar...") 
                    input()
                    if cuenta_ronda != 4:
                        
                        ronda_splash(cuenta_ronda)
                        
    #Luego de salir del bucle
                        
    quien_se_lleva_mesa()
    return False

#Funcion Agregar carta a mesa

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
        
        system('cls')
        print(" ______________________________________________________________________________")
        print(f"                                                               ")
        print(f"                  El jugador{turno_id} ha hecho 4 en mesa +4 pts         ")
        print(f"                                                                ")
        print(" ______________________________________________________________________________")
        print("")
        print(" Pulsa Enter para continuar...") 
        input()
        
        if turno_id == 1:
            
            pts1 = pts1 + 4
            
        elif turno_id == 2:
            
            pts2 = pts2 + 4
            
        elif turno_id == 2:
            
            pts3 = pts3 + 4
            
        elif turno_id == 2:
            
            pts3 = pts3 + 4
            
    return int(maso)

#Funcion Caida
def comprobar_caida(valor_carta_jug, turno_id):
    
    global bak_valor_ultima_carta, ultimo_dejar_carta_mesa_id
    
    jug_anterior = turno_id - 1
    
    if valor_carta_jug != bak_valor_ultima_carta:
        
        return False, 0
    else:
        
        if valor_carta_jug >= 1 and valor_carta_jug <= 7 and ultimo_dejar_carta_mesa_id == jug_anterior:
            
            bak_valor_ultima_carta = 0
            return True, 1
        
        elif valor_carta_jug == 10 and ultimo_dejar_carta_mesa_id == jug_anterior:
            
            bak_valor_ultima_carta = 0
            return True, 2
        
        elif valor_carta_jug == 11 and ultimo_dejar_carta_mesa_id == jug_anterior:
            
            bak_valor_ultima_carta = 0
            return True, 3
        
        elif valor_carta_jug == 12 and ultimo_dejar_carta_mesa_id == jug_anterior:
            
            bak_valor_ultima_carta = 0
            return bool(True), int(4)
        
    return False, 0 #El valor es igual pero la carta no fue colocada por el jug anterior al de turno
        

#Funcion Turno Jug 1
def turno_jug1():
    
    global pts1, maso_jugador1, jug1, canto_jug1, nombre_carta, nombre_jug1
    
    system('cls')
    if len(jug1) != 0:
              
        mostrar_mesa()
        
        mostrar_cartas()
        if len(jug1) == 3:
            
            canto_jug1 = comprobar_canto_jug(jug1, 1)
            print(" ")
            
        print("")
        opcion = ''
        
        while True:
            
            opcion = str(input("  Selecciona la carta que desea jugar (a, b, c) y pulsa Enter: "))
            i = 0
            
            if opcion == 'a':
                
                i = jug1[0]
                j = agregar_a_mesa(i, 1)
                maso_jugador1 = maso_jugador1 + j
                jug1.remove(i)
                #Limpiar pantalla y mostrar cambios
                system('cls')
                mostrar_mesa()
                print(" ")
                print(f"     {nombre_jug1} coloco en la mesa un ({valor_carta[i]})  {nombre_carta[i]}    ")
                print(" ")
                print(" Pulsa Enter para continuar...") 
                input()
                #Comprobar caida
                
                if j != 0:
                    
                    caida, pts = comprobar_caida(valor_carta[i], 1)
                    pts1 = pts1 + pts #Variable global de pts jug 1
                    
                    if caida == True:
                        
                        print(" ______________________________________________________________________________")
                        print("                                                                 ")
                        print(f"                        {nombre_jug1} ha hecho caida de {pts} pts            ")
                        print("                                                                ")
                        print(" ______________________________________________________________________________")
                        print("")
                        print(" Pulsa Enter para continuar...")
                        input()
                        
                system('cls')        
                mostrar_mesa()
                break
            
            elif opcion == 'b':
                
                i = jug1[1]
                j = agregar_a_mesa(i, 1)
                maso_jugador1 = maso_jugador1 + j
                jug1.remove(i)
                system('cls')
                mostrar_mesa()
                
                print(" ")
                print(f"     {nombre_jug1} coloco en la mesa un ({valor_carta[i]})  {nombre_carta[i]}    ")
                print(" ")
                print("Pulsa Enter para continuar...") 
                input()
                #Comprobar caida
                if j != 0:
                    
                    caida, pts = comprobar_caida(valor_carta[i], 1)
                    pts1 = pts1 + pts #Variable global de pts
                    
                    if caida == True:
                        
                        print(" ______________________________________________________________________________")
                        print("                                                                 ")
                        print(f"                        {nombre_jug1} ha hecho caida de {pts} pts            ")
                        print("                                                                ")
                        print(" ______________________________________________________________________________")
                        print("")
                        print(" Pulsa Enter para continuar...")
                        input()
                        
                system('cls')        
                mostrar_mesa()
                break
            
            elif opcion == 'c':
                
                i = jug1[2]
                j = agregar_a_mesa(i, 1)
                maso_jugador1 = maso_jugador1 + j
                jug1.remove(i)
                system('cls')
                mostrar_mesa()
                print(" ")
                print(f"     {nombre_jug1} coloco en la mesa un ({valor_carta[i]})  {nombre_carta[i]}    ")
                print(" ")
                print("Pulsa Enter para continuar...") 
                input()
                #Comprobar caida
                if j != 0:
                    
                    caida, pts = comprobar_caida(valor_carta[i], 1)
                    pts1 = pts1 + pts
                    
                    if caida == True:
                        
                        print(" ______________________________________________________________________________")
                        print("                                                                 ")
                        print(f"                        {nombre_jug1} ha hecho caida de {pts} pts            ")
                        print("                                                                ")
                        print(" ______________________________________________________________________________")
                        print("")
                        print(" Pulsa Enter para continuar...")
                        input()
                system('cls')
                mostrar_mesa()
                break
    
    ##input()#Pausa para lectura

#Funcion Cambio de CPU a CPU_valor
def mano_a_valor(mano):
    
    i = 0
    mano_valor = []
    
    for j in mano:
        
        mano_valor.insert(i,valor_carta[j])
        i = i + 1
        
    return mano_valor

#Funcion Turno CPU  
def turno_cpu(cpuid):
    
    global bak_valor_ultima_carta, pts2, pts3, pts4, jug2, jug3, jug4, maso_jugador2, maso_jugador3, maso_jugador4
    global canto_jug2, canto_jug3, canto_jug4, nombre_carta
   
    if cpuid == 2:
        
        if len(jug2) == 3:
            
            canto_jug2 = comprobar_canto_jug(jug2, 2)
            
            if canto_jug2[0] != 0:
                
                print("")
                print("Pulsa Enter para continuar...")
                print("")
                input()
                
        print(" ")
        
        if len(jug2) != 0:
            
            index = 0
            #Analizar mesa preferencia Caida
            jug2_valor = mano_a_valor(jug2)
            if bak_valor_ultima_carta != 0 and bak_valor_ultima_carta in jug2_valor:
                
                index = jug2_valor.index(bak_valor_ultima_carta)
                
            else:
                
                if len(jug2) == 3:
                    
                    index = randint(0,2)
                    
                elif len(jug2) == 2:
                    
                    index = randint(0,1)
                    
                elif len(jug2) <= 1:
                    
                    index = 0
                    
            #Carta eligida por CPU   
            i = jug2[index]
            j = agregar_a_mesa(i, 2)
            maso_jugador2 = maso_jugador2 + j
            jug2.remove(i)
            system('cls')
            #Mostrar mesa y anunciar carta
            print(" ")
            mostrar_mesa()
            print(" ")
            print(f"     El jugador 2 coloco en la mesa un ({valor_carta[i]})  {nombre_carta[i]}    ")
            print(" ")
            #Comprobar caida
            
            if j != 0:
                
                caida, pts = comprobar_caida(valor_carta[i], 2)
                pts2 = pts2 + pts
                
                if caida == True:
                    
                    print(" ______________________________________________________________________________")
                    print("                                                                 ")
                    print(f"                     El jugador 2 ha hecho caida de {pts} pts            ")
                    print("                                                                ")
                    print(" ______________________________________________________________________________")
                    print("")
                    print(" Pulsa Enter para continuar...")
                    input()
                      
        
    elif cpuid == 3:
        
        if len(jug3) == 3:
            
            canto_jug3 = comprobar_canto_jug(jug3, 3)
            
            if canto_jug2[0] != 0:
                
                print("Pulsa Enter para continuar...") 
                input()
        print(" ")
        
        if len(jug3) != 0:
            
            index = 0
            
            #Analizar mesa preferencia Caida
            jug3_valor = mano_a_valor(jug3)
            
            if bak_valor_ultima_carta != 0 and bak_valor_ultima_carta in jug3_valor:
                
                index = jug3_valor.index(bak_valor_ultima_carta)#Carta eligida por CPU
                
            else:
                
                if len(jug3) == 3:
                    
                    index = randint(0,2)
                    
                elif len(jug3) == 2:
                    
                    index = randint(0,1)
                    
                elif len(jug3) <= 1:
                    
                    index = 0
                    
            #Carta eligida por CPU
            i = jug3[index]
            j = agregar_a_mesa(i, 3)
            maso_jugador3 = maso_jugador3 + j
            jug3.remove(i)
            system('cls')
            #Mostrar mesa y anunciar carta
            print(" ")
            mostrar_mesa()
            mostrar_mesa()
            print(" ")
            print(f"     El jugador 3 coloco en la mesa un ({valor_carta[i]})  {nombre_carta[i]}    ")
            print(" ")
            #Comprobar caida
            
            if j != 0:
                
                caida, pts = comprobar_caida(valor_carta[i], 3)
                pts3 = pts3 + pts
                
                if caida == True:
                    
                    print(" ______________________________________________________________________________")
                    print("                                                                 ")
                    print(f"                     El jugador 3 ha hecho caida de {pts} pts            ")
                    print("                                                                ")
                    print(" ______________________________________________________________________________")
                    print("")
                    print(" Pulsa Enter para continuar...")
                    input()
        
    elif cpuid == 4:
        
        if len(jug4) == 3:
            
            canto_jug4 = comprobar_canto_jug(jug4, 4)
            
            if canto_jug2[0] != 0:
                
                print(" Pulsa Enter para continuar...") 
                input()
        print(" ")
        
        if len(jug4) != 0:
            
            index = 0
            
            #Analizar mesa preferencia Caida
            jug4_valor = mano_a_valor(jug4)
            
            if bak_valor_ultima_carta != 0 and bak_valor_ultima_carta in jug4_valor:
                
                index = jug4_valor.index(bak_valor_ultima_carta)#Carta eligida por CPU
                
            else:
                
                if len(jug4) == 3:
                    
                    index = randint(0,2)
                    
                elif len(jug4) == 2:
                    
                    index = randint(0,1)
                    
                elif len(jug4) == 1:
                    
                    index = 0
                    
            #Carta eligida por CPU
            i = jug4[index]
            j = agregar_a_mesa(i, 4)
            maso_jugador4 = maso_jugador4 + j
            jug4.remove(i)
            system('cls')
            #Mostrar mesa y anunciar carta
            print(" ")
            mostrar_mesa()
            mostrar_mesa()
            print(" ")
            print(f"     El jugador 4 coloco en la mesa un ({valor_carta[i]})  {nombre_carta[i]}    ")
            print(" ")
            #Comprobar caida
            
            if j != 0:
                
                caida, pts = comprobar_caida(valor_carta[i], 4)
                pts4 = pts4 + pts
                
                if caida == True:
                    
                    print(" ______________________________________________________________________________")
                    print("                                                                 ")
                    print(f"                     El jugador 4 ha hecho caida de {pts} pts            ")
                    print("                                                                ")
                    print(" ______________________________________________________________________________")
                    print("")
                    print(" Pulsa Enter para continuar...")
                    input()
                    
    print("Pulsa Enter para continuar...")        
    input()

#Resultados cuenta maso
def resultados():
    
    global maso_jugador1, maso_jugador2, maso_jugador3, maso_jugador4, equipo1_pts, equipo2_pts, pts1, pts2, pts3, pts4, nombre_jug1
    equipo1_pts = pts1 + pts3
    equipo2_pts = pts2 + pts4
    equipo1_maso = maso_jugador1 + maso_jugador3
    equipo2_maso = maso_jugador2 + maso_jugador4
    
    
    if equipo1_maso > 20:
        
        sumar_pts_cartas_1 = equipo1_maso - 20
        
        if sumar_pts_cartas_1 < 0:
            
            sumar_pts_cartas_1 = sumar_pts_cartas_1 * -1
            
    else:
        
        sumar_pts_cartas_1 = 0
        
    if equipo2_maso > 20:
        
        sumar_pts_cartas_2 = equipo1_maso - 20
        
        if sumar_pts_cartas_2 < 0:
            
            sumar_pts_cartas_2 = sumar_pts_cartas_2 * -1
            
    else:
        
        sumar_pts_cartas_2 = 0
    
    total_equipo1 = equipo1_pts + sumar_pts_cartas_1
    total_equipo2 = equipo2_pts + sumar_pts_cartas_2
    
    
    system('cls')
    print("")
    print("#############################################################################")
    print("                                                                             ")
    print("                          TABLA DE PUNTUAJE                           ")             
    print("                                                                             ")
    print(f"            {nombre_jug1} y Jug. 3 = {equipo1_pts}pts |  Jug. 2 y Jug. 4 = {equipo2_pts}pts         ")
    print("                                                                             ")
    print("_____________________________________________________________________________")
    print("                                                                             ")
    print("              CUANTA TOTAL DE CARTAS EN MASO DE JUGADORES             ")             
    print("                                                                            ")
    print(f"        {nombre_jug1} y Jug. 3 = {equipo1_maso} cartas | Jug. 2 y Jug. 4 = {equipo2_maso} cartas     ")
    print(f"              Pts ganados = {sumar_pts_cartas_1}pts  |  Pts ganados = {sumar_pts_cartas_2}pts              ") 
    print("                                                                             ")
    if total_equipo1 >= 24 and total_equipo2 < 24 or total_equipo2 >= 24 and total_equipo1 < 24:
        
        print("_____________________________________________________________________________")
        print("                                                                             ")
        print("                               GANADORES                              ")
        print("                                                                             ")
        
        if total_equipo1 > total_equipo2:
            
            print("                               EQUIPO 1                               ")
            
        else:
            
            print("                               EQUIPO 2                               ")
            
        print("                                                                             ")
        print("#############################################################################")
        print("Pulsa Enter para continuar...") 
        input()
        pts1 = sumar_pts_cartas_1 + pts1
        pts2 = sumar_pts_cartas_2 + pts2
        return True
    
    else:
        
        print("_____________________________________________________________________________")
        print("                                                                             ")
        
        if total_equipo1 > total_equipo2:
            
            print("                               EQUIPO 1                               ")
            print(f"                         ARRIBA CON {total_equipo1}pts                           ")
            print("                               EQUIPO 2                               ")
            print(f"                                {total_equipo2}pts                           ")
            pts1 = sumar_pts_cartas_1 + pts1
            pts2 = sumar_pts_cartas_2 + pts2
            
        else:
            
            print("                               EQUIPO 2                               ")
            print(f"                         ARRIBA CON {total_equipo2}pts                           ")
            print("                               EQUIPO 1                               ")
            print(f"                                {total_equipo1}pts                           ")
            pts1 = sumar_pts_cartas_1 + pts1
            pts2 = sumar_pts_cartas_2 + pts2
            
        print("                                                                             ") 
        print("_____________________________________________________________________________")
        print("                                                                             ")
        print("                               Mezclando                              ")
        print("                                cartas                                ")
        print("                                                                             ")
        print("#############################################################################")
        pts1 = sumar_pts_cartas_1 + pts1
        pts2 = sumar_pts_cartas_2 + pts2
        print(" Pulsa Enter para continuar...") 
        input()
        return False
    
    

#Funcion Resetar mesa y conteo de maso jugadores
def reset_partida():
    
    global maso_jugador1, maso_jugador2, maso_jugador3, maso_jugador4, mesa, mesa_valor, jug1, jug2, jug3, jug4, maso_revuelto
    
    mesa.clear()
    mesa_valor.clear()
    jug1.clear()
    jug2.clear()
    jug3.clear()
    jug4.clear()
    maso_jugador1 = 0
    maso_jugador2 = 0
    maso_jugador3 = 0
    maso_jugador4 = 0
    maso_revuelto = sample(range(0,40),40)

#Funcion ultima ronda mesa
def quien_se_lleva_mesa():
    
    global ultimo_agarrar_carta_id , mesa, maso_jugador1, maso_jugador2, maso_jugador3, maso_jugador4, nombre_jug1
    
    if ultimo_dejar_carta_mesa_id == 1:
        
        i = len(mesa)
        maso_jugador1 = maso_jugador1 + i
        print("")
        print(f"  {nombre_jug1} se lleva la mesa + {i} a su maso")
        print("")
        print("Pulsa Enter para continuar...") 
        input()
        
    elif ultimo_dejar_carta_mesa_id == 2:
        
        i = len(mesa)
        maso_jugador2 = maso_jugador2 + i
        print("")
        print(f" El jugador {ultimo_dejar_carta_mesa_id} se lleva la mesa + {i} a su maso")
        print("")
        print("Pulsa Enter para continuar...") 
        input()
        
    elif ultimo_dejar_carta_mesa_id == 3:
        
        i = len(mesa)
        maso_jugador3 = maso_jugador3 + i
        print("")
        print(f" El jugador {ultimo_dejar_carta_mesa_id} se lleva la mesa + {i} a su maso")
        print("")
        print("Pulsa Enter para continuar...") 
        input()
        
    elif ultimo_dejar_carta_mesa_id == 4:
        
        i = len(mesa)
        maso_jugador4 = maso_jugador4 + i
        print("")
        print(f" El jugador {ultimo_dejar_carta_mesa_id} se lleva la mesa + {i} a su maso")
        print("")
        print("Pulsa Enter para continuar...") 
        input()

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
    canto = patrulla(cartas_jug_valor, turno_id)
    
    #Llamada a Registro
    if canto[0] == 0:
        
        canto = registro(cartas_jug_valor, turno_id)
        
    #Llamada a ronda_vigia_tribilin
    if canto[0] == 0:
        
        canto = ronda_vigia_tribilin(cartas_jug_valor, turno_id)
    
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
        print("")
        print(f"            El Jugador {turno_id} tiene {nombre_canto}        ")
        print("")
        return canto
    
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
                print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
                print("")
                return canto
            
        elif index_carta_canto == 1:
            
            if valor_carta_canto_mas == cartas_jug_valor[0]:
                
                pts_canto = 7
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Vigia'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print("")
                print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
                print("")
                return canto
             
        elif index_carta_canto == 0:
            
            if valor_carta_canto_menos == cartas_jug_valor[2]:
                
                pts_canto = 7
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Vigia'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
                print("")
                return canto
            
        elif index_carta_canto == 1:
            
            if valor_carta_canto_menos == cartas_jug_valor[0]:
                
                pts_canto = 7
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Vigia'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print("")
                print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
                print("")
                return canto
                
        #Si no es vigia Comprobando pts de la ronda
        if canto[0] == 0 and valor_carta_canto > 0:
            
            if valor_carta_canto >= 1 and valor_carta_canto <= 7:
                pts_canto = 1
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Ronda'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print("")
                print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
                print("")
                return canto
            
            elif valor_carta_canto == 10:
                
                pts_canto = 2
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Ronda'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print("")
                print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
                return canto 
            
            elif valor_carta_canto == 11:
                
                pts_canto = 3
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Ronda'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print("")
                print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
                return canto
           
            elif valor_carta_canto == 12:
                
                pts_canto = 4
                i = cartas_jug_valor[0] + cartas_jug_valor[1] + cartas_jug_valor[2]
                nombre_canto = 'Ronda'
                canto = [pts_canto,i,turno_id,nombre_canto]
                print("")
                print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
                print("")
                return canto
            
    #No hay ronda_vigia_tribilin
    else:
        return canto
        
    
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
        print("")
        print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
        print("")
        return canto
    
    else:
        
        return canto

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
        print("")
        print(f"          El Jugador {turno_id} tiene {nombre_canto}           ")
        print("")
        return canto
    
    else:#No hay registro
        
        return canto
    
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
        print(" ")
        print("###############################################################################")
        print("#                                                                             #")
        print(f"  El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts  ")
        print("#                                                                             #")
        print("###############################################################################")
        print(" ")
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
            print(" ")
            print("###############################################################################")
            print("#                                                                             #")
            print(f"  El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts  ")
            print("#                                                                             #")
            print("###############################################################################")
            print(" ")
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
                print(" ")
                print("###############################################################################")
                print("#                                                                             #")
                print(f"  El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts  ")
                print("#                                                                             #")
                print("###############################################################################")
                print(" ")
                return pts, id_ganador
            
            elif dup == rep: #Si uno de los jugadores es el repartidor pero no es posicion 4
                
                
                orden_id.remove(rep)
                if rep == orden_id[0]:
                    
                    id_ganador = orden_id[-1]
                    j = id_ganador - 1
                    nombre_canto = orden_nombre_canto[j]
                    pts = max_pts #Sumar pts al ganador
                    print(" ")
                    print("###############################################################################")
                    print("#                                                                             #")
                    print(f"  El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts  ")
                    print("#                                                                             #")
                    print("###############################################################################")
                    print(" ")
                    return pts, id_ganador
                
                else:
                    
                    id_ganador = orden_id[0]
                    j = id_ganador - 1
                    nombre_canto = orden_nombre_canto[j]
                    pts = max_pts #Sumar pts al ganador
                    print(" ")
                    print("###############################################################################")
                    print("#                                                                             #")
                    print(f"  El canto del Jugador {id_ganador} es el ganador con {nombre_canto}, {pts}pts  ")
                    print("#                                                                             #")
                    print("###############################################################################")
                    print(" ")
                    return pts, id_ganador
                    
    return pts, id_ganador #no hubo cantos  
    
def revisar_pts():
    
    global equipo1_pts, equipo2_pts, nombre_jug1
    
    if equipo1_pts >= 24 and equipo2_pts < 24 or equipo2_pts >= 24 and equipo1_pts < 24:
        
        system('cls')
        print("")
        print("##############################################################################")
        print("                                                                            ")
        print("                              TABLA DE PUNTUAJE                             ")             
        print("                                                                            ")
        print(f"            {nombre_jug1} y Jug. 3 = {equipo1_pts}pts |  Jug. 2 y Jug. 4 = {equipo2_pts}pts         ")
        print("                                                                            ")
        print("______________________________________________________________________________")
        print("                                                                            ")
        print("                                 GANADORES                                  ")
        print("                                                                            ")
        if equipo1_pts > equipo2_pts:
            
            print("                                  EQUIPO 1                                  ")
            
        else:
            
            print("                                  EQUIPO 2                              ")
        print("                                                                            ")
        print("##############################################################################")
        print("")
        print(" Pulsa Enter para continuar...") 
        input()
        return True
    
    else:
        
        return False
        
def banner_pts():
    
    global equipo1_pts, equipo2_pts, pts1, pts3, pts2, pts4, nombre_jug1
    equipo1_pts = pts1 + pts3
    equipo2_pts = pts2 + pts4
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"         {nombre_jug1} y Jug. 3 = {equipo1_pts}pts        |         Jug. 2 y Jug. 4 = {equipo2_pts}pts         ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
def ronda_splash(i):
    
    system('cls')
    print("")
    print("")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  RONDA {i} @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("")
    print(" Presione Enter para continuar...")
    input()
    system('cls')

def echar_mesa(repartidor):
    
    global mesa, valor_carta, nombre_carta, pts1, pts2, pts3, pts4
    pts = 0
    escoger_cpu = [1,4]
    
    if repartidor == 0:
        
        repartidor2 = repartidor + 2
        
    elif repartidor == 3:
        
        repartidor2 = 1
        
    elif repartidor == 1 or repartidor == 2:
        
        repartidor2 = repartidor + 2
        
    while True:
        
        try:
            
            system('cls')
            print("")
            print("###############################################################################")
            print("#                                                                             #")
            print("#                El repartidor apuesta que la mesa empezara por:              #")
            print("#                                                                             #")
            
            if repartidor != 0:
                
                opcion = int(choice(escoger_cpu))
                print(f"                                        {opcion}                                    ")
                print("#                                                                             #")
                print("###############################################################################")
                print(" ")
                print("Presione Enter para continuar")
                input()
                break
            
            else:
                
                print("#                              Elige 1 o 4 y pulsa Enter:                     #")
                print("#                                                                             #")
                print("###############################################################################")
                print(" ")
                opcion = int(input("                                      "))
                
                if opcion == 1:
                    
                    print(" El repartidor apuesta que la mesa empezara por 1 y terminara en 4")
                    
                    break
                
                else:
                    
                    print(" El repartidor apuesta que la mesa empezara por 4 y terminara en 1")
                    
                    break
                    

        except:
            
            continue
    
    
   
   
    i=0
    
    while i <= 4:
        
        system('cls')    
        print("###############################################################################")
        print("#                                                                             #")
        print("#                                  Cartas                                     #")
        print("#                                en la mesa                                   #")
        print("#                                                                             #")
        print("###############################################################################")
        print("")                                                                    
        print("")
        
        print(f"        1.-({valor_carta[mesa[0]]}) {nombre_carta[mesa[0]]}        ")
        
        if opcion == 1 and valor_carta[mesa[0]] == 1 :
            
            print("")
            print(" Pego el 1 se te suma 1 pts")
            print("")
            
            if i == 0:
                
                pts += 1
                
        elif opcion == 4 and valor_carta[mesa[0]] == 4 :
            
            print("")
            print(" Pego el 4 se te suma 4 pts")
            print("")
            
            if i == 0:
                
                pts += 4
            
            
        if i>=1:
            
            print(f"        2.-({valor_carta[mesa[1]]}) {nombre_carta[mesa[1]]}        ")
            
            if opcion == 1 and valor_carta[mesa[1]] == 2 :
                
                print("")
                print(" Pego el 2 se te suma 2 pts")
                print("")
                
                if i == 1:
                    
                    pts += 2
                    
            elif opcion == 4 and valor_carta[mesa[1]] == 3 :
                
                print("")
                print(" Pego el 3 se te suma 3 pts")
                print("")
                
                if i == 1:
                    
                    pts += 3
            
        if i>=2:
            
            print(f"        3.-({valor_carta[mesa[2]]}) {nombre_carta[mesa[2]]}        ")
            
            if opcion == 1 and valor_carta[mesa[2]] == 3:
                
                print("")
                print(" Pego el 3 se te suma 3 pts")
                print("")
                
                if i == 2:
                    
                    pts += 3
                    
            elif opcion == 4 and valor_carta[mesa[2]] == 2 :
                
                print("")
                print(" Pego el 2 se te suma 2 pts")
                print("")
                
                if i == 2:
                    
                    pts += 2
            
        if i>=3:
            
            print(f"        4.-({valor_carta[mesa[3]]}) {nombre_carta[mesa[3]]}        ")
            
            if opcion == 1 and valor_carta[mesa[3]] == 4 :
                
                print("")
                print(" Pego el 4 se te suma 4 pts")
                print("")
                
                if i == 3:
                    
                    pts += 4
                    
            elif opcion == 4 and valor_carta[mesa[3]] == 1 :
                
                print("")
                print(" Pego el 1 se te suma 1 pts")
                print("")
                
                if i == 3:
                    
                    pts += 1
                    
        if i>=4:
            
            if pts != 0:
                
                print("")
                print("")
                print("______________________________________________________________________________")
                print("")
                print(f"                         El repartidor ha ganado {pts}pts")
                print("")
                print("______________________________________________________________________________")
                print("")
                print("")
                
                if repartidor == 0:
                    
                    pts1 = pts1 + pts
                    
                elif repartidor == 1:
                    
                    pts2 = pts2 + pts
                    
                elif repartidor == 2:
                    
                    pts3 = pts3 + pts
                    
                elif repartidor == 3:
                    
                    pts4 = pts4 + pts
                    
            else:
                
                print("")
                print("")
                print("______________________________________________________________________________")
                print("")
                print(f"     El repartidor no ganado ningun punto. El jugador {repartidor2} ha ganado 1 pts")
                pts += 1
                
                if repartidor2 == 1:
                    
                    pts1 = pts1 + pts
                    
                elif repartidor2 == 2:
                    
                    pts2 = pts2 + pts
                    
                elif repartidor2 == 3:
                    
                    pts3 = pts3 + pts
                    
                elif repartidor2 == 4:
                    
                    pts4 = pts4 + pts
                print("")
                print("______________________________________________________________________________")
                print("")
                print("")
                
        i += 1
        sleep(1)
        
   
    print("")
    print(" Pulse Enter para continuar")
    input()

def obtener_nombre_jug1():
    
    global nombre_jug1
    empty_list = ''
    
    while True:
        
        try:
            
            print("")
            nombre_jug1 = input("       Ingresa tu nombre y presiona Enter: ")
            
            if nombre_jug1 != empty_list:
                
                print("")
                print(f" Bienvenido {nombre_jug1} seras el Jugador 1 tu companero sera el Jug. 3")
                print("")
                break
            
        except:
            
            continue
