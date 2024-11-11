x = int(input("x: "))
y = int(input("y:  "))

if x < y:
    while x<=y:
        if x % 2 == 0:

            print(x)
        x+=1
else:
    while y<=x:
        if y%2 == 0:
            print(y)
            y += 1
        else:
            y += 1
            continue

