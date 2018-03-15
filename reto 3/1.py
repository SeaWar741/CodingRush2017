si = raw_input()
s2 = raw_input()
an = 0
for caracter in si:
    if caracter in s2:
        an = 1
    else:
        an = 0
if an == 1:
    print "ANAGRAMA!"
else:
    print "No :("
