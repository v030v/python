'''
i=0
while(i<5):
    j=0
    while(j<i+1):
        j+=1
        print("*",end="")
    print("")
    i+=1

i=0
while(i<5):
    j=0
    while(j<5):
        if (j<5-(i+1)):
            print("  ", end="")
        else:
                print("*",end="")
        j+=1
    print("")
    i+=1
'''
i=0
while (i<5):
    j=0
    while(j<i+1):
        j+=1
        print("*", end="")
    while(j<5):
        j+=1
        print("0",end="")
    print("")
    i+=1

