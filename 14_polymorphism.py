# 14_polymorphism.py

class Kucing:
    def bersuara(self):
        return "Meong!"

class Anjing:
    def bersuara(self):
        return "Guk Guk!"

class Bebek:
    def bersuara(self):
        return "Kwek Kwek!"

# Fungsi yang menerima objek apa saja yang memiliki method 'bersuara'
def cetak_suara_hewan(objek_hewan):
    print(objek_hewan.bersuara())

# Uji Coba Program
kucing = Kucing()
anjing = Anjing()
bebek = Bebek()

print("--- Polimorfisme (Polymorphism) ---")
cetak_suara_hewan(kucing)
cetak_suara_hewan(anjing)
cetak_suara_hewan(bebek)
