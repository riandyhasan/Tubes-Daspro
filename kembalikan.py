f = open("gadget_borrow_history.csv","r")
raw_lines = f.readlines()
f.close()
line = [raw_line.replace('"', '') for raw_line in raw_lines]
lines = [i.replace("\n","") for i in line]

g = open("gadget_return_history.csv","r")
raw_lines2 = g.readlines()
f.close()
line2 = [raw_line2.replace('"', "") for raw_line2 in raw_lines2]
lines2 = [i.replace("\n","") for i in line2]

h = open("gadget.csv","r")
raw_lines3 = h.readlines()
h.close()
line3 = [raw_line3.replace('"', '') for raw_line3 in raw_lines3]
lines3 = [i.replace("\n","") for i in line3]

def convert_array_data_to_real_values_history(array_data, n):
  arr_cpy = array_data[:]
  for i in range(n):
    if(i == 0) or (i == 1) or (i == 4):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy

def convert_array_data_to_real_values_return(array_data, n):
  arr_cpy = array_data[:]
  for i in range(n):
    if(i == 0) or (i == 1) or (i == 3):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy

def convert_array_data_to_real_values(array_data, n):
  arr_cpy = array_data[:]
  for i in range(n):
    if(i == 3) or (i == 5):
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
borrow_datas_gadget = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values_history(array_of_data, 6)
  borrow_datas_gadget.append(real_values)

raw_header2 = lines2.pop(0)
header2 = convert_string_to_array(raw_header2)
return_data_gadget = []
for line in lines2:
  array_of_data2 = convert_string_to_array(line)
  real_values2 = convert_array_data_to_real_values_return(array_of_data2, 5)
  return_data_gadget.append(real_values2)

raw_header3 = lines3.pop(0)
header3 = convert_string_to_array(raw_header3)
datas_gadget = []
for line in lines3:
  array_of_data3 = convert_string_to_array(line)
  real_values3 = convert_array_data_to_real_values(array_of_data3, 6)
  datas_gadget.append(real_values3)

id_return = return_data_gadget[-1][0]
add_id_return = id_return + 1

for i in range(len(borrow_datas_gadget)):
  print((i+1), borrow_datas_gadget[i][2])

def kembalikan():
  nomor_peminjaman = int(input("Masukkan nomor peminjaman: "))
  cek_nomor = False
  for i in range(len(borrow_datas_gadget)):
    if (borrow_datas_gadget[i][0] == nomor_peminjaman):
      cek_nomor = True
  if (cek_nomor):
    tanggal_pengembalian = input("Tanggal pengembalian: ")
    jumlah_pengembalian = int(input("Jumlah pengembalian: "))
    new_return_history = [add_id_return, borrow_datas_gadget[i][0], tanggal_pengembalian, jumlah_pengembalian]
    return_data_gadget.append(new_return_history)
    jumlah_gadget = jumlah_pengembalian + datas_gadget[i][3]
    datas_gadget[i][3] = jumlah_gadget
    borrow_datas_gadget[i][5] = "Ya"
    print("Item " + borrow_datas_gadget[i][2] + " (x" + str(jumlah_pengembalian) + ") telah dikembalikan")
  else:
    print("Tidak ada item yang dipinjam")

kembalikan()
