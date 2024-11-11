#lab1.8

a = int(input('What is your age: '))
print(a)

if a > 18:
    print('You are adult')
elif 12 < a <= 18:
    print('you are teenager')
else:
    print('you are kid')