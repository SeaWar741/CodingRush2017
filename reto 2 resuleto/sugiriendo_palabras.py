s = raw_input()
ans = ""
for i in range(len(s)):
#expression short circuiting
    if i == 0 or s[i] != s[i-1] or ((i == len(s) or s[i]!= s[i+1]) and (i<= 1 or s[i]!=s[i-2])):
        ans += s[i]
print ans

#solucion 2
