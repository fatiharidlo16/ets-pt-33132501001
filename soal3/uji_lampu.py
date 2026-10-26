
from lampu import Lampu

lp = Lampu("L1")

print("Awal:", lp.aktif, lp.kecerahan)

lp.nyalakan()
print("Setelah nyalakan():", lp.aktif, lp.kecerahan)

nilai = float(input("Masukkan kecerahan pertama (60): "))
lp.atur(nilai)
print("Setelah atur(60):", lp.aktif, lp.kecerahan)

nilai = float(input("Masukkan kecerahan kedua (150): "))
lp.atur(nilai)
print("Setelah atur(150):", lp.aktif, lp.kecerahan)

nilai = float(input("Masukkan kecerahan ketiga (-5): "))
lp.atur(nilai)
print("Setelah atur(-5):", lp.aktif, lp.kecerahan)

lp.matikan()
print("Setelah matikan():", lp.aktif, lp.kecerahan)
