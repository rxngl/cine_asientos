filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))

sala =[]

for i in range(filas):
    fila= []

    for j in range(columnas):
        fila.append("L")

    sala.append(fila)

def mostrar_sala():

    print("\n========== SALA DE CINE ==========")
    print("             PANTALLA")
    print("----------------------------------")

    for i in range(filas):

        print(f"Fila {i + 1}: ", end="")

        for j in range(columnas):
            print(sala[i][j], end="  ")

        print()

    print("----------------------------------")
    print("L = Libre | X = Ocupado")

def reservar_asiento():

    mostrar_sala()

    fila=int(input("\nIngrese la fila: "))
    columna=int(input("Ingrese la columna: "))

    if fila < 1 or fila > filas or columna < 1 or columna > columnas:

        print("\nEl asiento seleccionado no existe")

    else:
        fila =fila - 1
        columna=columna - 1

        if sala[fila][columna]=="L":

            sala[fila][columna]="X"
            print("\nAsiento reservado correctamente!")

        else:

            print("\nEl asiento ya se encuentra ocupado")

def liberar_asiento():

    mostrar_sala()

    fila=int(input("\nIngrese la fila: "))
    columna=int(input("Ingrese la columna: "))

    if fila < 1 or fila > filas or columna < 1 or columna > columnas:

        print("\nEl asiento seleccionado no existe")

    else:
        fila=fila - 1
        columna=columna-1

        if sala[fila][columna]=="X":

            sala[fila][columna]="L"
            print("\n¡Asiento liberado correctamente!")

        else:

            print("\nEl asiento ya se encuentra libre")

def contar_asientos():

    libres=0
    ocupados=0

    for i in range(filas):

        for j in range(columnas):

            if sala[i][j]=="L":

                libres += 1

            elif sala[i][j]=="X":

                ocupados+=1

    print("\n========== ESTADISTICAS ==========")
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}")
    print(f"Total de asientos: {libres + ocupados}")

while True:
    print("==================================")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion=input("\nSeleccione una opcion: ")

    if opcion=="1":

        mostrar_sala()

    elif opcion=="2":

        reservar_asiento()

    elif opcion=="3":

        liberar_asiento()

    elif opcion=="4":

        contar_asientos()

    elif opcion=="5":

        print("Hasta pronto!")
        break

    else:

        print("\nOpcion no valida. Intente nuevamente.")