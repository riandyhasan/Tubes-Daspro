import datetime
import time

f = open("consumable_history.csv", "r")
raw_lines = f.readlines()
f.close()
line = [raw_line.replace('"', "") for raw_line in raw_lines]
lines = [i.replace("\n","") for i in line]

def convert_array_data_to_real_values(array_data, n):
    arr_cpy = array_data[:]
    for i in range(n):
        if(i == 0) or (i == 4):
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
data_consumable_return = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data, 5)
  data_consumable_return.append(real_values)

# print(data_consumable_return)
data_consumable_return_copy = data_consumable_return[:]
data_consumable_return_copy_sorted = sorted(data_consumable_return_copy, key=lambda x: datetime.datetime.strptime(x[3], "%d/%m/%Y").strftime("%Y-%m-%d"), reverse= True)
# print(data_consumable_return_copy_sorted )

for i in range(len(data_consumable_return_copy_sorted)):
    print("ID pengembalian: ", data_consumable_return_copy_sorted[i][0])
    print("Nama Pengambil: ", data_consumable_return_copy_sorted[i][1])
    print("Nama Consumable: ", data_consumable_return_copy_sorted[i][2])
    print("Tanggal Pengambilan: ", data_consumable_return_copy_sorted[i][3])
    print("Jumlah: ", data_consumable_return_copy_sorted[i][4])
    print("\n")
    time.sleep(2)
    if (i==4):
        user_input = input("Apakah Anda ingin mengetahui entry data lainnya?(Ketik 't' untuk 'tidak' dan ketik 'apapun' untuk 'melanjutkan'): ")
        if (user_input == 't'):
            break
