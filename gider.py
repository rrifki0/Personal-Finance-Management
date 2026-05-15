import datetime

def gider_ekle():

    try:
        miktar = float(input("Gider Miktarı: "))
        kategori = input("Kategori (market, ulaşım, kira vs): ")
        aciklama = input("Açıklama: ")
        tarih = datetime.datetime.today().isoformat()

        gider = {
            "miktar": miktar,
            "kategori": kategori,
            "aciklama": aciklama,
            "tarih": tarih
        }

        print("Gider Eklendi.")
        return gider
    except ValueError:
        print("Miktar Sayısal Olmalı!!!")
        return None
    
def gider_listele(gider_listesi):

    if not gider_listesi:
        print("Henüz Gider Girişi Olmadı.")
        return
    
    print("\n---- Giderler ----")
    toplam = 0

    for i, gider in enumerate(gider_listesi, start=1):
        print(f"{i}. {gider['tarih']} | {gider['kategori']} |"
              f"{gider['miktar']} TL | {gider['aciklama']}")
        toplam += gider["miktar"]

    print(f"\n Toplam Gider: {toplam} TL")

def gider_filtreleme_kategori(gider_listesi, kategori):

    return [g for g in gider_listesi if g["kategori"].lower() == kategori.lower()]

def gider_toplam(gider_listesi):

    return sum(g["miktar"] for g in gider_listele)