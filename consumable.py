import datetime

def check_jumlah(jumlah):
    check = False
    if jumlah >= 0:
        check = True
    return check

def minta(id_user, data, data_consumable_history, data_user):
    print("\n============ MINTA =============\n")
    id = input("Masukkan ID item: ")
    
    kode = [i[0] for i in data[:]]
    total_awal = [i[3] for i in data[:]]
    nama = [i[1] for i in data[:]]

    if (id not in kode):
        print("ID tidak valid")
        coba_ulang = input("Ingin mencoba lagi? Ketik (y) jika ingin mencoba ulang: ")
        if (coba_ulang == "y") or (coba_ulang == "Y"):
            return minta(id_user, data, data_consumable_history, data_user)
 
    else:     
        jumlah = int(input("Jumlah: "))
        if check_jumlah(jumlah):
            posisi = kode.index(id)
            total_akhir = total_awal[posisi] - jumlah
            if total_akhir < 0:
                print("\nMelebihi jumlah barang yang tersedia")
                print("Jumlah {} yang tersedia adalah {} ".format(nama[posisi], total_awal[posisi]))
                print("Pastikan jumlah barang yang dimasukkan sesuai dengan jumlah barang yang tersedia\n")
                coba_ulang = input("Ingin mencoba lagi? Ketik (y) jika ingin mencoba ulang: ")
                if (coba_ulang == "y") or (coba_ulang == "Y"):
                    return minta(id_user, data, data_consumable_history, data_user)
    
            else:
                Kondisi = False
                while (Kondisi == False):
                    tanggal = input("Tanggal permintaan (dd/mm/YYYY): ")
                    try:
                        if tanggal == datetime.datetime.strptime(tanggal, "%d/%m/%Y").strftime('%Y-%m-%d'):
                            raise ValueError
                        Kondisi = True
                    except ValueError:
                        print("Format tanggal tidak sesuai, silakan ketik lagi dengan format yang sesuai (format:dd/mm/YYYY)")
                        Kondisi = False
                data[posisi][3] = total_akhir
                id_minta = len(data_consumable_history)
                for i in range (len(data_user)):
                    if id_user == data_user[i][0]:
                        nama_peminjam = data_user[i][2]
                for i in range (len(data)):
                    if id == data[i][0]:
                        nama_item = data[i][1]
                temp = [(id_minta+1), nama_peminjam, nama_item, tanggal, jumlah]
                data_consumable_history.append(temp)
                print("Item {} (x{}) telah berhasil diambil!".format(nama[posisi], jumlah))
        else:
            print("Jumlah tidak boleh negatif!")
            coba_ulang = input("Ingin mencoba lagi? Ketik (y) jika ingin mencoba ulang: ")
            if (coba_ulang == "y") or (coba_ulang == "Y"):
                return minta(id_user, data, data_consumable_history, data_user)
        
    return data, data_consumable_history
