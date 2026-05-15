import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dosya_islemleri import dosya_kaydet


class GelirFrame(tk.Frame):
    def __init__(self, parent, finans):
        super().__init__(parent)
        self.finans = finans

        baslik = tk.Label(self, text="Gelir Ekle", font=("Arial", 16, "bold"))
        baslik.pack(pady=10)

        form = tk.Frame(self)
        form.pack(pady=20)

        tk.Label(form, text="Kategori:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.kategori_entry = tk.Entry(form)
        self.kategori_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Miktar:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.miktar_entry = tk.Entry(form)
        self.miktar_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self, text="Gelir Ekle", command=self.gelir_ekle).pack(pady=10)

    def gelir_ekle(self):
        kategori = self.kategori_entry.get().strip()
        miktar = self.miktar_entry.get().strip()

        if not kategori or not miktar:
            messagebox.showwarning("Uyarı", "Tüm alanları doldurun.")
            return

        try:
            miktar = float(miktar)
        except ValueError:
            messagebox.showerror("Hata", "Miktar sayı olmalıdır.")
            return

        gelir = {
            "kategori": kategori,
            "miktar": miktar,
            "tarih": datetime.now().isoformat()
        }

        self.finans["gelir"].append(gelir)
        dosya_kaydet(self.finans)

        messagebox.showinfo("Başarılı", "Gelir eklendi.")

        self.kategori_entry.delete(0, tk.END)
        self.miktar_entry.delete(0, tk.END)
