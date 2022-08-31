#ENTRADA= VARIABLES=REFERENCIAS EN MEMORIA
nivelagua=int(input("Digite el nivel de agua: "))

#PROCESO
if(nivelagua>=0 and nivelagua<20):
    print(f'El nivel del agua es {nivelagua} y este es bajo')
elif(nivelagua>=20 and nivelagua<400):
    print(f'El nivel del agua es {nivelagua} y este es adecuado')
elif(nivelagua>=400):
    print(f'El nivel del agua es {nivelagua} y este es alto')
else:
    print("El nivel del agua no es valido")

#SALIDA: Son los print de arriba 