def guerraPOO():
    import random
    import os
#A JUAN LE GUSTA EL PENE
    #sexo anal
    def limpiar_consola():
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para Linux y macOS
            os.system('clear')

    class JuegoGuerra:
        def __init__(self):
            self.mazo1 = []
            self.mazo2 = []
            self.mesa1 = []
            self.mesa2 = []
            self.menu_guerra()
    
        def menu_guerra(self):
            self.cartas_aleatorias()
            limpiar_consola()

            resp = "si"
            while resp == "si":
                print("\t ==== Menu Guerra ====\n")
                num = input(" #1 Empezar a Jugar \n #2 ¿Cómo Jugar? \n #3 Créditos \n\n\n# ")
                limpiar_consola()

                if num == "1":
                    self.sub_menu_guerra()
                elif num == "2":
                    self.instrucciones_guerra()
                elif num == "3":
                    self.creditos_guerra()
                elif num == "salir":
                    resp = "no"

        def cartas_aleatorias(self):
            valores = [1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 10,10,10,10, 11,11,11,11, 12,12,12,12]
            random.shuffle(valores)
            mazos = [valor for valor in valores]
            mitad = len(mazos) // 2
            mazo1_mitad = mazos[:mitad]
            mazo2_mitad = mazos[mitad:]
            x = 20
            z = 20
            while x != 0:
                self.mazo1.append(mazo1_mitad.pop())
                x -= 1
            while z != 0:
                self.mazo2.append(mazo2_mitad.pop())
                z -= 1

        def contar_cartas(self):
            cont = len(self.mazo1)
            cont2 = len(self.mazo2)

            if cont == 1 or cont2 == 1:
                self.devolver_cartas()
            elif cont == 0:
                self.resultado_perdio()
            elif cont2 == 0:
                self.resultado_gano()

            return cont

        def total_cartas(self):
            print("\t==== Cartas Totales ====\n")

            cartas1 = len(self.mazo1) + len(self.mesa1)
            cartas2 = len(self.mazo2) + len(self.mesa2)

            if cartas1 == 1:
                limpiar_consola()
                print("\t==== Te has quedado sin cartas ====\n\n")
            elif cartas2 == 1:
                limpiar_consola()
                print("\t==== Tu enemigo se ha quedado sin cartas ====\n\n")

            print(" Cartas totales del jugador", cartas1, "/ 40")
            print(" Cartas totales del enemigo", cartas2, "/ 40")
            input("\n\n Pulse cualquier tecla para salir \t")
            limpiar_consola()

        def contar_mesa(self):
            cont = len(self.mesa1)
            cont2 = len(self.mesa2)
            return cont

        def devolver_cartas(self):
            self.ordenar_mesas_aleatoriamente1()
            self.ordenar_mesas_aleatoriamente2()
            while self.mesa1:
                self.mazo1.append(self.mesa1.pop())
            while self.mesa2:
                self.mazo2.append(self.mesa2.pop())

        def ver_mazo(self):
            print("\t ==== Ver Mazo ====\n")
            cont = self.contar_cartas()
            print(" Cartas actuales en mazo", cont, "/ 40")
            print("\n Tu mazo", self.mazo1)
            input("\n\n Pulse cualquier tecla para salir \t")
            limpiar_consola()

        def ver_mesa(self):
            print("\t ==== Ver Mesa ====\n")
            cont = self.contar_mesa()
            print(" Cartas actuales en mesa", cont, "/ 20")
            print("\n En la mesa tienes", self.mesa1)
            input("\n\n Pulse cualquier tecla para salir \t")
            limpiar_consola()

        def ordenar_mesas_aleatoriamente1(self):
            random.shuffle(self.mesa1)

        def ordenar_mesas_aleatoriamente2(self):
            random.shuffle(self.mesa2)

        def resultado_perdio(self):
            resp = ""
            while resp == "":
                print("\n\t ==== Juego Terminado ====\n")
                print("Te has quedado sin cartas para continuar")
                resp = input("\n\n Pulse cualquier tecla para regresar al menu principal \t")
                limpiar_consola()
                guerraPOO()

        def resultado_gano(self):
            resp = ""
            while resp == "":
                print("\n\t ==== Juego Terminado ====\n")
                print("Tu enemigo se ha quedado sin cartas para continuar")
                resp = input("\n\n Pulse cualquier tecla para regresar al menu principal \t")
                limpiar_consola()
                guerraPOO()

        def jugada(self):
            r = "si"
            while r == "si":
                print("\t ==== Jugada ====\n")
                ultima_carta1 = self.mazo1[-1] if self.mazo1 else None
                print(" Has lanzado un", ultima_carta1)
                try:
                    self.mazo1.pop()
                except:
                    print("Te has quedado sin cartas para continuar, has perdido")
                ultima_carta2 = self.mazo2[-1] if self.mazo2 else None
                print(" Te han lanzado un", ultima_carta2)
                try:
                    self.mazo2.pop()
                except:
                    print("Tu enemigo se ha quedado sin cartas para continuar, has Ganado")

                def gano():
                    self.mesa1.extend([ultima_carta1, ultima_carta2])
                    print("\n\t ==== Ganaste ====\n")
                    print(" Has ganado, ahora tienes 2 cartas más en mesa:", "[", ultima_carta1, ",", ultima_carta2, "]")

                def perdio():
                    self.mesa2.extend([ultima_carta1, ultima_carta2])
                    print("\n\t ==== Perdiste ====\n")
                    print(" Has perdido, ahora el oponente tiene 2 cartas más en mesa:", "[", ultima_carta1, ",", ultima_carta2, "]")

                def empate():
                    print("\n\t ==== Empate ====\n")
                    reposo1 = [ultima_carta1]
                    reposo2 = [ultima_carta2]
                    self.devolver_cartas()

                    while True:
                        try:
                            reposo1.append(self.mazo1.pop())
                            print(" Has tapado con ?")
                        except:
                            print("Te has quedado sin cartas para continuar, has perdido")
                            self.resultado_perdio()
                        try:
                            reposo2.append(self.mazo2.pop())
                            print(" Han tapado con ?")
                        except:
                            print("Tu enemigo se ha quedado sin cartas para continuar, has ganado")
                            self.resultado_gano()
                        try:
                            ultima_empate1 = self.mazo1.pop()
                            print(" Destapas con", ultima_empate1)
                            reposo1.append(ultima_empate1)
                        except:
                            print("Te has quedado sin cartas para continuar, has perdido")
                            self.resultado_perdio()

                        try:
                            ultima_empate2 = self.mazo2.pop()
                            print(" Destapan con", ultima_empate2)
                            reposo2.append(ultima_empate2)
                        except:
                            print("Tu enemigo se ha quedado sin cartas para continuar, has Ganado")
                            self.resultado_gano()

                        if ultima_carta1 is not None and ultima_carta2 is not None:
                            if ultima_empate1 > ultima_empate2:
                                print("\n\t ==== Ganaste ====\n")
                                self.mesa1.extend(reposo1 + reposo2)
                                break
                            elif ultima_empate1 < ultima_empate2:
                                print("\n\t ==== Perdiste ====\n")
                                self.mesa2.extend(reposo1 + reposo2)
                                break
                            else:
                                print("\n\t ==== Empate ====\n")
                        else:
                            self.limpiar_consola()
                            self.contar_cartas()
                            break


                if ultima_carta1 is not None and ultima_carta2 is not None:
                    if ultima_carta1 > ultima_carta2:
                        gano()
                    elif ultima_carta1 < ultima_carta2:
                        perdio()
                    else:
                        empate()
                else:
                    limpiar_consola()
                    self.contar_cartas()
                    break
                r=input("\n\n Pulse cualquier tecla para continuar \t")
                limpiar_consola()
        def sub_menu_guerra(self):
            resp = "si"
            while resp == "si":
                print("\t ==== Menu de Juego ====\n")
                eleccion = input(" #1 Jugar \n #2 Ver Mazo \n #3 Ver Mesa \n\n\n# ")
                limpiar_consola()

                if eleccion == "1":
                    self.contar_cartas()
                    self.jugada()
                    self.total_cartas()
                elif eleccion == "2":
                    self.ver_mazo()
                elif eleccion == "3":
                    self.ver_mesa()
                elif eleccion == "salir":
                    resp = "no"
        def instrucciones_guerra(self):
            r="si"
            while r == "si":

                print ("\t Bienvenid@ a Guerra\n")
                print ("Guerra es un juego de cartas; donde, el objetivo principal es dejar al rival sin cartas para jugar.\n\nEn Juego: Se lanzan dos cartas, una de tu mazo y la otra del mazo rival; las cuales decidirán el resultado de la partida.\n\nSistema de puntuación: Cada carta tiene un valor numerico; donde, 1<2<3<4<5<6<7<10<11<12.\n\nEmpate: En este juego el empate no devuelve las cartas; sino que, pasa a decidirse en una nueva ronda con la misma carta que empataste, otra de tu mazo que no puedes ver y por ultimo la que decidirá el resultado del empate. siempre que caigas en empate se restablecerán las cartas del mazo.\n\nMazo: El mazo es el conjunto de cartas disponibles para jugar.\n\nMesa: La mesa es el grupo de cartas que ganas jugando y que volverán a tu mazo en cuanto este se termine.")
                print("\n¡Buena suerte!")
                r=input("\n\n Pulse cualquier tecla para salir \t")
                limpiar_consola()
        def creditos_guerra(self):

            r="si"
            while r == "si":

                print ("\t ====Creditos==== \n")
                print ("Desarrollo:\n- Juan R: Programador Principal.\n- Carlos P: Programador Secundario. \n- Rony M: Programador Secundario\n\nInformación Legal:\n© 2024 StarLight. Todos los derechos reservados.")
                print("¡Gracias por jugar!")
                r=input("\n\n Pulse cualquier tecla para salir \t")
                limpiar_consola()
    guerra=JuegoGuerra()
    guerra.menu_guerra()
def juego_sieteymedio():
    import random
    import os
    import sys

    class Carta:
        def __init__(self, valor, mano):
            self.valor = valor
            self.mano = mano
    
        def __repr__(self):
            return f"{self.valor} de {self.mano}"
    
        def obtener_valor(self):
            if self.valor in ['Rey', 'Caballo', 'Sota']:
                return 0.5
            elif self.valor == 'As':
                return 1
            else:
                return float(self.valor)

    def limpiar_consola():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    class Baraja:
        def __init__(self):
            self.mano = ['Oros', 'Copas', 'Espadas', 'Bastos']
            self.valores = [2, 3, 4, 5, 6, 7, 'Sota', 'Caballo', 'Rey', 'As']
            self.cartas = self.crear_baraja()
            random.shuffle(self.cartas)

        def crear_baraja(self):
            baraja = []
            for mano in self.mano:
                for valor in self.valores:
                    baraja.append(Carta(valor, mano))
            return baraja
    
        def repartir(self):
            if len(self.cartas) > 0:
                return self.cartas.pop()
            else:
                return None

    class Jugador:
        def __init__(self, nombre):
            self.nombre = nombre
            self.mano = []
            self.puntos = 0

        def agregar_carta(self, carta):
            if carta:
                self.mano.append(carta)
                self.puntos += carta.obtener_valor()

        def mostrar_mano(self):
            return ', '.join(str(carta) for carta in self.mano)
    
        def __repr__(self):
            return f"{self.nombre} tiene {len(self.mano)} cartas y {self.puntos} puntos."

    class Juego:
        def __init__(self, jugadores):
            self.jugadores = [Jugador(nombre) for nombre in jugadores]
            self.baraja = Baraja()

        def repartir_cartas_iniciales(self):
            for jugador in self.jugadores:
                jugador.agregar_carta(self.baraja.repartir())

        def turno_jugador(self, jugador):
            limpiar_consola()
            print(f"\nEs el turno de {jugador.nombre}")
            while jugador.puntos <= 7.5:
                print(f"Tienes {jugador.puntos} puntos con las cartas: {jugador.mostrar_mano()}")
                opcion = input("¿Quieres pedir otra carta? (s/n): ").strip().lower()
                if opcion == 's':
                    carta = self.baraja.repartir()
                    if carta:
                        jugador.agregar_carta(carta)
                        print(f"Te han dado: {carta}")
                        if jugador.puntos > 7.5:
                            print(f"¡Te has pasado! {jugador.nombre} pierde.")
                            break
                    else:
                        print("La baraja está vacía. No hay más cartas para repartir.")
                        break
                elif opcion == 'n':
                    print(f"{jugador.nombre} se queda con {jugador.puntos} puntos.")
                    break
                else:
                    print("Opción no válida. Por favor, ingresa 's' o 'n'.")
        
            print(f"\n{jugador.nombre} termina su turno con {jugador.puntos} puntos.")
            input("Presiona Enter para continuar al siguiente jugador.")

        def jugar(self):
            self.repartir_cartas_iniciales()
        
            for jugador in self.jugadores:
                self.turno_jugador(jugador)
        
            self.determinar_ganador_y_perdedor()

        def determinar_ganador_y_perdedor(self):
            jugadores_validos = [jugador for jugador in self.jugadores if jugador.puntos <= 7.5]
        
            if not jugadores_validos:
                print("\nTodos los jugadores se han pasado de 7.5. No hay ganador.")
                self.confirmar_salida()
                return
        
            ganador = max(jugadores_validos, key=lambda j: j.puntos)
            print(f"\nEl ganador es {ganador.nombre} con {ganador.puntos} puntos.")
        
            perdedor = min(jugadores_validos, key=lambda j: j.puntos)
        
            print(f"El perdedor es {perdedor.nombre} con {perdedor.puntos} puntos.")
        
            self.confirmar_salida()

        def confirmar_salida(self):
            print("\n¿Quieres salir del juego? (s/n): ", end="")
            opcion = input().strip().lower()
            if opcion == 's':
                print("¡Gracias por jugar!")
                sys.exit(0)
            else:
                print("Volviendo al menú principal...")
                input("Presiona Enter para continuar...")
                menu_principal()  

    def mostrar_como_se_juega():
        limpiar_consola()
        print("Cómo se juega:")
        print("1. El juego trata de acercarse a un total de 7.5 puntos sin pasarse.")
        print("2. Cada jugador recibe una carta al inicio y puede pedir más cartas durante su turno.")
        print("3. Las cartas tienen los siguientes valores:")
        print("   - Las cartas numéricas tienen su valor (2-7).")
        print("   - La Sota, Caballo y Rey valen 0.5 puntos.")
        print("   - El As vale 1 punto.")
        print("\n¡Buena suerte!")
        input("\nPresiona Enter para volver al menú.")

    def mostrar_creditos():
        limpiar_consola()
        print("Créditos:")
        print ("Desarrollo:\n- Juan R: Programador Principal. \n- Carlos P: Programador Secundario. \n- Rony M: Programador Secundario\n\nInformación Legal:\n© 2024 StarLight. Todos los derechos reservados.")
        print("¡Gracias por jugar!")
        input("\nPresiona Enter para volver al menú.")

    def menu_principal():
        while True:
            limpiar_consola()
            print("\t~~~ Menú de Siete y Medio ~~~\n")
            print("1. Cómo se juega")
            print("2. Jugar")
            print("3. Créditos")
            print("4. Salir")
        
            opcion = input("Selecciona una opción: ").strip()

            if opcion == '1':
                mostrar_como_se_juega()
            elif opcion == '2':
                jugadores = input("Introduce los nombres de los jugadores separados por coma: ").split(',')
                jugadores = [nombre.strip() for nombre in jugadores]
                juego = Juego(jugadores)
                juego.jugar()
            elif opcion == '3':
                mostrar_creditos()
            elif opcion == '4':
                print("¡Gracias por jugar!")
                limpiar_consola()
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
                input("Presiona Enter para continuar...")

    if __name__ == "__main__":
        menu_principal()
def menu():
    while True:
        print("\t ==== Mesa de Juegos ====\n")
        num = input(" #1 Guerra \n #2 Siete y Medio \n #3 Salir \n\n\n# ")

        if num == "1":
            guerraPOO()
        elif num == "2":
            juego_sieteymedio()
        elif num == "3":
            break
menu()
