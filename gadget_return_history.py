import datetime
import time

def riwayatkembali(data_gadget_return, data_user, data_gadget, data_gadget_borrow):
    data_gadget_return_copy = data_gadget_return[:]
    data_gadget_return_copy_sorted = sorted(data_gadget_return_copy, key=lambda x: datetime.datetime.strptime(x[2], "%d/%m/%Y").strftime("%Y-%m-%d"), reverse= True)
    nama = [i[2] for i in data_user]
    id = [i[0] for i in data_gadget_return_copy_sorted]
    id_peminjaman = [i[1] for i in data_gadget_return_copy_sorted]
    id_borrow = [i[0] for i in data_gadget_borrow]
    id_gadget = [i[0] for i in data_gadget]
    id_gadget_borrow = [i[2] for i in data_gadget_borrow]
    id_user_borrow = [i[1] for i in data_gadget_borrow]
    id_user = [i[0] for i in data_user]
    for i in range(len(data_gadget_borrow)):
        print("ID pengambilan: ", id[i])
        index_id_peminjam_borrow = id_borrow.index(id_peminjaman[i])
        id_peminjam_borrow = id_user_borrow[index_id_peminjam_borrow]
        cek_id_nama = id_user.index(id_peminjam_borrow)
        ambil_nama = nama[cek_id_nama]
        print("Nama Pengambil:",ambil_nama)
        ambil_id_gadget_borrow = data_gadget_borrow[index_id_peminjam_borrow][2]
        index_id_gadget = id_gadget.index(ambil_id_gadget_borrow)
        print("Nama Gadget: ", data_gadget[index_id_gadget][1])
        print("Tanggal Pengembalian: ", data_gadget_return_copy_sorted[i][2])
        print("\n")
        time.sleep(2)
        if (i==4):
            user_input = input("Apakah Anda ingin mengetahui entry data lainnya?(Ketik 't' untuk 'tidak' dan ketik apapun untuk melanjutkan): ")
            if (user_input == 't'):
                break


