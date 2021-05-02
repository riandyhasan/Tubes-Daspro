import datetime
import time

def riwayatpinjam(data_user, data_gadget_borrow, data_gadget):
    print("\n============ RIWAYAT PINJAM =============\n")  
    data_gadget_borrow_copy = data_gadget_borrow[:]
    data_gadget_borrow_copy_sorted = sorted(data_gadget_borrow_copy, key=lambda x: datetime.datetime.strptime(x[3], "%d/%m/%Y").strftime("%Y-%m-%d"), reverse= True)
    nama = [i[2] for i in data_user]
    id_peminjam = [i[1] for i in data_gadget_borrow_copy_sorted]
    id_gadget_pinjam = [i[2] for i in data_gadget_borrow_copy_sorted]
    id_gadget = [i[0] for i in data_gadget]
    id = [i[0] for i in data_user]
    for i in range(len(data_gadget_borrow)):
        print("ID Peminjaman: ",data_gadget_borrow_copy_sorted[i][0])
        id_cek_nama = id.index(id_peminjam[i])
        print("Nama Pengambil: ", data_user[id_cek_nama][2])
        id_cek_gadget = id_gadget.index(id_gadget_pinjam[i])
        print("Nama Gadget: ", data_gadget[id_cek_gadget][1])
        print("Tanggal Peminjaman: ", data_gadget_borrow_copy_sorted[i][3])
        print("Jumlah: ",data_gadget_borrow_copy_sorted[i][-2])
        print("\n")
        time.sleep(2)
        if (i==4):
            user_input = input("Apakah Anda ingin mengetahui entry data lainnya?(Ketik 't' untuk 'tidak' dan ketik apapun untuk melanjutkan): ")
            if (user_input == 't'):
                break
