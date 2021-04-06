class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad + " " + self.soyad + " " + str(self.yas) + " " + self.ulke + " " + self.sehir + " " + str(
            self.yetenekler)

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


kisi = Insan("Zehra", "Çiçek", 27, "Türkiye", "Istanbul")
print(kisi.kisi_bilgileri())

kisi.yetenek_ekle("Piyano çalmak")
print(kisi.kisi_bilgileri())

print(kisi.yetenekler)
