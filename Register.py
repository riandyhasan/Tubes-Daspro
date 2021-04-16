from Hashing import *


f = open("user.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace('"', "") for raw_line in raw_lines]

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(6):
    if(i == 0):
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

def username_availability(reg_username, data_username):
    available = True
    if (reg_username == data_username):
        available = False

    return (available)

def modify_data(id, username, name, address, password, role):
    data = [id+1, username, name, address, password, role]
    return data

raw_header = lines.pop(0)
header = convert_string_to_array(raw_header)
data_akun = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data)
  data_akun.append(real_values)
for i in range (len(lines)):
  data_akun[i][5] = delete_n(data_akun[i][5])

def run_register():
  print("===================================")
  print("============ REGISTER =============")
  print("===================================\n")

  id = 165000 + len(data_akun)
  name = input("Masukkan nama: ")
  username = input("Masukkan username: ")
  password = input("Masukkan password: ")
  address = input("Masukkan alamat: ")
  can = True

  for i in range (len(data_akun)):
      if not(username_availability(username, data_akun[i][1])):
          can = False

  if can:
      password = SHA3(256)._hash(password)
      data_akun.append(modify_data(id, username, name, address, password, "user"))

def convert_datas_to_string():
  string_data = ";".join(header) + "\n"
  for arr_data in data_akun:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data

def print():
  datas_as_string = convert_datas_to_string()
  print(datas_as_string)

        
    



