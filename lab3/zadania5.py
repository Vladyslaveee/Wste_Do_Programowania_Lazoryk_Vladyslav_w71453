"""
#lista zakupow

zakupy = {"chleb":5.0,"maslo":7.0,"czekolada": 12.0, "chipsy": 12.0, "goriwka": 40.0}


#print(zakupy)
suma = 0

for el in zakupy:
    # el -- index/klucz

    suma +=  zakupy[el]
    print(f"{el} za {zakupy[el]} zl")

print(f"za zakupy zaplacimy: {suma}")

