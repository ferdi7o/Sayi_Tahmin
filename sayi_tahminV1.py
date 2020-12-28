def sayitahmin():
    import random
    name = input("Isminizi giriniz:")
    print( name ,"bil bakalim kac sayisini tuttum (0-100)?")
    tahmin_sayisi = random.randint(0,100)
    liste = []
    players = open("players.txt","a")

    while True:
        kullanici = int(input("Tahmin Sayiniz:"))
        liste.append(kullanici)

        if (tahmin_sayisi > kullanici):
             print("Daha Buyuk!",liste ,"\n")
        elif (100 < kullanici):
            print("Lutfen 100'den buyuk sayi girmeyin!")
        elif (tahmin_sayisi < kullanici):
            print("Daha Kucuk!",liste , "\n")
        elif (tahmin_sayisi == kullanici):
            print("Tebrikler Kazandın." , name , len(liste) ,"denemede buldu.")
            ekle = (name + " - " + str(len(liste)) + "\n")
            players.write(ekle)
            break




sayitahmin()