# 02_struktur_dasar.py
# Ini adalah komentar satu baris di Python

"""
Ini adalah komentar multi-baris (docstring).
Menjelaskan struktur dasar blok program.
"""

def sapa_pengguna(nama):
    # Indentasi sangat penting dalam struktur Python
    pesan = f"Selamat datang di praktikum Python, {nama}!"
    return pesan

if __name__ == "__main__":
    output = sapa_pengguna("Santrikoding")
    print(output)
