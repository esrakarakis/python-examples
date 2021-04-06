def ortalama(vize1, vize2, final):
    toplam_not = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
    if vize1 > 100 or vize2 > 100 or final > 100:
        print("girilen notlar 100'den büyük olamaz")
    else:
        if toplam_not > 100:
            print("toplam not 100'den büyük olamaz")
        elif toplam_not >= 90:
            print("AA")
        elif toplam_not >= 85:
            print("BA")
        elif toplam_not >= 80:
            print("BB")
        elif toplam_not >= 75:
            print("CB")
        elif toplam_not >= 70:
            print("CC")
        elif toplam_not >= 65:
            print("DC")
        elif toplam_not >= 60:
            print("DD")
        elif toplam_not >= 55:
            print("FD")
        elif toplam_not < 55:
            print("FF")

ortalama(40,81,89)
