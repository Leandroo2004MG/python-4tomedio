#Lo que hice aqui fue poner print y el nombre que es "maquina de sueldo liguido".
print("maquina de sueldo liquido")
#Despues le puse nombre, sueldo, afp, prevision, seguro y use el int y intput para poner los datos
nombre = input("introduce su nombre: ")
sueldo = int(input("introduce el sueldo bruto: "))
afp = int(input("introduce su afp: "))
prevision = (input("es fonasa o isapre? "))
seguro = int(input("su seguro de cesantia: "))
#Despues hice que escogieramos una opcion de calculo y agregamos el while
opcion = 1
while opcion != 3:
    print("introduce una opcion: ")
    print("1. calcular sueldo imposible")
    print("2. calcular los descuentos")
    print("3. salir")
    opcion = int(input())
    break
#Despues les puse print y ahora calcule
print("ahora calcula")
#Despues puse los porcentaje de afp, fonasa, isapre y seguro
afp = 5
afp1 = 5/100

fonasa = 5
fonasa1 = 5/100

isapre = 5
isapre1 = 5/100

seguro = 5
seguro1 = 5/100
#Despues puse que colocamos una de las opciones.
print("introduce la primera opcion")
n1 = int(input())
print("introduce la segunda opcion")
n2 = int(input())
#Despues utilize el if y elif para los calculos
if opcion == 2:
   sueldoafp = sueldo*afp1
   print(str(sueldoafp))
elif opcion == 2:
   sueldofonasa = sueldo*fonasa1
   print(str(sueldofonasa))
elif opcion == 2:
   sueldoisapre = sueldo*isapre1
   print(str(sueldoisapre))
elif opcion == 2:
   sueldoseguro = sueldo*seguro1
   print(str(sueldoseguro))
#Despues de hacer esto me di cuenta de algunos errores que cometi.