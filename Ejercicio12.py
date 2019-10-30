import sys
option=0
while option!=1 and option!=2 and option!=3:
option=input('Qué objeto quieres calcular? \n1-> Cubo\n2-> Esfera\n3-> Cilindro')

if option==1:
    print('Cubo seleccionado')
elif option==2:
    print('Esfera seleccionada')
else :
    print('Cilindro seleccionado')