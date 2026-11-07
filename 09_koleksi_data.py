# 09_koleksi_data.py

# 1. List (Bisa diubah isinya)
buah = ["Apel", "Jeruk", "Mangga"]
buah.append("Pisang")  # Menambah item
print("List Buah:", buah)
print("Buah pertama:", buah[0])

# 2. Tuple (Tidak bisa diubah isinya / immutable)
koordinat = (10.5, 20.8)
print("\nTuple Koordinat:", koordinat)

# 3. Set (Tidak ada duplikat & tidak berurutan)
angka_unik = {1, 2, 2, 3, 4, 4, 5}
print("Set Angka Unik (Duplikat otomatis dihapus):", angka_unik)
