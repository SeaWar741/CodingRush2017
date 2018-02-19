numb = str(raw_input())
i=0
total = False
while i < len(numb):
    if numb[i] == "1" or numb[i] == "0":
        total = True
    else:
        total = False
    i += 1
    
if total == True:
    print "parece binario"
else:
    print "no parece binario"