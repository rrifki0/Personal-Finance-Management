import tkinter as tk
from tkinter import ttk
from rapor import (
    aylik_rapor,
    bu_ay_en_cok_harcama
)
from gui.grafik_ekran import gider_pie_chart


def rapor_ekrani(parent, finans):
    pencere = tk.Toplevel(parent)
    pencere.title("Raporlar")
    pencere.geometry("600x500")

    baslik = tk.Label(pencere, text="Finans Raporları", font=("Arial", 16, "bold"))
    baslik.pack(pady=10)

    cikti_alani = tk.Text(pencere, height=12, width=70)
    cikti_alani.pack(pady=10)

    def raporu_goster():
        cikti_alani.delete("1.0", tk.END)
        sonuc = aylik_rapor(finans)
        cikti_alani.insert(tk.END, sonuc)

    def en_cok_harcama_goster():
        cikti_alani.delete("1.0", tk.END)
        sonuc = bu_ay_en_cok_harcama(finans["gider"])
        cikti_alani.insert(tk.END, sonuc)

    def grafik_goster():
        grafik_pencere = tk.Toplevel(pencere)
        grafik_pencere.title("Gider Dağılımı Grafiği")
        gider_pie_chart(grafik_pencere, finans)

    buton_frame = tk.Frame(pencere)
    buton_frame.pack(pady=10)

    ttk.Button(buton_frame, text="Aylık Rapor", command=raporu_goster).grid(row=0, column=0, padx=5)
    ttk.Button(buton_frame, text="Bu Ay En Çok Harcama", command=en_cok_harcama_goster).grid(row=0, column=1, padx=5)
    ttk.Button(buton_frame, text="Gider Dağılımı (Pie Chart)", command=grafik_goster).grid(row=0, column=2, padx=5)

    ttk.Button(pencere, text="Kapat", command=pencere.destroy).pack(pady=10)
