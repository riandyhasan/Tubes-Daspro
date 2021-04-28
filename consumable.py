import datetime

f = open("consumable.csv", "r")
raw_lines = f.readlines()
f.close()
line = [raw_line.replace('"', "") for raw_line in raw_lines]
lines = [i.replace("\n","") for i in line]

def convert_array_data_to_real_values(array_data, n):
    arr_cpy = array_data[:]
    for i in range(n):
        if(i == 3):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy
def convert_string_to_array(line):
    word = ""
    delete = ";"
    line += delete
    l = len(line)
    new_list = []
    for i in range(l):
        if (line[i] != delete):
            word += line[i]
        else:
            if (len(word) != 0):
                new_list.append(word)
            word = ""
    return new_list


raw_header = lines.pop(0)
header = convert_string_to_array(raw_header)
data = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data,5)
  data.append(real_values)

def printing():
    id = input("Masukkan ID item: ")
    
    kode = [i[0] for i in data[:]]
    total_awal = [i[3] for i in data[:]]
    nama = [i[1] for i in data[:]]

    if (id not in kode):
        print("ID tidak valid")
        coba_ulang = input("Ingin mencoba lagi? Ketik (y) jika ingin mencoba ulang: ")
        if coba_ulang == "y" or "Y":
            return printing()
    else:     
        jumlah = int(input("Jumlah: "))
        posisi = kode.index(id)
        total_akhir = total_awal[posisi] - jumlah
        if total_akhir < 0:
            print("\nMelebihi jumlah barang yang tersedia")
            print("Jumlah {} yang tersedia adalah {} ".format(nama[posisi], total_awal[posisi]))
            print("Pastikan jumlah barang yang dimasukkan sesuai dengan jumlah barang yang tersedia\n")
            coba_ulang = input("Ingin mencoba lagi? Ketik (y) jika ingin mencoba ulang:")
            if coba_ulang == "y" or "Y":
                return printing()
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
            print("Item {} (x{}) telah berhasil diambil!".format(nama[posisi], jumlah))

printing()
