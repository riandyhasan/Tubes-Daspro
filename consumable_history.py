import datetime
import time

def riwayatambil(data_consumable_return):
    print("\n============ RIWAYAT AMBIL =============\n")
    # print(data_consumable_return)
    data_consumable_return_copy = data_consumable_return[:]
    data_consumable_return_copy_sorted = sorted(data_consumable_return_copy, key=lambda x: datetime.datetime.strptime(x[3], "%d/%m/%Y").strftime("%Y-%m-%d"), reverse= True)
    # print(data_consumable_return_copy_sorted )
    for i in range(len(data_consumable_return_copy_sorted)):
        print("ID pengembalian: ", data_consumable_return_copy_sorted[i][0])
        print("Nama Pengambil: ", data_consumable_return_copy_sorted[i][1])
        print("Nama Consumable: ", data_consumable_return_copy_sorted[i][2])
        print("Tanggal Pengambilan: ", data_consumable_return_copy_sorted[i][3])
        print("Jumlah: ", data_consumable_return_copy_sorted[i][4])
        print("\n")
        time.sleep(2)
        if (i==4):
            user_input = input("Apakah Anda ingin mengetahui entry data lainnya?(Ketik 't' untuk 'tidak' dan ketik apapun untuk melanjutkan): ")
            if (user_input == 't'):
                break
