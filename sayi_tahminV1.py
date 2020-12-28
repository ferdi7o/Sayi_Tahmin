print("Bil bakalim kac sayisini tuttum (0-100)?")
tahmin_sayisi = 23


while True:
    kullanici = int(input("Tahmin Sayiniz:"))
    if (tahmin_sayisi > kullanici):
         print("Daha Buyuk!")
    elif (100 < kullanici):
        print("Lutfen 100'den buyuk sayi girmeyin!")
    elif (tahmin_sayisi < kullanici):
        print("Daha Kucuk!")
    elif (tahmin_sayisi == kullanici):
        print("Tebrikler Bildiniz...")
        break
    