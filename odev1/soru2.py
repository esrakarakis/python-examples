def sayiAtama(sayi):
    if 100 > sayi > 9:
        sayiOkunusu(sayi)
    else:
        print("Verilen Sayı iki basamaklı olmalıdır")


def sayiOkunusu(sayi):
    birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

    birinci = sayi % 10 #birler basamağını bulabilmek için sayıyı 10 a bölündüğündeki katsayıyı bul.
    ikinci = sayi // 10 #onlar basamağını bulabilmek için sayıyı 10 a böl küsuratı at.

    print(onlar[ikinci] + " " + birler[birinci])

sayiAtama(79)
