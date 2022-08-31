#ENTRADA= VARIABLES=REFERENCIAS EN MEMORIA
mesdigitado=input("Digite el mes: ")
mes= mesdigitado.lower()

#PROCESO
if(mes=="enero" or mes=="febrero" or mes=="marzo"):
    print(f'En el mes de {mes} es invierno')
elif(mes=="abril" or mes=="mayo" or mes=="junio"):
    print(f'En el mes de {mes} es primavera')
elif(mes=="julio" or mes="agosto" or mes="septiembre"):
    print(f'En el mes de {mes} es verano')
elif(mes=="octubre" or mes=="noviembre" or mes="diciembre"):
    print(f'En el mes de {mes} es otoño')
else:
    print("Mes invalido")

#SALIDA: Son los print de arriba 