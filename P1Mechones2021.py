"""
@3N1CM4 ~ github.com/linusmaastok
2021-05-04
Subido DESPUES de entregada la prueba
>> Ayuda para los alumnos tutorados 2021
"""

numerosrolvalidos = 0
numerosinvalidos = 0
numero2021 = 0
while True :
    numero = int(input())
    if numero == 0 : break
    aux = numero
    largo = 0
#SE CALCULA EL LARGO DEL NUMERO
    while aux >= 1 :
        largo += 1
        aux = aux // 10
    aux2 = numero
    digitocontrol = 0
    if largo < 8 or largo > 15:
        flag = False
        numerosinvalidos += 1
    else:
        flag = True
        numerosrolvalidos += 1
#SE SUMAN LOS ROLES VÁLIDOS DE LA PROMOCIÓN 2021
        if (numero % 10000) == 2021 : numero2021 += 1

#PASO 1 y 2
    for i in range(largo,0,-1):
        suma=0
        if i % 2 != 0 : ultdig = aux2 % 10
        if i % 2 == 0 :
            ultdig = (aux2 % 10) * 2
            if ultdig >= 10 :
                ultdig = (ultdig % 10) + (ultdig // 10)
        aux2 = aux2 // 10
        digitocontrol = digitocontrol + ultdig

#PASO 3
    digitocontrol = digitocontrol * 9

#PASO 4
    digitocontrol = digitocontrol % 10 
    if flag: print("{} es un rol PUCV y su dígito de control es {}".format(numero,digitocontrol))
    else: print("{} NO es un rol PUCV".format(numero))

print("-------------------------------------------------------------------------------------------------------------------")
#SE IMPRIME LA CANTIDAD DE ROLES VÁLIDOS
if numerosrolvalidos == 0: print("No se ingresaron Roles PUCV válidos")
elif numerosrolvalidos == 1: print("Se ingresó un Rol PUCV válido")
else: print("Se ingresaron {} Roles PUCV válidos".format(numerosrolvalidos))

#SE IMPRIME LA CANTIDAD DE ROLES NO-VÁLIDOS
if numerosinvalidos == 0: print("No se ingresaron datos NO válidos")
elif numerosrolvalidos == 1: print("Se ingresó un dato NO válido")
else: print("Se ingresaron {} datos NO válidos".format(numerosrolvalidos))

#SE IMPRIME LA CANTIDAD DE ROLES DE LA PROMOCIÓN 2021
if numero2021 == 0: print("No se ingresaron Roles PUCV de la promoción 2021")
elif numero2021 == 1: print("Se ingresó un Rol PUCV de la promoción 2021")
else: print("Se ingresaron {} Roles PUCV de la promoción 2021".format(numero2021))
print("-------------------------------------------------------------------------------------------------------------------")


