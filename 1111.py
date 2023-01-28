'''
c=int(input("class"))
s=int(input("students"))
i = 0
j = 0
tot = 0
while (i<c):
    while(j<s):
        p = int(input("point"))
        tot+=p
        j+=1
    print(tot//s)
    i+=1
    j=0
    tot=0
'''
