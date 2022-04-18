def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    bolunen = [] #yeni bir dize oluştur
    for x in range(min_sayi, max_sayi): #minimum sayı ile maximum sayı arasındaki bütün sayıları dön
        if x % bolunecek_sayi == 0: #eger değer bolunecek_sayıyla bölünebiliyorsa
            bolunen.append(x) #bolunen dizisine ekle
    print(bolunen) #bolunen dizeyi yazdır


bolunenSayiBulma(1, 100, 5)
