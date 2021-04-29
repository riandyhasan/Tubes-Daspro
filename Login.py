from readcsv import data_user
from hashing import *

def validate_account(log_username, log_password, data, n):
  idx = -1
  log_password = SHA3(256)._hash(log_password)
  for i in range (n):
    if log_username == data[i][1] and log_password  == data[i][4]:
      idx = i
  return (idx)

def login():
  print("================================")
  print("============ LOGIN =============")
  print("================================\n")

  baris = len(data_user)
  username_login = input("Masukkan username: ")
  pass_login = input("Masukkan password: ")
  cek = False

  while not(cek):
    if validate_account(username_login, pass_login, data_user, baris) > -1:
      idx_nama = validate_account(username_login, pass_login, data_user, baris)
      print("Halo {}! Selamat datang di AiTeBeh!".format(data_user[idx_nama][2]))
      role = data_user[idx_nama][5]
      if role == "admin":
        print("Anda login sebagai admin!")
      else:
        print("Anda login sebagai user!")
      cek = True
    else:
      print("Username atau password salah! Silahkan login ulang!\n")
      username_login = input("Masukkan username: ")
      pass_login = input("Masukkan password: ")
  
  return role



    