# 15_abstraction.py
from abc import ABC, abstractmethod

# Abstract Class
class Kendaraan(ABC):
    
    @abstractmethod
    def nyalakan_mesin(self):
        pass

# Concrete Class (Wajib mengimplementasikan method abstrak)
class Mobil(Kendaraan):
    def nyalakan_mesin(self):
        return "Mesin mobil dinyalakan dengan kunci kontak / tombol Start."

class Motor(Kendaraan):
    def nyalakan_mesin(self):
        return "Mesin motor dinyalakan dengan electric starter / kick starter."

# Uji Coba Program
# kendaraan_umum = Kendaraan() # Error jika langsung diinstansiasi karena abstrak

mobil_ku = Mobil()
motor_ku = Motor()

print("--- Abstraksi (Abstraction) ---")
print("Mobil:", mobil_ku.nyalakan_mesin())
print("Motor:", motor_ku.nyalakan_mesin())
