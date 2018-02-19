m = int(raw_input())
for i in range(m):
    numb = int(raw_input())
    x = 1
    total = 0
    if numb != 1:
        while x < numb+1:
            suma = ((2*x)-1)
            total = total + suma
            x = x+1
    else:
        total = 1
    print total
    if total == numb * numb:
        print "* o *"
    else:
        print ":C"