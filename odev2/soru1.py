class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi


class Soru:
    def __init__(self, dogru, yanlis):
        self.dogru = dogru
        self.yanlis = yanlis

    def NetSayisi(self):
        if self.yanlis >= 4:
            dusulecekNet = self.yanlis // 4
        else:
            dusulecekNet = 0
        return self.dogru - dusulecekNet

    def PuanHesapla(self):

        dogruCevap = self.NetSayisi()

        return str(dogruCevap * 2)


ogrenci_1 = Ogrenci("Zehra", "Yaprak", "4A")

ogrenci_1_puan = Soru(47, 3)

ogrenci_2 = Ogrenci("Ali", "Ağaç", "4A")

ogrenci_2_puan = Soru(20, 30)

print(
    ogrenci_1.ogrenciAdi + " " + ogrenci_1.ogrenciSoyadi + " isimli öğrenci " + ogrenci_1.ogrenciSinifi + " sınıfında okumaktadır ve " + ogrenci_1_puan.PuanHesapla() + " almıştır")

print(
    ogrenci_2.ogrenciAdi + " " + ogrenci_2.ogrenciSoyadi + " isimli öğrenci " + ogrenci_2.ogrenciSinifi + " sınıfında okumaktadır ve " + ogrenci_2_puan.PuanHesapla() + " almıştır")
