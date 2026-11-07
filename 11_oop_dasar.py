# 11_oop_dasar.py

# Mendefinisikan Class
class Mobil:
    # Constructor (Inisialisasi atribut)
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    # Method (Fungsi di dalam class)
    def info(self):
        return f"Mobil merk {self.merk} berwarna {self.warna}"

# Membuat Objek (Instantiation)
mobil1 = Mobil("Toyota", "Hitam")
mobil2 = Mobil("Honda", "Putih")

print("--- Data Mobil (OOP Dasar) ---")
print(mobil1.info())
print(mobil2.info())
