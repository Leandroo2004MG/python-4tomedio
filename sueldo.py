sueldo = int(input("ingrese su sueldo"))
s1=(sueldo *0,1)
s2= (sueldo * 0,05)
s3= (sueldo * 0,03)
if sueldo<1000:
    sf1=(sueldo-s1)
    print(f"tu sueldo es: {sueldo}, se te encontrara el: {s1}")
    print(f"tu sueldo final es:,sf1")
elif sueldo <=1000 and sueldo >=2000:
    sf2=(sueldo-s2)
    print(f"tu sueldo es {sueldo}, se te descontara el:{s2}")
    print("tu sueldo final es:,sf2")
elif sueldo=>2000:
    sf3=(sueldo-s3)
    print(f"tu sueldo es: {sueldo}, se te descontara el:{s3}")
    print("tu sueldo final es :",sf3)
else:
    print("ingrese un valor valido")