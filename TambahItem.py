f = open("gadget.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace('"', '') for raw_line in raw_lines]

g = open("consumable.csv","r")
raw_lines2 = g.readlines()
f.close()
lines2 = [raw_line2.replace('"', "") for raw_line2 in raw_lines2]

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

def delete_n(word):
    word = word.replace('\n','')
    return word


raw_header = lines.pop(0)
header = convert_string_to_array(raw_header)
data_gadget = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data, 6)
  data_gadget.append(real_values)

raw_header2 = lines2.pop(0)
header2 = convert_string_to_array(raw_header2)
data_consum = []
for line in lines2:
  array_of_data2 = convert_string_to_array(line)
  real_values2 = convert_array_data_to_real_values(array_of_data2, 5)
  data_consum.append(real_values2)
for i in range (len(lines2)):
  data_consum[i][4] = delete_n(data_consum[i][4])

def run_tambahitem():
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


