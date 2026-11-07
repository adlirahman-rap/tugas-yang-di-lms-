# 13_inheritance.py

# Parent Class (Kelas Induk)
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        return f"{self.nama} mengeluarkan suara."

# Child Class (Kelas Anak mewarisi Hewan)
class Kucing(Hewan):
    def bersuara(self):
        return f"{self.nama} mengeong: Meong! Meong!"

class Anjing(Hewan):
    def bersuara(self):
        return f"{self.nama} menggonggong: Guk! Guk!"

# Uji Coba Program
hewan_umum = Hewan("Binatang")
kucing_lokal = Kucing("Milo")
anjing_lokal = Anjing("Bulldog")

print("--- Pewarisan (Inheritance) ---")
print(hewan_umum.bersuara())
print(kucing_lokal.bersuara())  # Mewarisi metode dengan overriding
print(anjing_lokal.bersuara())
