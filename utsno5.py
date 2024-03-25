def formatdengankoma(number):
    # pakai koma setiap 3 digit
    return '{:,}'.format(number)

def main():
    total = 0
    with open("input.txt", "r") as file:
        for line in file:
            # Mengkonversi setiap baris menjadi integer dan menambahkannya ke total
            total += int(line.strip())
    
    # cetak koma sebagai pemisah 
    print("Total:", formatdengankoma(total))

main()
