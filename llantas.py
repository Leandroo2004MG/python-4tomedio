cliente=input("ingrese su nombre: ")
compras=int(input("ingrese el numero de llantas compradas: "))
valor1=250
valor2=220

c1=(valor1*compras)
c2=(valor2*compras)
menor12=0.20
mayor12=0.25
totald1=(c1-0.20)
totald2=(c2-0.25)
compras<12:

print(f"tu total de llantas compradas es: {c1}, y con tu descuento de: {menor12}")
print("tu costo total es: totald1")