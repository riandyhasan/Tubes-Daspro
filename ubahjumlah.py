f = open("gadget.csv","r")
raw_lines = f.readlines()
f.close()
line = [raw_line.replace('"', '') for raw_line in raw_lines]
lines = [i.replace("\n","") for i in line]

g = open("consumable.csv","r")
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
datas_consum = []
for line in lines2:
  array_of_data2 = convert_string_to_array(line)
  real_values2 = convert_array_data_to_real_values(array_of_data2, 5)
  datas_consum.append(real_values2)

def ubahjumlah():
    id = input("Masukkan ID: ")
    id_check = False
    if (id[0] == "G"):
        for i in range (len(datas_gadget)):
            if (datas_gadget[i][0] == id):
                id_check = True
        if (id_check):
            print("Tidak ada item dengan ID tersebut.")
        else:
            change_gadget = int(input("Masukkan Jumlah: "))

            if (change_gadget > 0 ):
                jumlah_gadget = change_gadget + datas_gadget[i][3]
                datas_gadget[i][3] = jumlah_gadget
                print(change_gadget + datas_gadget[i][3] + "berhasil ditambahkan. Stok sekarang: " + jumlah_gadget)
            else:
                jumlah_gadget = datas_gadget[i][3] - change_gadget
                datas_gadget[i][3] = jumlah_gadget
                print(change_gadget + datas_gadget[i][2] + "berhasil dibuang. Stok sekarang: " + jumlah_gadget)
    elif (id[0] == "C"):
        for i in range (len(datas_consum)):
            if (datas_consum[i][0] == id):
                id_check = True
        if (id_check):
            print("Tidak ada item dengan ID tersebut.")
        else:
            change_consumable = int(input("Masukkan Jumlah: "))

            if (change_consumable > 0 ):
                jumlah_consumable = change_consumable + datas_consum[i][3]
                datas_consum[i][3] = jumlah_consumable
                print(change_consumable + datas_consum[i][2] + "berhasil ditambahkan. Stok sekarang: " + jumlah_consumable)
            else:
                jumlah_consumable = datas_consum[i][3] - change_consumable
                datas_consum[i][3] = jumlah_consumable
                print(change_consumable + datas_consum[i][2] + "berhasil dibuang. Stok sekarang: " + jumlah_consumable)
    else:
        print("Gagal menambahkan item karena ID tidak valid")