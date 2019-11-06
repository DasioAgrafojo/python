option = "0"

while (option!="1" and option!="2" and option!="3" ):
    option=input('Qué objeto quieres calcular? \n1-> Cubo\n2-> Esfera\n3-> Cilindro\n')

if option=="1":
    print('Cubo seleccionado')
    AristaCubo= int (input('Dame la medida de las aristas: '))
    VolCubo= ( AristaCubo ** 3)
    print ('Su volumen es ', VolCubo)

elif option=="2":
    print('Esfera seleccionada')
    RadioEsfera= int (input('Dame la medida del radio: '))
    VolEsfera= (4.2*(RadioEsfera**3))
    print ('Su volumen es ', VolEsfera)
else :
    print('Cilindro seleccionado')
    RadioCilindro= int (input('Dame el radio del cilindro: '))
    AlturaCilindro= int (input('Dame la altura del cilindro: '))
    VolCilindro= (AlturaCilindro*RadioCilindro*6.2832)
    print ('Su volumen es ', VolCilindro)
