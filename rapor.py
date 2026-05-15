import datetime


def tarih_parse(tarih_str):
    try:
        return datetime.datetime.fromisoformat(tarih_str).date()
    except ValueError:
        return datetime.datetime.strptime(
            tarih_str.split(".")[0],
            "%Y-%m-%d %H:%M:%S"
        ).date()


def aylik_rapor(finans):
    bugun = datetime.date.today()
    ay = bugun.month
    yil = bugun.year

    toplam_gelir = 0
    toplam_gider = 0

    for g in finans["gelir"]:
        tarih = tarih_parse(g["tarih"])
        if tarih.month == ay and tarih.year == yil:
            toplam_gelir += g["miktar"]

    for g in finans["gider"]:
        tarih = tarih_parse(g["tarih"])
        if tarih.month == ay and tarih.year == yil:
            toplam_gider += g["miktar"]

    bakiye = toplam_gelir - toplam_gider

    rapor = (
        f"Ay/Yıl: {ay}/{yil}\n"
        f"Toplam Gelir: {toplam_gelir} TL\n"
        f"Toplam Gider: {toplam_gider} TL\n"
        f"Bakiye: {bakiye} TL\n"
    )

    return rapor


def bu_ay_en_cok_harcama(gider_listesi):
    if not gider_listesi:
        return None

    en_cok = max(gider_listesi, key=lambda x: x["miktar"])
    return en_cok

