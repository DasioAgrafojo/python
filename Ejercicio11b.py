import re
dni = input('Dame un DNI: ')
dniparameters = r'^[0-9]{8}[a-zA-Z]{1}'
match = re.search(dniparameters, dni)
if match:
 print(dni + ' es un DNI válido.')
else:
 print(dni + ' no es un DNI válido.')