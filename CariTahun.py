def year_check(sign,year, gadget_year):
    check = False
    if (sign == "="):
        if (year == gadget_year):
            check = True
    elif (sign == ">"):
        if (year < gadget_year):
            check = True
    elif (sign == "<"):
        if (year > gadget_year):
            check = True
    elif (sign == ">="):
        if (year <= gadget_year):
            check = True
    elif (sign == "<="):
        if (year >= gadget_year):
            check = True

    return check

def yearfind(data_gadget):
    year = int(input("\nMasukkan tahun: "))
    category = input("Masukkan kategori: ")

    print("\nHasil pencarian:")
    count = 0
    for i in range (len(data_gadget)):
        if year_check(category,year, data_gadget[i][5]):
            print("\nNama             : {}".format(data_gadget[i][1]))
            print("Deskripsi        : {}".format(data_gadget[i][2]))
            print("Jumlah           : {}".format(data_gadget[i][3]))
            print("Rarity           : {}".format(data_gadget[i][4]))
            print("Tahun Ditemukan  : {}".format(data_gadget[i][5]))
            count += 1

    if count == 0:
        print("Tidak ada gadget yang ditemukan")


def caritahun(data_gadget):
    print("\n============ CARI TAHUN ==============\n")

    yearfind(data_gadget)

    user_input = input("\nApakah Anda ingin mengetahui entry data lainnya?(Ketik 't' untuk 'tidak' dan ketik apapun untuk melanjutkan): ")
    while user_input != "t":
        yearfind(data_gadget)
        user_input = input("\nApakah Anda ingin mengetahui entry data lainnya?(Ketik 't' untuk 'tidak' dan ketik apapun untuk melanjutkan): ")