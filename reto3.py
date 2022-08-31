edad= int(input("Digite su edad: "))

#PROCESO
if(edad >=0 and edad <14):
    print(f'Para la edad de {edad} es un niño')
elif(edad >=14 and edad <28):
    print(f'Para la edad de {edad} es un joven')
elif(edad >=28 and edad <60):
     print(f'Para la edad de {edad} es un adulto')
elif(edad >=60 and edad<150):
    print(f'Para la edad de {edad} es un adulto mayor')
else:
    print("Edad invalida")

#SALIDA: Son los print de arriba 