def rarity_check(find, gadget_rarity):
    check = False
    if (find == gadget_rarity):
        check = True
    return check


def rarityfind(data_gadget):
  rare = input("\nMasukkan rarity: ")

  print("\nHasil pencarian:")
  count = 0
  for i in range (len(data_gadget)):
      if rarity_check(rare, data_gadget[i][4]):
          print("\nNama             : {}".format(data_gadget[i][1]))
          print("Deskripsi        : {}".format(data_gadget[i][2]))
          print("Jumlah           : {}".format(data_gadget[i][3]))
          print("Rarity           : {}".format(data_gadget[i][4]))
          print("Tahun Ditemukan  : {}".format(data_gadget[i][5]))
          count += 1

  if count == 0:
      print("Tidak ada gadget yang ditemukan")
  

def carirarity(data_gadget):
  print("\n============ CARI RARITY =============\n")
  rarityfind(data_gadget)
  
  user_input = input("\nApakah Anda ingin mengetahui entry data lainnya?(Ketik 't' untuk 'tidak' dan ketik apapun untuk melanjutkan): ")
  while user_input != "t":
      rarityfind(data_gadget)
      user_input = input("\nApakah Anda ingin mengetahui entry data lainnya?(Ketik 't' untuk 'tidak' dan ketik apapun untuk melanjutkan): ")