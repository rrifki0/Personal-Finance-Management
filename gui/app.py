import tkinter as tk
from gui.gelir_frame import GelirFrame
from gui.gider_frame import GiderFrame
from gui.rapor_frame import RaporFrame


def uygulamayi_baslat(finans):
    root = tk.Tk()
    root.title("Finans Takip Uygulaması")
    root.geometry("800x500")

    # ÜST MENÜ
    menu_frame = tk.Frame(root)
    menu_frame.pack(side="top", fill="x")

    # ORTA ALAN (ekranlar burada)
    content_frame = tk.Frame(root)
    content_frame.pack(expand=True, fill="both")

    # Frame'leri oluştur
    frames = {
        "gelir": GelirFrame(content_frame, finans),
        "gider": GiderFrame(content_frame, finans),
        "rapor": RaporFrame(content_frame, finans),
    }

    # Hepsini aynı yere koy
    for frame in frames.values():
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def ekran_goster(isim):
        frames[isim].tkraise()

    # Menü butonları
    tk.Button(menu_frame, text="Gelir Ekle",
              command=lambda: ekran_goster("gelir")).pack(side="left", padx=5)

    tk.Button(menu_frame, text="Gider Ekle",
              command=lambda: ekran_goster("gider")).pack(side="left", padx=5)

    tk.Button(menu_frame, text="Raporlar",
              command=lambda: ekran_goster("rapor")).pack(side="left", padx=5)

    # Açılış ekranı
    ekran_goster("gelir")

    root.mainloop()
