import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from collections import defaultdict


def gider_pie_chart(parent, finans):
    kategori_toplam = defaultdict(float)

    for g in finans["gider"]:
        kategori_toplam[g["kategori"]] += g["miktar"]

    fig = Figure(figsize=(5, 4))
    ax = fig.add_subplot(111)

    ax.pie(
        kategori_toplam.values(),
        labels=kategori_toplam.keys(),
        autopct="%1.1f%%"
    )
    ax.set_title("Gider Dağılımı")

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack()


