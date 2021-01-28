#Escribir un programa que almacene la cadena de caracteres
#contraseña en una variable, pregunte al usuario por la contraseña e imprima
#por pantalla si la contraseña introducida por el usuario coincide con la
#guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/#ejercicio-2

password = 'password'
second = input('Write your password: ')

if second == password:
    print(f'Password is correct')

else:
    print(f'Wrong password')