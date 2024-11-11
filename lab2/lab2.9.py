#lab1.9

age = int(input("what is your age?"))

if (age < 0) and (age > 150):
    print("your age are incorrect")
elif age <= 4:
    print("your ticket are free")
elif age <= 18:
    print("your ticket cost 10zl")

else:
    if_student = input("Are you student").lower()
    if (if_student == "yes"):
        print("you ticket cost 15zl")
    else:
        print("your ticket cost 20zl")
