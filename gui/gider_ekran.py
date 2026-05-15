import tkinter as tk
from tkinter import messagebox
import datetime

from dosya_islemleri import dosya_yaz


def gider_ekrani(parent, finans):
    pencere = tk.Toplevel(parent)
    pencere.title("Gider Ekle")
    pencere.geometry("350x350")
    pencere.grab_set()

    tk.Label(pencere, text="Gider Ekle", font=("Arial", 14)).pack(pady=10)

    tk.Label(pencere, text="Gider Adı").pack()
    ad_entry = tk.Entry(pencere, width=30)
    ad_entry.pack(pady=5)

    tk.Label(pencere, text="Tutar (TL)").pack()
    tutar_entry = tk.Entry(pencere, width=30)
    tutar_entry.pack(pady=5)

    tk.Label(pencere, text="Kategori").pack()
    kategori_entry = tk.Entry(pencere, width=30)
    kategori_entry.pack(pady=5)

    def kaydet():
        ad = ad_entry.get().strip()
        kategori = kategori_entry.get().strip()

        try:
            tutar = float(tutar_entry.get())
        except ValueError:
            messagebox.showerror("Hata", "Tutar sayısal olmalı")
            return

        if not ad or not kategori:
            messagebox.showerror("Hata", "Tüm alanları doldur")
            return

        gider = {
            "ad": ad,
            "miktar": tutar,
            "kategori": kategori,
            "tarih": datetime.datetime.now().isoformat()
        }

        finans["gider"].append(gider)
        dosya_yaz(finans)

        messagebox.showinfo("Başarılı", "Gider kaydedildi 💸")
        pencere.destroy()

    tk.Button(pencere, text="Kaydet", width=20, command=kaydet).pack(pady=20)
