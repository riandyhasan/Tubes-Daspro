f = open("gadget.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace('"', "") for raw_line in raw_lines]

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(6):
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

def year_check(sign,year, gadget_year):
    check = False
    if (sign == "="):
        if (year == gadget_year):
            check = True
    elif (sign == ">"):
        if (year < gadget_year):
            check = True
    elif (sign == "<"):
        if (year > gadget_year):
            check = True
    elif (sign == ">="):
        if (year <= gadget_year):
            check = True
    elif (sign == "<="):
        if (year >= gadget_year):
            check = True

    return check


raw_header = lines.pop(0)
header = convert_string_to_array(raw_header)
data_gadget = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data)
  data_gadget.append(real_values)

def run_caritahun():
    print("======================================")
    print("============ CARI TAHUN ==============")
    print("======================================\n")

    year = int(input("Masukkan tahun: "))
    category = input("Masukkan kategori: ")

    print("\nHasil pencarian:")
    count = 0
    for i in range (len(lines)):
        if year_check(category,year, data_gadget[i][5]):
            print("\nNama             : {}".format(data_gadget[i][1]))
            print("Deskripsi        : {}".format(data_gadget[i][2]))
            print("Jumlah           : {}".format(data_gadget[i][3]))
            print("Rarity           : {}".format(data_gadget[i][4]))
            print("Tahun Ditemukan  : {}".format(data_gadget[i][5]))
            count += 1

    if count == 0:
        print("Tidak ada gadget yang ditemukan")
