from CariRarity import *
from CariTahun import *
from Login import *
from Register import *
from TambahItem import *
import os

run_login()

cmd = input(">>> ")

def command(cmd):
    if cmd == "register":
        run_register()
    elif cmd == "carirarity":
        run_carirarity()
    elif cmd == "caritahun":
        run_caritahun()
    elif cmd == "tambahitem":
        run_tambahitem()

while cmd != "exit":
    command(cmd)
    cmd = input(">>> ")
