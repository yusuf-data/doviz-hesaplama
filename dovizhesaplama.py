print("1-Dolar")
print("2-Euro")

secim = input("Seçimin: ")

if secim == "1":
    print("Dolar Seçtiniz.")
    miktar = float(input("Kaç Dolarınız Var?: "))
    tl = miktar * 45

elif secim == "2":
    print("Euro Seçtiniz.")
    miktar = float(input("Kaç Euro'nuz Var?: "))
    tl = miktar * 50

else:
    print("Geçersiz İşlem")
    tl = 0

print("Elinizdeki paranın değeri:", round(tl, 2), "TL'dir.")