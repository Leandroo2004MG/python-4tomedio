nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2])
print(nombres[:3])
print(nombres[1])
nombres[3] = "ivone"
print(nombres)
for nombre in nombres:
    print(nombre)
else:
    print("no existe mas nombres en la lista")
print(len(nombres))
nombres.append("Lorenzo")
print(nombres)
nombres.insert("Octavio")
print(nombres)
nombres.remove("Octavio")
print(nombres)
nombres.pop()
print(nombres)
del nombres[0]
print(nombres)
nombres.clear()
print(nombres)
del nombres
print(nombres)