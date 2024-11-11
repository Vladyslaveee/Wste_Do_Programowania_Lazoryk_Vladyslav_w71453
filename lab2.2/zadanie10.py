x = int(input("x: "))
y = int(input("y: "))

if x < y:
    while x<=y:
        print(x)
        x+=1
else:
    while y<=x:
        print(y)
        y+=1