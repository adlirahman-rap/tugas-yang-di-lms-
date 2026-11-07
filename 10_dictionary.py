# 10_dictionary.py

# Mendefinisikan Dictionary
mahasiswa = {
    "nama": "Andi Pratama",
    "nim": "2023001",
    "jurusan": "Teknik Informatika",
    "aktif": True
}

print("--- Data Mahasiswa ---")
print("Nama:", mahasiswa["nama"])
print("Jurusan:", mahasiswa.get("jurusan"))

# Menambah / Mengubah Data di Dictionary
mahasiswa["ipk"] = 3.85  # Menambah key baru
mahasiswa["nama"] = "Andi Pratama, S.Kom."  # Mengubah value

print("\n--- Setelah Diperbarui ---")
print(mahasiswa)
