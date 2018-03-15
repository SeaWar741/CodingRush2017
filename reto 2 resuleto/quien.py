calificacion_a = [0.0,0.0,0.0]
cala= 0
calb= 0
calificacion_b = [0.0,0.0,0.0]
n = 3
for i in range (n):
    number = float(raw_input())
    calificacion_a[i] = number
for i in range (n):
    number = float(raw_input())
    calificacion_b[i] = number
for i in range (n):
    if calificacion_a[i] < calificacion_b[i]:
        calb =calb+1
    elif calificacion_a[i]> calificacion_b[i]:
        cala= cala +1
        
if cala < calb:
    print "Gano B"
elif cala == calb:
    print "Hubo empate"
elif cala > calb:
    print "Gano A"

#segunda solucion posible:
    
a = []
b = []
for i in range (3):
    a +=[float(raw_input()]
for i in range (3):
    b +=[float(raw_input()]
         
for i in range (n):
    if calificacion_a[i] < calificacion_b[i]:
        calb =calb+1
    elif calificacion_a[i]> calificacion_b[i]:
        cala= cala +1

if cala < calb:
    print "Gano B"
elif cala == calb:
    print "Hubo empate"
elif cala > calb:
    print "Gano A"
