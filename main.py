from carirarity import carirarity
from caritahun import caritahun
from login import login
from register import register
from TambahItem import run_tambahitem
import os

role = login()

cmd = input(">>> ")

def command_admin(cmd):
    if cmd == "register":
        register()
    elif cmd == "carirarity":
        carirarity()
    elif cmd == "caritahun":
        caritahun()
    elif cmd == "tambahitem":
        run_tambahitem()
    else:
        print("Input tidak valid!")

def command_user(cmd):
    if cmd == "carirarity":
        carirarity()
    elif cmd == "caritahun":
        caritahun()
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
