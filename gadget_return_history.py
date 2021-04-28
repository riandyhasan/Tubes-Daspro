import datetime
import time

f = open("gadget_return_history.csv", "r")
raw_lines = f.readlines()
f.close()
line = [raw_line.replace('"', "") for raw_line in raw_lines]
lines = [i.replace("\n","") for i in line]

g = open("User.csv", "r")
raw_lines = g.readlines()
g.close()
line2 = [raw_line.replace('"', "") for raw_line in raw_lines]
lines2 = [i.replace("\n","") for i in line2]

h = open("gadget.csv", "r")
raw_lines = h.readlines()
h.close()
line3 = [raw_line.replace('"', "") for raw_line in raw_lines]
lines3 = [i.replace("\n","") for i in line3] 

i = open("gadget_borrow_history.csv", "r")
raw_lines = i.readlines()
i.close()
line4 = [raw_line.replace('"', "") for raw_line in raw_lines]
lines4 = [i.replace("\n","") for i in line4]

def convert_array_data_to_real_values(array_data, n):
    arr_cpy = array_data[:]
    for i in range(n):
        if(i == 0) or (i == 1) or (i == 3):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy


def convert_array_data_to_real_values2(array_data, n):
    arr_cpy = array_data[:]
    for i in range(n):
        if(i == 0):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def convert_array_data_to_real_values3(array_data, n):
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
data_gadget_return = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data, len(lines))
  data_gadget_return.append(real_values)



raw_header2 = lines2.pop(0)
header2 = convert_string_to_array(raw_header2)
data_user = []
for line in lines2:
  array_of_data2 = convert_string_to_array(line)
  real_values2 = convert_array_data_to_real_values2(array_of_data2, len(lines2))
  data_user.append(real_values2)

raw_header3 = lines3.pop(0)
header3 = convert_string_to_array(raw_header3)
data_gadget = []
for line in lines3:
  array_of_data3 = convert_string_to_array(line)
  data_gadget.append(array_of_data3)

raw_header4 = lines4.pop(0)
header4 = convert_string_to_array(raw_header4)
data_gadget_borrow = []
for line in lines4:
  array_of_data4 = convert_string_to_array(line)
  real_values4 = convert_array_data_to_real_values3(array_of_data4, len(lines4))
  data_gadget_borrow.append(real_values4)


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



for i in range(len(lines)):
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


