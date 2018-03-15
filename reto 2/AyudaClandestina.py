# Aqui podemos guardar el texto
oracion = raw_input()
#Aqui podemos guardar la respuesta
total = 0
for caracter in oracion:
    if caracter == "1":
        total = total +1
    if caracter == "2":
        total = total +2
	#Tenemos que chechar si es 1 o 2 no?
print  total
