from hashing import *
from readcsv import data_user, header3

def username_availability(reg_username, data_username):
    available = True
    if (reg_username == data_username):
        available = False

    return (available)

def modify_data(id, username, name, address, password, role):
    data = [id+1, username, name, address, password, role]
    return data

def check_availability():
  id = 165000 + len(data_user)
  name = input("\nMasukkan nama: ")
  username = input("Masukkan username: ")
  password = input("Masukkan password: ")
  address = input("Masukkan alamat: ")
  can = True

  for i in range (len(data_user)):
      if not(username_availability(username, data_user[i][1])):
          can = False

  if can:
    password = SHA3(256)._hash(password)
    data_user.append(modify_data(id, username, name, address, password, "user"))
    print ("Register telah berhasil!")
    
  else:
    user_input = input("\nUsername telah digunakan! \nIngin mengulang proses register lagi? (Ketik 't' untuk 'tidak' dan apapun untuk melanjutkan): ")
    if user_input != "t":
      check_availability()


def register():
  print("===================================")
  print("============ REGISTER =============")
  print("===================================\n")

  check_availability()



def convert_datas_to_string():
  string_data = ";".join(header3) + "\n"
  for arr_data in data_user:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data



