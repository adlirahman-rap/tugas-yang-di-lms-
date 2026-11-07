# 19_package_main.py

# Mengimpor modul dari dalam package
from my_package import aritmatika, pesan

print("--- Penggunaan Package Python ---")
hasil_tambah = aritmatika.tambah(20, 10)
hasil_kurang = aritmatika.kurang(20, 10)
salam = pesan.sapa("Rahman")

print(f"Hasil Tambah (20 + 10): {hasil_tambah}")
print(f"Hasil Kurang (20 - 10): {hasil_kurang}")
print(salam)
