# Aqui podemos almacenar la respuesta, que es la longitud
# del nombre mas largo

	# Aqui puedes ocupar la funcion max(res,a) 
	# que devuelve el maximo entre res y a 
	# O puedes hacer un if
large = 0
for i in range(10):
    word = raw_input()
    if len(word)> large:
        large =len(word)
print "El nombre mas largo tiene "+str(large)+" letras."
