def ubahjumlah(datas_gadget, datas_consum):
    print("\n============ UBAH JUMLAH =============\n")
    id = input("Masukkan ID: ")
    id_check = False
    if (id[0] == "G"):
        for i in range (len(datas_gadget)):
            if (datas_gadget[i][0] == id):
                id_check = False
        if (id_check):
            print("Tidak ada item dengan ID tersebut.")
            user_input = input("Ingin mengulang proses lagi? (Ketik 't' untuk 'tidak' dan apapun untuk melanjutkan): ")
            if user_input != "t":
                ubahjumlah(datas_gadget, datas_consum)
        else:
            change_gadget = int(input("Masukkan Jumlah: "))

            if (change_gadget > 0 ):
                jumlah_gadget = change_gadget + datas_gadget[i][3]
                datas_gadget[i][3] = jumlah_gadget
                print(str(change_gadget) + " " + datas_gadget[i][1] + " berhasil ditambahkan. Stok sekarang: " + str(jumlah_gadget))
            else:
                jumlah_gadget = datas_gadget[i][3] - change_gadget
                datas_gadget[i][3] = jumlah_gadget
                print(str(change_gadget) + " " + datas_gadget[i][1] + " berhasil dibuang. Stok sekarang: " + str(jumlah_gadget))
    elif (id[0] == "C"):
        for i in range (len(datas_consum)):
            if (datas_consum[i][0] == id):
                id_check = False
        if (id_check):
            print("Tidak ada item dengan ID tersebut.")
            user_input = input("Ingin mengulang proses lagi? (Ketik 't' untuk 'tidak' dan apapun untuk melanjutkan): ")
            if user_input != "t":
                ubahjumlah(datas_gadget, datas_consum)
        else:
            change_consumable = int(input("Masukkan Jumlah: "))

            if (change_consumable > 0 ):
                jumlah_consumable = change_consumable + datas_consum[i][3]
                datas_consum[i][3] = jumlah_consumable
                print(str(change_consumable) + " " + datas_consum[i][1] + " berhasil ditambahkan. Stok sekarang: " + str(jumlah_consumable))
            else:
                jumlah_consumable = datas_consum[i][3] - change_consumable
                datas_consum[i][3] = jumlah_consumable
                print(str(change_consumable) + " " + datas_consum[i][1] + " berhasil dibuang. Stok sekarang: " + str(jumlah_consumable))
    else:
        print("Gagal menambahkan item karena ID tidak valid")
        user_input = input("Ingin mengulang proses lagi? (Ketik 't' untuk 'tidak' dan apapun untuk melanjutkan): ")
        if user_input != "t":
            ubahjumlah(datas_gadget, datas_consum)
    
    return datas_gadget, datas_consum


