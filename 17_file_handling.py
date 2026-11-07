# 17_file_handling.py

nama_file = "catatan.txt"

# 1. Menulis data ke dalam file (Mode 'w' / Write)
with open(nama_file, "w") as file:
    file.write("Halo, ini adalah baris pertama catatan.\n")
    file.write("Belajar Python Dasar di Santrikoding sangat menyenangkan!\n")
print(f"Berhasil menulis data ke dalam {nama_file}")

# 2. Menambah data ke dalam file tanpa menghapus data lama (Mode 'a' / Append)
with open(nama_file, "a") as file:
    file.write("Baris tambahan baru ditambahkan di akhir file.\n")
print("Berhasil menambahkan data (append).")

# 3. Membaca isi file (Mode 'r' / Read)
print("\n--- Isi Berkas Catatan ---")
with open(nama_file, "r") as file:
    isi = file.read()
    print(isi)
