
header = ["id", "id_peminjaman", "tanggal_pengembalian" , "jumlah_pengembalian"]

header2 = ["id", "username", "nama", "alamat", "password", "role"]

header3 = ["id", "nama", "deskripsi", "jumlah", "rarity", "tahun_ditemukan"]

header4 = ["id", "id_peminjam", "id_gadget", "tanggal_peminjaman", "jumlah", "is_returned"]

header5 = ["id", "nama", "deskripsi", "jumlah;rarity"]

header6 = ["ID Pengambilan", "Nama Pengambil", "Nama Consumable", "Tanggal Pengembilan", "Jumlah"]



def convert_datas_to_string(header, data):
  string_data = ";".join(header) + "\n"
  for arr_data in data:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data