list=["as","kft","ktfs","hfktrg"]
krotka= tuple(list)
print(krotka)

sk = 0
suma = 0
skt = 0
s = int(input("podaj minimalny rozmiar slowa: "))
slowa= []


for el in krotka:
    #A
    suma += len(el)
    #B
    for z in el:
        if z == "k":
            sk +=1
    #C
    if el.find("kt") < 0:
        skt+=1

    #D
    if len(el) >= s:
        slowa.append(el)



print(f"Liczba znakow w krotce to: {suma}")
print(f"w krotce znaleziono: {sk} wystapien/nia litery 'k'")
print(f"w krotce znaleziono: {skt} wystapien/nia ciagu 'kt'")
print(f"slowa o dlugosci wieksej niz {s}, to: ", end=" ")
for s in slowa: print(s, end=", ")

n = 3
x = 6
lista = []
slowo = ""
dlugosc_slowa = 0


for i in range(n):



    lista.append(slowo)

