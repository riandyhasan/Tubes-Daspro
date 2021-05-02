def kembalikan(borrow_datas_gadget, return_data_gadget, datas_gadget):
  print("\n============ KEMBALIKAN =============\n")
  id_return = return_data_gadget[-1][0]
  add_id_return = id_return + 1

  for i in range(len(borrow_datas_gadget)):
    print((i+1), borrow_datas_gadget[i][2])
    
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
    user_input = input("Ingin mengulang proses lagi? (Ketik 't' untuk 'tidak' dan apapun untuk melanjutkan): ")
    if user_input != "t":
      kembalikan(borrow_datas_gadget, return_data_gadget, datas_gadget)

  return datas_gadget, borrow_datas_gadget, return_data_gadget