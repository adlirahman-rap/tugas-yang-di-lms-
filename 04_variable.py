# 04_variable.py

# Deklarasi dan inisialisasi variabel
nama_depan = "Budi"
nama_belakang = "Santoso"
usia = 25
gaji = 4500000.50

# Menggabungkan variabel (String Concatenation / f-string)
nama_lengkap = f"{nama_depan} {nama_belakang}"

print("--- Data Karyawan ---")
print("Nama Lengkap :", nama_lengkap)
print("Usia         :", usia, "tahun")
print("Gaji         : Rp", gaji)

# Aturan penulisan variabel (Assignment ulang)
usia = 26
print("Usia Tahun Depan:", usia, "tahun")
