# 08_function.py

# 1. Fungsi Sederhana tanpa Parameter
def sapa_halo():
    print("Halo, selamat datang di modul fungsi Python!")

# 2. Fungsi dengan Parameter dan Return Value
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# Pemanggilan Fungsi
sapa_halo()

p = 10
l = 5
hasil = hitung_luas_persegi_panjang(p, l)
print(f"Luas persegi panjang dengan panjang {p} dan lebar {l} adalah: {hasil}")
