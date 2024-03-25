import datetime

def tanggalitu(bilangan_bulat):
    # Mendapatkan tanggal dari bilangan bulat
    tanggal = datetime.date.today() + datetime.timedelta(days=bilangan_bulat)

    # Mendapatkan nama hari dan bulan
    nama_hari = tanggal.strftime("%A")
    nama_bulan = tanggal.strftime("%B")

    return nama_hari, tanggal.day, nama_bulan, tanggal.year

def main():
    try:
        bilangan_bulat = int(input("Masukkan bilangan bulat: "))
        nama_hari, day, nama_bulan, year = tanggalitu(bilangan_bulat)
        print(f"{nama_hari} on {day} {nama_bulan} {year}")
    except ValueError:
        print("Masukkan bilangan bulat")

main()
