#Escribir un programa que pregunte al usuario su edad
#y muestre por pantalla si es mayor de edad o no.
#https://aprendeconalf.es/docencia/python/ejercicios/condicionales/#ejercicio-1

age = int(input('Digite su edad: '))

if age >= 18:
    print(f'You have {age}, you are an adult')
elif age <= 18:
    print(f'You have {age}, you are not an adult')
else:
    print(f'Thats not an age')