from hashing import *

def username_availability(reg_username, data_username):
    available = True
    if (reg_username == data_username):
        available = False

    return (available)

def modify_data(id, username, name, address, password, role):
    data = [id+1, username, name, address, password, role]
    return data

def check_availability(data_user):
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
    name = name.title()
    data_user.append(modify_data(id, username, name, address, password, "user"))
    print ("Register telah berhasil!")
    return data_user
    
  else:
    user_input = input("\nUsername telah digunakan! \nIngin mengulang proses register lagi? (Ketik 't' untuk 'tidak' dan apapun untuk melanjutkan): ")
    if user_input != "t":
      check_availability(data_user)


def register( data_user):
  print("===================================")
  print("============ REGISTER =============")
  print("===================================\n")

  data_user = check_availability( data_user)

  return data_user

