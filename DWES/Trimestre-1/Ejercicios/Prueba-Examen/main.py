# Ejercicio 1
# numero = int(input('Numero positivo: '))
# if numero > 0:
#     numSuma = 0
#     while numSuma < numero:
#         sumador = int(input('Numero: '))
#         numSuma += sumador
# else:
#     print('Pon un numero positivo')

# Ejercicio 2:
print('El primer numero debe ser mayor al segundo\n')
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))

if num2 > num1:
    for i in range(num1, num2+1):
        if i % 2 == 0:
            print(f'{i} es par')
        else:
            print(f'{i} es inpar')
else:
    print('El primer numero debe ser mayor!!!!!!!!!!!')
    
    