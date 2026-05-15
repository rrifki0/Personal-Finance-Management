from dosya_islemleri import dosya_oku
from gui.app import uygulamayi_baslat

def main():
    finans = dosya_oku()
    uygulamayi_baslat(finans)

if __name__ == "__main__":
    main()


