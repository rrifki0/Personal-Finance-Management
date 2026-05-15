import tkinter as tk
from tkinter import ttk
from rapor import aylik_rapor, bu_ay_en_cok_harcama


class RaporFrame(tk.Frame):
    def __init__(self, parent, finans):
        super().__init__(parent)
        self.finans = finans

        # Frame ayarları
        self.pack(fill="both", expand=True)

        # Başlık
        baslik = ttk.Label(
            self,
            text="Raporlar",
            font=("Arial", 16)
        )
        baslik.pack(pady=10)

        # Rapor Göster Butonu
        rapor_btn = ttk.Button(
            self,
            text="Aylık Raporu Göster",
            command=self.rapor_goster
        )
        rapor_btn.pack(pady=5)

        # Rapor Yazı Alanı
        self.rapor_text = tk.Text(
            self,
            width=60,
            height=15
        )
        self.rapor_text.pack(pady=10)

    def rapor_goster(self):
        self.rapor_text.delete("1.0", tk.END)

        # Aylık rapor metni
        rapor_metni = aylik_rapor(self.finans)

        # Gider listesi (korumalı erişim)
        gider_listesi = self.finans.get("gider", [])

        en_cok = bu_ay_en_cok_harcama(gider_listesi)

        self.rapor_text.insert(tk.END, rapor_metni + "\n")

        if en_cok:
            self.rapor_text.insert(
                tk.END,
                f"\nBu ay en çok harcama:\n"
                f"{en_cok['kategori']} - {en_cok['miktar']} TL\n"
            )
        else:
            self.rapor_text.insert(
                tk.END,
                "\nBu ay için gider bulunamadı.\n"
            )


