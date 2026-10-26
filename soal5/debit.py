
import csv


def galat_absolut(hasil, acuan):
    return abs(hasil - acuan)


def galat_relatif(hasil, acuan):
    if acuan == 0:
        raise ValueError("Nilai acuan tidak boleh nol")

    return galat_absolut(hasil, acuan) / abs(acuan) * 100


def baca_log(nama_file):
    data_valid = []
    data_ditolak = []

    with open(nama_file, mode="r", newline="", encoding="utf-8-sig") as file:
        pembaca = csv.reader(file)
        next(pembaca, None)

        for nomor_baris, baris in enumerate(pembaca, start=2):
            isi_baris = ",".join(baris)

            if len(baris) != 2:
                data_ditolak.append({
                    "baris": nomor_baris,
                    "isi": isi_baris,
                    "alasan": "Jumlah kolom tidak sesuai"
                })
                continue

            nilai_debit = baris[1].strip()

            if nilai_debit == "":
                data_ditolak.append({
                    "baris": nomor_baris,
                    "isi": isi_baris,
                    "alasan": "Nilai debit kosong"
                })
                continue

            try:
                debit = float(nilai_debit)
            except ValueError:
                data_ditolak.append({
                    "baris": nomor_baris,
                    "isi": isi_baris,
                    "alasan": "Nilai debit bukan angka yang valid"
                })
                continue

            if not 5 <= debit <= 25:
                data_ditolak.append({
                    "baris": nomor_baris,
                    "isi": isi_baris,
                    "alasan": "Debit di luar rentang 5-25 L/menit"
                })
                continue

            data_valid.append(debit)

    return data_valid, data_ditolak


if __name__ == "__main__":
    data_valid, data_ditolak = baca_log("log_debit.csv")

    print("Jumlah data valid:", len(data_valid))
    print("Jumlah data ditolak:", len(data_ditolak))

    for data in data_ditolak:
        print(
            f"Baris {data['baris']}: "
            f"{data['isi']} -> {data['alasan']}"
        )

    if data_valid:
        rata_rata = sum(data_valid) / len(data_valid)
        print(f"Rata-rata debit: {rata_rata:.2f} L/menit")

        acuan = 13.5714
        galat_a = galat_absolut(rata_rata, acuan)
        galat_r = galat_relatif(rata_rata, acuan)

        print(f"Galat absolut: {galat_a:.4f}")
        print(f"Galat relatif: {galat_r:.4f}%")

        toleransi = 0.5
        if galat_r <= toleransi:
            print("Status: LULUS")
        else:
            print("Status: TIDAK LULUS")
    else:
        print("Rata-rata debit: tidak dapat dihitung")
