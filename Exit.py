from savedata import run_save
import sys
def exit(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history):
    N = (input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): "))
    while (N != "y") and (N != "Y") and (N !="n") and (N !="N"):
        print ("Masukkan salah, silahkan ulangi lagi!")
        N = (input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): "))
    if (N == "y") or (N == "Y"):
        run_save(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history)
        sys.exit()
    elif (N=="n") or (N=="N") : 
        sys.exit()
