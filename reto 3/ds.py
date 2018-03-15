k = int(raw_input())
numb = {}
for i in range(k):
    number = raw_input()
    if len(number)%2 == 0:
        numb[number]="SI"
    else:
        numb[number]="NO"
for key, value in numb.iteritems() :
    print value
        
    
