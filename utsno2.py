def hitung_produk(angka):
    produk = 1
    for i in range(1, angka + 1):
        produk *= i
    return produk

def main():
    tanggal = 25  # Tanggal hari ini
    hasil_produk = hitung_produk(tanggal)
    print("Seluruh produk dari semua nilai dari 1 hingga tanggal 25 adalah:", hasil_produk)

main()