def sayitahmin():
    import random

    print("Bil bakalim kac sayisini tuttum (0-100)?")
    tahmin_sayisi = random.randint(0,100)


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



def fordongusu():
    import random
    print("Tahmin etme oyunu 0-100")
    tahmin = random.randint(0,100)
    al = ""

    for dongu in range(5):
        al = int(input("Tahmini sayiniz:"))
        if  (tahmin == al):
            print("Tebrikelr bildiniz")
            break
        elif (tahmin > al):
            print("Daha buyuk")
        elif (tahmin < al):
                print("Daha ufak")
    if (al != tahmin):
        print("Kaybettiniz! Tuttugum sayi:", tahmin)

sayitahmin()