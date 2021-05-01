def hapusitem(datas_gadget, datas_consum):
    id = input("Masukkan ID item: ")
    id_check = False
    if (id[0] == "G"):
        for i in range (len(datas_gadget)):
            if (datas_gadget[i][0] == id):
                id_check = False
        if (id_check):
            print("Tidak ada item dengan ID tersebut.")
        else:
            test = input("Apakah anda yakin ingin menghapus " + datas_gadget[i][1] + "(Y/N)?")

            if (test == "N"):
                print("Item gagal dihapus dari database")
            else:
                delete_gadget = [datas_gadget[i][0], datas_gadget[i][1], datas_gadget[i][2], datas_gadget[i][3], datas_gadget[i][4], datas_gadget[i][5]]
                datas_gadget.remove(delete_gadget)
    elif (id[0] == "C"):
        for i in range (len(datas_consum)):
            if (datas_consum[i][0] == id):
                id_check = False
        if (id_check):
            print("Tidak ada item dengan ID tersebut.")
        else:
            test = input("Apakah anda yakin ingin menghapus " + datas_consum[i][1] + "(Y/N)?")

            if (test == "N" or test == "n"):
                print("Item gagal dihapus dari database")
            else:
                delete_consumable = [datas_consum[i][0], datas_consum[i][1], datas_consum[i][2], datas_consum[i][3], datas_consum[i][4]]
                datas_consum.remove(delete_consumable)
                print("Item telah berhasil dihapus dari database")
    else:
        print("Gagal menambahkan item karena ID tidak valid")
    
    return datas_gadget, datas_consum
