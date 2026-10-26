
from perangkat import SensorSuhu, SensorDebit

# Membuat objek sensor
suhu = SensorSuhu("Suhu")
debit = SensorDebit("Debit", "L/menit")

# Memasukkan data pembacaan suhu
suhu.baca(30.1)
suhu.baca(30.6)
suhu.baca(30.3)

# Memasukkan data pembacaan debit
debit.baca(12.0)
debit.baca(15.0)
debit.baca(15.0)

# Menggabungkan kedua perangkat dalam satu list
perangkat_list = [suhu, debit]

# Memproses setiap perangkat
for p in perangkat_list:
    print(f"{p.nama} -> {p.proses()}")
