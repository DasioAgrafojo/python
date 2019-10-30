import re
email = input('Dame un correo: ')
emailRegex = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+[.][a-zA-Z0-9]{2,3}'
match = re.search(emailRegex, email)
if match:
 print(email + ' es una dirección válida.')
else:
 print(email + ' no es una dirección válida.')