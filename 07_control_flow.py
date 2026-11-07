# 07_control_flow.py

# 1. Percabangan (If, Elif, Else)
nilai = 85

print(f"Nilai ujian Anda: {nilai}")
if nilai >= 90:
    print("Grade: A (Sangat Memuaskan)")
elif nilai >= 75:
    print("Grade: B (Memuaskan)")
elif nilai >= 60:
    print("Grade: C (Cukup)")
else:
    print("Grade: D (Kurang)")

# 2. Perulangan For (Looping)
print("\n--- Perulangan For (1 sampai 5) ---")
for i in range(1, 6):
    print(f"Perulangan ke-{i}")

# 3. Perulangan While
print("\n--- Perulangan While ---")
counter = 3
while counter > 0:
    print(f"Hitung mundur: {counter}")
    counter -= 1
print("Waktu habis!")
