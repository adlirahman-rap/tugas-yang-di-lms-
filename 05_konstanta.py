# 05_konstanta.py

# Konvensi penulisan konstanta (menggunakan huruf kapital semua)
PI = 3.14159
MAX_USER = 100
DATABASE_URL = "localhost:3306/db_python"

print("--- Konfigurasi Sistem ---")
print("Nilai PI          :", PI)
print("Maksimal User     :", MAX_USER)
print("URL Database      :", DATABASE_URL)

# Contoh penggunaan dalam perhitungan (misal: luas lingkaran)
jari_jari = 7
luas_lingkaran = PI * (jari_jari ** 2)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas_lingkaran}")
