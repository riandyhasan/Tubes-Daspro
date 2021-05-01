from csv import data_gadget, data_gadget_borrow, header3, header4, header5, convert_datas_to_string

datas_gadget = data_gadget
history_data_gadget = data_gadget_borrow

id_history = history_data_gadget[-1][0]
add_id_history = id_history + 1

def pinjam(id_user):
    id = input("Masukkan ID item: ")
    cek_id = False
    is_returned = "Tidak"
    if (id[0] == "G"):
        for i in range (len(datas_gadget)):
            if (datas_gadget[i][0] == id):
                cek_id = False
        if (cek_id):
            print("Tidak ada item dengan ID tersebut.")
        else:
            username_id = id_user
            tanggal_peminjaman = input("Tanggal peminjaman: ")
            jumlah_peminjaman = int(input("Masukkan Jumlah: "))
            jumlah_akhir_gadget = datas_gadget[i][3] - jumlah_peminjaman
            datas_gadget[i][3] = jumlah_akhir_gadget
            new_history = [add_id_history, username_id, id, tanggal_peminjaman, jumlah_peminjaman, is_returned]
            history_data_gadget.append(new_history)
            print("Item" + datas_gadget[i][1] + "(x" + str(jumlah_peminjaman) + ") berhasil dipinjam!")
    else:
        print("Gagal menambahkan item karena ID tidak valid")
    
    return datas_gadget, history_data_gadget



