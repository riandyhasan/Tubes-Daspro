from CariRarity import run_carirarity
from CariTahun import run_caritahun
from Login import run_login
from Register import run_register
from TambahItem import run_tambahitem
import os

role = run_login()

cmd = input(">>> ")

def command_admin(cmd):
    if cmd == "register":
        run_register()
    elif cmd == "carirarity":
        run_carirarity()
    elif cmd == "caritahun":
        run_caritahun()
    elif cmd == "tambahitem":
        run_tambahitem()
    else:
        print("Input tidak valid!")

def command_user(cmd):
    if cmd == "carirarity":
        run_carirarity()
    elif cmd == "caritahun":
        run_caritahun()
    else:
        print("Input tidak valid!")

if role == "admin":
    while cmd != "exit":
        command_admin(cmd)
        cmd = input(">>> ")
elif role == "user":
    while cmd != "exit":
        command_user(cmd)
        cmd = input(">>> ")
