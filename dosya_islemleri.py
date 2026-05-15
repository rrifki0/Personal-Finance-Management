import json
import os

DOSYA_ADI = "finans_veri.json"

def dosya_oku():
    if not os.path.exists(DOSYA_ADI):
        return {
            "gelir": [],
            "gider": []
        }

    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        return json.load(dosya)


def dosya_yaz(finans):
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(finans, dosya, ensure_ascii=False, indent=4)

def dosya_kaydet(finans):
    dosya_yaz(finans)