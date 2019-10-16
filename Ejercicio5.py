frase=(input("Ingresa una frase "))
longitud=len(frase)
contespa=0
contcar=0
for i in range(0,longitud):
    if(frase[i].isspace()):
        contespa+=1
    else:
        contcar+=1
print("Número de caracteres = ",contcar)
print("Número de espacios = ", contespa)