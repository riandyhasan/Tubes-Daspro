from savedata import save, run_save
import sys
N = (input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): "))
while (N != "y") and (N != "Y") and (N !="n") and (N !="N"):
    print ("Masukkan salah, silahkan ulangi lagi!")
    N = (input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): "))
if (N == "y") or (N == "Y"):
    run_save()
    sys.exit()
elif (N=="n") or (N=="N") : 
    sys.exit()
