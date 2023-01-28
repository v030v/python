'''
for i in range(2,10,1):
    for j in range(1,10,1):
        print(i,j,i*j)

for i in range(1,6,1):
    for j in range(i):
        print("*", end="")
    print()

i=2
j=1
while(i<9):
    while(j<10):
        print(i,j,i*j)
        j+=1

i=2
while(i<10):
    for j in range(1,10,1):
        print(i,j,i*j)
    i+=1
   
i=1
while(i<6):
    for j in range(i):
        print("*",end="")
    print()
    i+=1

i=2
j=1
while(i<10):
    while(j<10):
        print(i,j,i*j)
        j+=1
    print("")
    i+=1
    j=1

i=1
j=1
while(i<6):
    while(j<i+1):
        print("*",end="")
        j+=1
    print("")
    i+=1
    j=1

i=0

while(i<5):
    j=0
    while(j<i):
        print("O",end="")
        j+=1
    print("*")
    i+=1
'''
