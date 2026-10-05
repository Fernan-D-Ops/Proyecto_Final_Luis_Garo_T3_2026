# Cartelera basada en Caribbean Cinemas en Octubre 2026:
cartelera = {
    "Lunes": [
        {"pelicula": "Digger", "sala": 1, "horario": "2:00 pm", "formato": "Normal"},
        {"pelicula": "Verity", "sala": 2, "horario": "4:30 pm", "formato": "3D"},
        {"pelicula": "Spider-Man: Brand New Day", "sala": 3, "horario": "6:00 pm", "formato": "4DX"},
        {"pelicula": "Los Rechazados 2", "sala": 4, "horario": "5:30 pm", "formato": "Normal"},
        {"pelicula": "Coyote vs Acme", "sala": 5, "horario": "8:00 pm", "formato": "CXC"},
    ],
    "Martes": [
        {"pelicula": "Digger", "sala": 3, "horario": "5:00 pm", "formato": "4DX"},
        {"pelicula": "Verity", "sala": 1, "horario": "7:00 pm", "formato": "Normal"},
        {"pelicula": "Spider-Man: Brand New Day", "sala": 2, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Los Rechazados 2", "sala": 5, "horario": "6:30 pm", "formato": "3D"},
        {"pelicula": "Coyote vs Acme", "sala": 4, "horario": "9:00 pm", "formato": "Normal"},
    ],
    "Miércoles": [
        {"pelicula": "Digger", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Verity", "sala": 5, "horario": "2:30 pm", "formato": "CXC"},
        {"pelicula": "Spider-Man: Brand New Day", "sala": 1, "horario": "7:30 pm", "formato": "3D"},
        {"pelicula": "Los Rechazados 2", "sala": 2, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "Coyote vs Acme", "sala": 3, "horario": "8:30 pm", "formato": "4DX"},
    ],
    "Jueves": [
        {"pelicula": "Digger", "sala": 2, "horario": "6:30 pm", "formato": "3D"},
        {"pelicula": "Verity", "sala": 3, "horario": "3:30 pm", "formato": "Normal"},
        {"pelicula": "Spider-Man: Brand New Day", "sala": 4, "horario": "8:00 pm", "formato": "Normal"},
        {"pelicula": "Los Rechazados 2", "sala": 1, "horario": "2:00 pm", "formato": "4DX"},
        {"pelicula": "Coyote vs Acme", "sala": 5, "horario": "5:30 pm", "formato": "CXC"},
    ],
    "Viernes": [
        {"pelicula": "Digger", "sala": 5, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Verity", "sala": 4, "horario": "7:00 pm", "formato": "3D"},
        {"pelicula": "Spider-Man: Brand New Day", "sala": 1, "horario": "5:30 pm", "formato": "CXC"},
        {"pelicula": "Los Rechazados 2", "sala": 3, "horario": "9:00 pm", "formato": "Normal"},
        {"pelicula": "Coyote vs Acme", "sala": 2, "horario": "2:30 pm", "formato": "4DX"},
    ],
    "Sábado": [
        {"pelicula": "Digger", "sala": 1, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Verity", "sala": 2, "horario": "6:00 pm", "formato": "4DX"},
        {"pelicula": "Spider-Man: Brand New Day", "sala": 5, "horario": "8:30 pm", "formato": "3D"},
        {"pelicula": "Los Rechazados 2", "sala": 4, "horario": "4:30 pm", "formato": "Normal"},
        {"pelicula": "Coyote vs Acme", "sala": 3, "horario": "7:30 pm", "formato": "CXC"},
    ],
    "Domingo": [
        {"pelicula": "Digger", "sala": 3, "horario": "2:30 pm", "formato": "3D"},
        {"pelicula": "Verity", "sala": 5, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "Spider-Man: Brand New Day", "sala": 2, "horario": "7:00 pm", "formato": "CXC"},
        {"pelicula": "Los Rechazados 2", "sala": 1, "horario": "8:30 pm", "formato": "4DX"},
        {"pelicula": "Coyote vs Acme", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
    ],
}

#Definimos una funcion para crear las salas vacias
def sala_vacia():
    return [
             [".", ".", ".", ".", ".", "."], #Fila 0 (A)
             [".", ".", ".", ".", ".", "."], #Fila 1 (B)
             [".", ".", ".", ".", ".", "."], #Fila 2 (C)
             [".", ".", ".", ".", ".", "."], #Fila 3 (D)
             [".", ".", ".", ".", ".", "."], #Fila 4 (E)            
        ]

#Bucle para generar las salas
for dia in cartelera:
    for proyeccion in cartelera[dia]:
        # A cada proyeccion le inyectamos una key nueva con su propia matriz de sala independiente.
        proyeccion["asientos"] = sala_vacia()

#Variables que estaremos utilzando para almenar informacion:
dia_seleccionado =""
intentos = 0

def preguntar_continuar(accion_personalizada): # Para evitar repetir codigo utilizaremos esta funcion
    respuesta = input(f"\n¿Desea volver al menú principal (1) o {accion_personalizada} (2)? ")
    
    if respuesta == "1":
        return False # Falso: No quiere continuar aquí, quiere volver al menú
    else:
        return True  # Verdadero: Quiere repetir la opción actual

def menu_cine():
    print ("""
   ---------------------------
   |  Bienvenido a CINEMAX!  |
   |El mejor cine del caribe.|
   ---------------------------

   1. Ver Cartelera de un día
   2. Mostrar asientos de una funcion
   3. Reservar asientos
   4. Cancelar asientos
   5. Ver disponibilidad
   6. Salir
   """)

    while True:
      
        opcion = int(input("\n En que podemos ayudarlo hoy? "))

        if opcion == 1:
            while True:
                dia_seleccionado = input("De que dia desea ver la catelera? ").title()
                if dia_seleccionado in cartelera:
                    print (f"\n --- Esta es la cartelera del {dia_seleccionado} --- ")
                    for proyeccion in cartelera[dia_seleccionado]:
                        print(f"{proyeccion['pelicula']}, Sala {(proyeccion['sala'])}, {proyeccion['horario']}, {proyeccion['formato']} ")
                    if preguntar_continuar("Consultar la cartelera de otro dia"):
                        continue
                    else:
                       break 
                else:
                    print("\n Este dia no es valido, favor de intentarlo nuevamente")
            
        elif opcion == 2:
            while True:
                dia_seleccionado = input("Para que dia desea visualizar los asientos? ").title()
                existencia_sala = int(input("Cual sala desea validar? "))
                existencia_horario = input("Que horario desea validar? ")

                for proyeccion in cartelera[dia_seleccionado]:
                    if proyeccion["sala"] == existencia_sala and proyeccion["horario"] == existencia_horario:
                        print("  1   2   3   4   5   6") # Filas de asientos
                        indice = 0 # Gracias a esta vareable recorremos la lista de letras, para utilizarla en los asientos
                        letras = ["A", "B", "C", "D", "E"]
                        for asientos in proyeccion["asientos"]:
                            print(f"{letras[indice]} {'   '.join(asientos)}") # Unimos la variable 'asientos' separada por un espacio
                            indice +=1 # Le sumamos 1 al índice para que la siguiente vuelta use la próxima letra
                    
                if preguntar_continuar("Visualizar los asientos de otro dia"):
                    continue
                else:
                     break   
            

        elif opcion == 3:
            dia_seleccionado = input("Para que dia desea reservar? ").title()
            existencia_sala = int(input("En cual sala? "))
            existencia_horario = input("En cual horario? ")
        
            for proyeccion in cartelera[dia_seleccionado]:
                if proyeccion["sala"] == existencia_sala and proyeccion["horario"] == existencia_horario:
                    print("  1   2   3   4   5   6") # Filas de asientos
                    indice = 0 # Gracias a esta vareable recorremos la lista de letras, para utilizarla en los asientos
                    letras = ["A", "B", "C", "D", "E"]
                    for asientos in proyeccion["asientos"]:
                        print(f"{letras[indice]} {'   '.join(asientos)}") # Unimos la variable 'asientos' separada por un espacio\
                        indice +=1 # Le sumamos 1 al índice para que la siguiente vuelta use la próxima letra
                    while True:    
                        reserva_asiento = input("Cual asiento desea reservar? (ej. A2): ").upper()# .Upper para susanar que el user ponga c1, b5, etc..
                        reserva_fila = reserva_asiento[0] #Separamos la respuesta del usuario en filas y columnas
                        reserva_columna = reserva_asiento[1]
                        indice_columna = int(reserva_columna) - 1 #Convertirmos el numero de asiento a int y le restamos 1 para buscarlo en la lista ya que incia desde 0
                        indice_fila = letras.index(reserva_fila) #Con .index buscamos un elemento exacto dentro de la lista "letras" ["A","B" ...] y esto nos da como resultado su indice eje: A = 0
                        if proyeccion["asientos"][indice_fila][indice_columna] == ".": #Evaluamos que el asiento este disponible
                            proyeccion["asientos"][indice_fila][indice_columna] = "X" #Si esta disponible lo reservamos con X
                            print(f"\nSe ha reservado el asiento {reserva_asiento} con exito!")
                        else: #En caso de que el asiento este reservado se lo indicamos al usuario
                            print(f"\n Lo sentimos el asiento {reserva_asiento} no esta disponible")
                        if preguntar_continuar("Volver al menu de reservas"):
                            continue
                        else:
                            break
                        
                    break        

        elif opcion == 4:
            dia_seleccionado = input("Para que dia desea cancelar su reservacion? ").title()
            existencia_sala = int(input("En cual sala? "))
            existencia_horario = input("En cual horario? ")
        
            for proyeccion in cartelera[dia_seleccionado]:
                if proyeccion["sala"] == existencia_sala and proyeccion["horario"] == existencia_horario:
                    print("  1   2   3   4   5   6") # Filas de asientos
                    indice = 0 # Gracias a esta vareable recorremos la lista de letras, para utilizarla en los asientos
                    letras = ["A", "B", "C", "D", "E"]
                    for asientos in proyeccion["asientos"]:
                        print(f"{letras[indice]} {'   '.join(asientos)}") # Unimos la variable 'asientos' separada por un espacio\
                        indice +=1 # Le sumamos 1 al índice para que la siguiente vuelta use la próxima letra
                    while True:    
                        reserva_asiento = input("Para cual asiento desea cancelar su reserva? (ej. A2): ").upper()# .Upper para susanar que el user ponga c1, b5, etc..
                        reserva_fila = reserva_asiento[0] #Separamos la respuesta del usuario en filas y columnas
                        reserva_columna = reserva_asiento[1]
                        indice_columna = int(reserva_columna) - 1 #Convertirmos el numero de asiento a int y le restamos 1 para buscarlo en la lista ya que incia desde 0
                        indice_fila = letras.index(reserva_fila) #Con .index buscamos un elemento exacto dentro de la lista "letras" ["A","B" ...] y esto nos da como resultado su indice eje: A = 0
                        if proyeccion["asientos"][indice_fila][indice_columna] == "X": #Evaluamos que el asiento este reservadp
                            proyeccion["asientos"][indice_fila][indice_columna] = "." #Si esta reservado lo colocamos disponible
                            print(f"\nSe ha cancelado la reserva del asiento {reserva_asiento} con exito!")
                        else: 
                            print(f"\n Lo sentimos el asiento {reserva_asiento} no tiene una reserva la cual cancelar")
                        if preguntar_continuar("Volver al menu de cancelaciones"):
                            continue
                        else:
                            break   
                    break    
            
        elif opcion == 5:
            while True:
                dia_seleccionado = input("De que dia desea saber la disponibilidad? ").title() 
                print (f"\n --- Esta es la disponibilidad del {dia_seleccionado}  --- ")
                if dia_seleccionado in cartelera:

                    for proyeccion in cartelera[dia_seleccionado]:
                        asientos_libres = 0
                        asientos_ocupados = 0
                        print(f"Sala {(proyeccion['sala'])}, {proyeccion['horario']}")
                        for fila_asientos in proyeccion["asientos"]:
                            for asientos_individuales in fila_asientos:
                                if asientos_individuales == ".": 
                                    asientos_libres += 1
                                elif asientos_individuales == "X":  
                                    asientos_ocupados += 1
                                else:
                                    break
                        total_asientos = asientos_libres + asientos_ocupados
                        porcentaje_de_ocupacion = (asientos_ocupados * 100) // total_asientos 
                        print(f"Hay {asientos_libres} asientos libres en esta sala y {asientos_ocupados} ocupados, lo que equivale a un {porcentaje_de_ocupacion}% de ocupacion")
                        
                else:
                    print('\n Ese dia no es valido')
                if preguntar_continuar("Consultar la disponibilidad de otro dia"):
                    continue
                else:
                     break
                

        elif opcion == 6 :
            print("\n Gracias por visitarnos, regreso pronto")
            break

        else:
            print("Esa no es una opcion valida, favor de intentarlo nuevamente")
            intentos += 1
            continue

    else:
        print("Lo sentimos ha llegado al numero maximo de intentos")

   
menu_cine()