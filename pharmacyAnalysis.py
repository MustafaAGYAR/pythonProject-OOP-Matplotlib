import matplotlib.pyplot as plt
import time as h

class Eczane():

    def __init__(self, ilacIsim, ilacTarih, ilacSayisi):

        self.ilacIsim = ilacIsim
        self.ilacTarih = ilacTarih
        self.ilacSayisi = ilacSayisi

    def guncelCıktılarıGoster(self):
        print(f'ilaç ismi: {self.ilacIsim} ilaç tarihi: {self.ilacTarih} rafdaki sayı: {self.ilacSayisi}')

    def tarihİlac(self, tarihGüncelleme):
        print("Tarih Güncellemesi Gerçekleşti")
        self.ilacTarih = tarihGüncelleme

    def stokEkle(self, ilacMiktar):
        print("İlaç Ekleme Gerçekleşti")
        self.ilacSayisi +=ilacMiktar

eczane = Eczane("parol", 2025, 300)
eczane.guncelCıktılarıGoster()

eczane.tarihİlac(2030)
eczane.guncelCıktılarıGoster()

eczane.stokEkle(200)
eczane.guncelCıktılarıGoster()

class ilacToptancısı(Eczane):
    def __init__(self, ilacIsim, ilacTarih, ilacSayisi, hesapKaydı):
        super().__init__(ilacIsim, ilacTarih, ilacSayisi)
        self.hesapKaydı = hesapKaydı

    def guncelCıktılarıGoster(self):
        print(f'ilaç ismi: {self.ilacIsim} ilaç tarihi: {self.ilacTarih} rafdaki sayı: {self.ilacSayisi} hesap kaydı {self.hesapKaydı}')

ilacFirması1=ilacToptancısı("Şurup", 2021, 1000, "5000 TL ödeme çıktısı bulunmaktadır")
ilacFirması1.guncelCıktılarıGoster()

ilacFirması2=ilacToptancısı("Novalgin", 2028, 3000, "100000 TL ödeme çıktısı bulunmaktadır.")
ilacFirması2.guncelCıktılarıGoster()


class Analiz(Eczane):
    def __init__(self, ilacIsim, ilacTarih, ilacSayisi, analizGunu):
        super().__init__(ilacIsim, ilacTarih, ilacSayisi)
        self.analizGunu = analizGunu

    def guncelCıktılarıGoster(self):
        print(f'ilaç ismi: {self.ilacIsim} ilaç tarihi: {self.ilacTarih} rafdaki sayı: {self.ilacSayisi} Anazliz Günü: {self.analizGunu}')

    def analiz(self):
        gunler=["pazartesi","salı","çarşamba",] 
        gunlukSatıs=[1200,900,2500] 
        GunlukOrtalama=[1100,1200,1580] 
        Kar=[1500,2000,2800] 
        plt.plot(gunler,gunlukSatıs,label="Günlük Satış") 
        plt.plot(gunler,GunlukOrtalama,label="Günlük ortalama satış") 
        plt.plot(gunler,Kar,label="Kar") 
        plt.xlabel("Günler") 
        plt.ylabel("Ortalama Değerler") 
        plt.title("Günlük Eczana satış cirosu") 
        plt.legend()
        plt.show()
        h.sleep(2)
    
analiz1=Analiz("aknetrent", 2020, 1000, "2. Ayın 8. Günü Analiz Grafiği")
analiz1.analiz()
analiz1.guncelCıktılarıGoster()