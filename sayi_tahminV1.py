def sayitahmin():
    import random

    print("Bil bakalim kac sayisini tuttum (0-100)?")
    tahmin_sayisi = random.randint(0,100)
    liste = []

    while True:
        kullanici = int(input("Tahmin Sayiniz:"))
        liste.append(kullanici)

        if (tahmin_sayisi > kullanici):
             print("Daha Buyuk!",liste ,"\n")
        elif (5 == len(liste)):
            print("Kaybettiniz!\nTuttugum sayi:",tahmin_sayisi,"Sizin tahmin sayilariniz:",liste)
            break

        elif (100 < kullanici):
            print("Lutfen 100'den buyuk sayi girmeyin!")
        elif (tahmin_sayisi < kullanici):
            print("Daha Kucuk!",liste , "\n")
        elif (tahmin_sayisi == kullanici):
            print("Tebrikler Bildiniz..." , len(liste) ," denemede buldunuz.")
            break




sayitahmin()