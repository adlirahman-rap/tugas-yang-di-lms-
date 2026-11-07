# 18_module_main.py

# Mengimpor modul yang sudah dibuat
import matematika

print("--- Penggunaan Modul Kustom ---")
hasil_tambah = matematika.tambah(15, 5)
hasil_kali = matematika.kali(4, 5)

print(f"Hasil Tambah (15 + 5) : {hasil_tambah}")
print(f"Hasil Kali (4 * 5)    : {hasil_kali}")
print(f"Nilai konstanta PI    : {matematika.PI}")
