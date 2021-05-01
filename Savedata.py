import os
from writecsv import convert_datas_to_string, header, header2, header3, header4, header5, header6

def check(n):
    return n in os.listdir()

def new(n):
    os.makedirs(n)

def save(n, str_ch, str_c, str_gbh, str_grh, str_user, str_gadget):
    with open(n+"/consumable_history.csv", "w") as file:
        file.write(str_ch)

    with open(n+"/consumable.csv", "w") as file:
        file.write(str_c)

    with open(n+"/gadget_borrow_history.csv", "w") as file:
        file.write(str_gbh)

    with open(n+"/gadget_return_history.csv", "w") as file:
        file.write(str_grh)

    with open(n+"/user.csv", "w") as file:
        file.write(str_user)

    with open(n+"/gadget.csv", "w") as file:
        file.write(str_gadget)

def run_save(data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history):
    str_ch, str_c, str_gbh, str_grh, str_user, str_gadget = convert_datas_to_string(header6, data_consumable_history), convert_datas_to_string(header5, data_consumable), convert_datas_to_string(header4, data_gadget_borrow), convert_datas_to_string(header, data_gadget_return), convert_datas_to_string(header2, data_user), convert_datas_to_string(header3, data_gadget)
    namafolder =input("Masukkan nama folder penyimpanan: ")
    if check(namafolder):
        save(namafolder, str_ch, str_c, str_gbh, str_grh, str_user, str_gadget)
        print ("Saving...")
        print("Data telah disimpan pada folder {}!".format(namafolder))
    else:
        new(namafolder)
        save(namafolder, str_ch, str_c, str_gbh, str_grh, str_user, str_gadget)
        print ("Saving...")
        print("Data telah disimpan pada folder {}!".format(namafolder))
   

    