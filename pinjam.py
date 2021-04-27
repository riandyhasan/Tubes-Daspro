f = open("gadget.csv","r")
raw_lines = f.readlines()
f.close()
line = [raw_line.replace('"', '') for raw_line in raw_lines]
lines = [i.replace("\n","") for i in line]

g = open("gadget_borrow_history.csv","r")
raw_lines2 = g.readlines()
f.close()
line2 = [raw_line2.replace('"', "") for raw_line2 in raw_lines2]
lines2 = [i.replace("\n","") for i in line2]

def convert_array_data_to_real_values(array_data, n):
  arr_cpy = array_data[:]
  for i in range(n):
    if(i == 3) or (i == 5):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy

def convert_array_data_to_real_values_history(array_data, n):
  arr_cpy = array_data[:]
  for i in range(n):
    if(i == 0) or (i == 1) or (i == 4):
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
datas_gadget = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data, 6)
  datas_gadget.append(real_values)

raw_header2 = lines2.pop(0)
header2 = convert_string_to_array(raw_header2)
history_data_gadget = []
for line in lines2:
  array_of_data2 = convert_string_to_array(line)
  real_values2 = convert_array_data_to_real_values_history(array_of_data2, 5)
  history_data_gadget.append(real_values2)

id_history = history_data_gadget[-1][0]
add_id_history = id_history + 1

def pinjam():
    id = input("Masukkan ID item: ")
    cek_id = False
    if (id[0] == "G"):
        for i in range (len(datas_gadget)):
            if (datas_gadget[i][0] == id):
                cek_id = False
        if (cek_id):
            print("Tidak ada item dengan ID tersebut.")
        else:
            tanggal_peminjaman = input("Tanggal peminjaman: ")
            jumlah_peminjaman = int(input("Masukkan Jumlah: "))
            jumlah_akhir_gadget = datas_gadget[i][3] - jumlah_peminjaman
            datas_gadget[i][3] = jumlah_akhir_gadget
            new_history = [add_id_history, username_login, id, tanggal_peminjaman, jumlah_peminjaman]
            history_data_gadget.append(new_history)
            print("Item" + datas_gadget[i][1] + "(x" + jumlah_peminjaman + ") berhasil dipinjam!")
    else:
        print("Gagal menambahkan item karena ID tidak valid")
