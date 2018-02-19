# Las lineas que tienen el signo de gato son comentarios
# no pasa nada si los dejas o los eliminas!
# -----------------------------------
# Tienes que leer n datos 
n= int(raw_input())
# Necesitar llevar un acumulado?
tiempo = 0
for i in range(n):
    t = int(raw_input())
    tiempo = tiempo + t
#Esta linea no la muevas, es para imprimir en el formato correcto
print round(tiempo/7.0,4)