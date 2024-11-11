#a

ile=int(input("how much line "))

for i in range(ile):
    for i in range(ile):
        print("*", end=" ")
    print("")


#b

ile = int(input("how much line "))

for i in range(ile):
    for j in range(i+1):
        print("*", end=" ")
    print("")



#c
ile = int(input("how much line "))
spc = ile - 1
for i in range(ile):
    print(" " * spc, end= "")
    spc -= 1
    for j in range(i+1):
        print("*",end=" ")
    print("")




