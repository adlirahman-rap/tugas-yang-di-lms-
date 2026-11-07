# 12_encapsulation.py

class RekeningBank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik        # Public attribute
        self.__saldo = saldo_awal     # Private attribute (menggunakan __)

    # Getter untuk melihat nilai saldo private
    def get_saldo(self):
        return self.__saldo

    # Setter untuk mengubah/menyetor saldo dengan validasi
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil setor Rp{jumlah:,}. Saldo sekarang: Rp{self.__saldo:,}")
        else:
            print("Jumlah setoran harus lebih dari 0!")

# Uji Coba Program
rekening = RekeningBank("Budi Santoso", 500000)

print("--- Informasi Rekening ---")
print("Pemilik:", rekening.pemilik)
print("Saldo Awal:", rekening.get_saldo())

# Melakukan transaksi melalui method setor (Setter)
rekening.setor(250000)

# Jika mencoba mengakses __saldo secara langsung dari luar class, akan terjadi error (AttributeError):
# print(rekening.__saldo)
