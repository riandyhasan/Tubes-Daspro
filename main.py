from csv import data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history
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
import os

role, id_user = login()

data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history = data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history

cmd = input(">>> ")

def command_admin(cmd, id_user, datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history):
    global data_user, data_gadget, data_consumable
    if cmd == "register":
        data_user = register()
    elif cmd == "carirarity":
        carirarity()
    elif cmd == "caritahun":
        caritahun()
    elif cmd == "tambahitem":
        data_gadget, data_consumable = tambahitem()
    elif cmd == "hapusitem":
        data_gadget, data_consumable = hapusitem()
    elif cmd == "ubahjumlah":
        data_gadget, data_consumable = ubahjumlah()
    elif cmd == "riwayatpinjam":
        riwayatpinjam()
    elif cmd == "riwayatkembali":
        riwayatkembali()
    elif cmd == "riwayatambil":
        riwayatambil()
    elif cmd == "save":
        run_save(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history)
    elif cmd == "exit":
        exit(data_user, datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history)
    elif cmd == "help":
        help_admin()
    else:
        print("Input tidak valid!")

def command_user(cmd, id_user, datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history):
    global data_gadget, data_gadget_borrow, data_gadget_return, data_consumable, data_consumable_history
    if cmd == "carirarity":
        carirarity()
    elif cmd == "caritahun":
        caritahun()
    elif cmd == "pinjam":
        data_gadget, data_gadget_borrow = pinjam(id_user)
    elif cmd == "kembalikan":
        data_gadget, data_gadget_borrow, data_gadget_return = kembalikan()
    elif cmd == "minta":
        data_consumable, data_consumable_history = minta(id_user)
    elif cmd == "save":
        run_save(datas_user, datas_gadget, datas_consumable, datas_gadget_borrow, datas_gadget_return, datas_consumable_history)
    elif cmd == "exit":
        exit(data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history)
    elif cmd == "help":
        help_user() 
    else:
        print("Input tidak valid!")

if role == "admin":
    while True:
        command_admin(cmd, id_user, data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history)
        cmd = input(">>> ")
elif role == "user":
    while True:
        command_user(cmd, id_user, data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history)
        cmd = input(">>> ")


