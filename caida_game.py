from caida_var import repartir_mesa, echar_mesa, elegir_repartidor, juego, resultados, reset_partida, obtener_nombre_jug1
from time import sleep
from os import system

#IMPORT VARIABLES
print("")
print("###############################################################################")
print("#                                                                             #")
print("#                      Bienvenido a Caida Command Line                        #") 
print("#                                                                             #")
print("#                                                                             #")
print("#                   Para empezar sortearemos el repartidor                    #")
print("#                    repartiremos una carta a cada Jugador                    #")
print("#                         ganara la carta 'mas alta'                          #")
print("#                                                                             #")
print("#                                                                             #")
print("###############################################################################")
print("                                                  Programado por Nestor Ramirez")
print(" ")
obtener_nombre_jug1()
print(" ")
print(" ")
print(" Pulsa Enter para continuar...") 
input()
system('cls') 
                                                                  
repartidor = elegir_repartidor()

system('cls')
print("###############################################################################")
print("#                                                                             #")
print("#                                Revolviendo                                  #")
print("#                                  cartas                                     #")
print("#                                                                             #")
print("###############################################################################")
sleep(1)
system('cls')

#Repartir Mesa
repartir_mesa()
echar_mesa(repartidor)
#Inicio del juego
ganador_en_juego = juego(repartidor)

if ganador_en_juego == False:
    
    continuar_partida = resultados() #Se juega una o mas partidas hasta hallar un ganador

    while continuar_partida == False or ganador_en_juego == False:
        
        if repartidor != 3:
            repartidor = repartidor + 1
            
        else:
            repartidor = 0
            
        reset_partida()
        repartir_mesa()
        ganador_en_juego = juego(repartidor)
        if ganador_en_juego == False:
            
            continuar_partida = resultados()#Verificar para buscar ganador por mayor numero de cartas maso
            
            if continuar_partida == True:
                
                system('cls')
                print("###############################################################################")
                print("#                                                                             #")
                print("#                                     GAME                                    #")
                print("#                                     OVER                                    #")
                print("#                                                                             #")
                print("###############################################################################")
                print("                                                  Programado por Nestor Ramirez")
                input()
                break

        else:
            
            system('cls')
            print("###############################################################################")
            print("#                                                                             #")
            print("#                                     GAME                                    #")
            print("#                                     OVER                                    #")
            print("#                                                                             #")
            print("###############################################################################")
            print("                                                  Programado por Nestor Ramirez")
            input()
            break

else: #Hay un ganador en la primera partida
    system('cls')
    print("###############################################################################")
    print("#                                                                             #")
    print("#                                     GAME                                    #")
    print("#                                     OVER                                    #")
    print("#                                                                             #")
    print("###############################################################################")
    print("                                                  Programado por Nestor Ramirez")
    input()
    

