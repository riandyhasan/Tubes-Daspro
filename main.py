from carirarity import carirarity
from caritahun import caritahun
from login import login
from register import register
from tambahitem import tambahitem
from hapusitem import hapusitem
from ubahjumlah import ubahjumlah
from gadget_borrow_history import riwayatpinjam
from gadget_return_history import riwayatkembali
from consumable_history import riwayatambil
from pinjam import pinjam
from kembalikan import kembalikan
from consumable import minta
from savedata import run_save
from help import help_admin, help_user
from exit import exit

data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history = [], [], [], [], [], []

def command_admin(cmd, id_user, datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history):
    global data_user, data_gadget, data_consumable
    if cmd == "register":
        data_user = register(datas_user)
    elif cmd == "carirarity":
        carirarity(datas_gadget)
    elif cmd == "caritahun":
        caritahun(datas_gadget)
    elif cmd == "tambahitem":
        data_gadget, data_consumable = tambahitem(datas_gadget, datas_consumable)
    elif cmd == "hapusitem":
        data_gadget, data_consumable = hapusitem(datas_gadget, datas_consumable)
    elif cmd == "ubahjumlah":
        data_gadget, data_consumable = ubahjumlah(datas_gadget, datas_consumable)
    elif cmd == "riwayatpinjam":
        riwayatpinjam(datas_user, datas_gadget_borrow, datas_gadget)
    elif cmd == "riwayatkembali":
        riwayatkembali(datas_gadget_return, datas_user, datas_gadget, datas_gadget_borrow)
    elif cmd == "riwayatambil":
        riwayatambil(datas_consumable_history)
    elif cmd == "save":
        run_save(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history)
    elif cmd == "exit":
        exit(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history)
    elif cmd == "help":
        help_admin()
    else:
        print("Input tidak valid!")

def command_user(cmd, id_user, datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history):
    global data_gadget, data_gadget_borrow, data_gadget_return, data_consumable, data_consumable_history
    if cmd == "carirarity":
        carirarity(datas_gadget)
    elif cmd == "caritahun":
        caritahun(datas_gadget)
    elif cmd == "pinjam":
        data_gadget, data_gadget_borrow = pinjam(id_user, datas_gadget, datas_gadget_borrow)
    elif cmd == "kembalikan":
        data_gadget, data_gadget_borrow, data_gadget_return = kembalikan(datas_gadget_borrow, datas_gadget_return, datas_gadget)
    elif cmd == "minta":
        data_consumable, data_consumable_history = minta(id_user, datas_consumable, datas_consumable_history, datas_user)
    elif cmd == "save":
        run_save(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history)
    elif cmd == "exit":
        exit(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history)
    elif cmd == "help":
        help_user() 
    else:
        print("Input tidak valid!")

def main(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history):
    global data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history
    data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history = datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history
    role, id_user = login(data_user)
    cmd = input(">>> ")
    if role == "admin":
        while True:
            command_admin(cmd, id_user, data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history)
            cmd = input(">>> ")
    elif role == "user":
        while True:
            command_user(cmd, id_user, data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history)
            cmd = input(">>> ")


