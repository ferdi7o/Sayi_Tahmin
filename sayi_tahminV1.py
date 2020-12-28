print("Bil bakalim kac sayisini tuttum (0-100)?")
tahmin_sayisi = 23

kullanici = int(input("Tahmin Sayiniz:"))

if (tahmin_sayisi > kullanici):
    print("Daha Buyuk!")
elif (tahmin_sayisi < kullanici):
    print("Daha Kucuk!")
elif (tahmin_sayisi == kullanici):
    print("Tebrikler Bildiniz...")