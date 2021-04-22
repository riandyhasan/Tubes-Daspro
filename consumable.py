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

def validasi(id, jumlah, list):
    kode = [i[0] for i in list[:]]
    total_awal = [i[3] for i in list[:]]
    nama = [i[1] for i in list[:]]

    if (id in kode):
        posisi = kode.index(id)
        total_akhir = int(total_awal[posisi]) - jumlah
        if total_akhir < 0:
            return "Melebihi jumlah barang yang tersedia"
        else:
            list[posisi][3] = total_akhir
            return ("Item {} (x{}) telah berhasil diambil!".format(nama[posisi], jumlah))
    else:
        return "ID tidak valid"
    

raw_header = lines.pop(0)
header = convert_string_to_array(raw_header)
data = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data,5)
  data.append(real_values)


id = input("Masukkan ID item: ")
jumlah = int(input("Jumlah: "))
tanggal = input("Tanggal permintaan: ")
print(validasi(id,jumlah, data))

print(data)