def main():
    year = 366
    try:
        bilangan_bulat = int(input("Input bilangan bulat: "))
        hasil_pembagian = bilangan_bulat / year
        print("Hasil pembagian:", round(hasil_pembagian, 11))
    except ValueError:
        print("Input sebuah bilangna bulat")

main()
