#lab1.10

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))


if x > y:
    if x>z:
        if y>z:
            print(f"your number: {z},{y},{x}")
        else:
            print(print(f"your number: {y},{z},{x}"))
    else:
        print(print(f"your number: {y},{x},{z}"))
else:
    print(print(f"your number: {x},{z},{y}"))