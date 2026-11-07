# 16_exception_handling.py

print("--- Program Pembagian Angka ---")

try:
    # Meminta input dari pengguna
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    
    # Operasi pembagian yang berpotensi error (ZeroDivisionError)
    hasil = angka1 / angka2

except ZeroDivisionError:
    print("Error: Tidak bisa membagi angka dengan nol (0)!")
except ValueError:
    print("Error: Masukan harus berupa angka yang valid!")
else:
    print(f"Hasil pembagian: {hasil}")
finally:
    print("Blok try-except selesai dieksekusi.")
