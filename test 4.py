from os import system
from random import sample
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




def elegir_repartidor():
    global nombre_carta, valor_carta 
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
                list_id = ['Jugador 1','Jugador 2', 'Jugador 3', 'Jugador 4']
                list_id2 = [0,1,2,3]
                break
            
            elif opcion == 2:
                list_id = ['Jugador 4','Jugador 1','Jugador 2', 'Jugador 3' ]
                list_id2 = [3,0,1,2]
                break
            elif opcion == 3:
                list_id = ['Jugador 3','Jugador 4','Jugador 1','Jugador 2' ]
                list_id2 = [2,3,0,1]
                break
            
            elif opcion == 4:
                list_id = ['Jugador 2','Jugador 3','Jugador 4','Jugador 1', ]
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
            print(f" El repartidor sera el jugador {list_id[index]} con la carta alta ({carta_alta}) {nombre_carta[num_carta]}")
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

repartidor = elegir_repartidor()
print(repartidor)

"""def elegir_repartidor():
        repartidor = random.sample(range(0,40),40) #barajar cartas
        A_1=repartidor[0]
        B_2=repartidor[1]
        C_3=repartidor[2]
        D_4=repartidor[3]
        A= valor_carta[A_1]
        B= valor_carta[B_2]
        C= valor_carta[C_3]
        D= valor_carta[D_4]
    
        if(A > B and A > C and A > D):
            X=A
            res=0
            print(f"#      Ganaste con la carta '{nombre_carta[A_1]}' eres el repartidor        #")
                    
        else:
            if(B > A and B > C and B > D):
                X=B
                res=1
                print(f"#  Gano el Jugador 2 con la carta '{nombre_carta[B_2]}' sera el repartidor  #")
            else:
                if(C > A and C > B and C > D):
                    X=C
                    res=2
                    print(f"#  Gano el Jugador 3 con la carta '{nombre_carta[B_2]}' sera el repartidor  #")
                else:
                    X=D
                    res=3
                    print(f"#  Gano el Jugador 4 con la carta '{nombre_carta[B_2]}' sera el repartidor  #")
        return res
"""