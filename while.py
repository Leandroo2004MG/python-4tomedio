mensaje = 'cuantos juegos vendi o (-1) para salir: '
total = 0
contar = 0
ventas = int(input(mensaje))
while ventas != -1:
    total = total+ventas
    contar += 1
    ventas = int(input(mensaje))
else:
    promedio = total/contar
    print("El total de ventas: " + str(promedio))
