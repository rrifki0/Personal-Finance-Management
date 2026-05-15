import datetime

def gelir_ekle():

    try:
        miktar = float(input("Gelir Miktarı: "))
        kategori = input("Kategori (maaş, ek iş, burs vs): ")
        aciklama = input("Açıklama: ")
        tarih = datetime.datetime.today().isoformat()

        gelir = {
            "miktar": miktar,
            "kategori": kategori,
            "aciklama": aciklama,
            "tarih": tarih
        }

        print("Gelir Eklendi.")
        return gelir
    
    except ValueError:
        print("Miktar Sayısal Olmalı!!!")
        return None
    

def gelir_listele(gelir_listesi):

    if not gelir_listesi:
        print("Henüz Gelir Girişi Olmadı.")   
        return
    
    print("\n---- Gelirler ----")
    toplam = 0

    for i, gelir in enumerate(gelir_listesi,start=1):
        print(f"{i}. {gelir['tarih']} | {gelir['kategori']} | "
              f"{gelir['miktar']} TL | {gelir['aciklama']}")
        toplam += gelir["miktar"]

    print(f"\n Toplam Gelir : {toplam} TL ")

def gelir_filtrele_kategori(gelir_listesi, kategori):

    return [g for g in gelir_listesi if g["kategori"].lower() == kategori.lower()]

def gelir_toplam(gelir_listesi):

    return sum(g["miktar"] for g in gelir_listesi)


