from csv import data_gadget, data_consumable

data_consum = data_consumable

def tambahitem():
    id = input("Masukkan ID: ")
    id_check = False
    if (id[0] == "G"):
        for i in range (len(data_gadget)):
            if (data_gadget[i][0] == id):
                id_check = True
        if (id_check):
            print("Gagal menambahkan item karena ID sudah ada.")
        else:
            name = input("Masukkan Nama: ")
            desc = input("Masukkan Deskripsi: ")
            amount = int(input("Masukkan Jumlah: "))
            rarity = input("Masukkan Rarity: ")
            year = int(input("Masukkan tahun ditemukan: "))

            if rarity != "C" and rarity != "B" and rarity != "A" and rarity != "S":
                print("Input rarity tidak valid!")
            else:
                add_gadget = [id, name, desc, amount, rarity, year]
                data_gadget.append(add_gadget)
    elif (id[0] == "C"):
        for i in range (len(data_consum)):
            if (data_consum[i][0] == id):
                id_check = True
        if (id_check):
            print("Gagal menambahkan item karena ID sudah ada.")
        else:
            name = input("Masukkan Nama: ")
            desc = input("Masukkan Deskripsi: ")
            amount = int(input("Masukkan Jumlah: "))
            rarity = input("Masukkan Rarity: ")

            if rarity != "C" and rarity != "B" and rarity != "A" and rarity != "S":
                print("Input rarity tidak valid!")
            else:
                add_consum = [id, name, desc, amount, rarity]
                data_consum.append(add_consum)
    else:
        print("Gagal menambahkan item karena ID tidak valid")
    
    return data_gadget, data_consum

