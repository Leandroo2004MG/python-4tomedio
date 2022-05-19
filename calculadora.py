#Aqui puse que escogamos una opcion del 1 al 5 y utilize el while
opcion = 1
while opcion != 5:
    print("introduce una opcion: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input())
#aqui puse que colocara dos numeros, puede ser calquier numero
    print("introduce el primer numero")
    n1 = int(input())
    print("introduce el segundo numero")
    n2 = int(input())
#aqui puse los calculos y opciones con if y elif
    if opcion == 1:
        Suma = n1+n2
        print(str(Suma))
    elif opcion == 2:
        Restar = n1-n2
        print(str(Restar))
    elif opcion == 3:
         Multiplicar = n1*n2
         print(str(Multiplicar))
    elif opcion == 4:
         Dividir = n1/n2
         print(str(Dividir))
    elif opcion == 5:
#aqui puse que ya termino el calculo
        print("terminando")
