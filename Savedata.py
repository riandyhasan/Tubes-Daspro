import os

def check(n):
    return n in os.listdir()

def new(n):
    os.makedirs(n)

def save(n):
    A = open(os.getcwd() + "\\consumable_history.csv","r")
    with open(n+"/consumable_history.csv", "w") as file:
        temp = " "
        for i in A:
            temp = temp + i
        file.write(temp)

    B = open(os.getcwd() + "\\consumable.csv","r")
    with open(n+"/consumable.csv", "w") as file:
        temp = " "
        for i in A:
            temp = temp + i
        file.write(temp)
    
    C = open(os.getcwd() + "\\gadget_borrow_history.csv","r")
    with open(n+"/gadget_borrow_history.csv", "w") as file:
        temp = " "
        for i in A:
            temp = temp + i
        file.write(temp)

    D = open(os.getcwd() + "\\gadget_return_history.csv","r")
    with open(n+"/gadget_return_history.csv", "w") as file:
        data = ''
        temp = " "
        for i in A:
            temp = temp + i
        file.write(temp)

    E = open(os.getcwd() + "\\user.csv", "r")
    with open(n+"/user.csv", "w") as file:
        temp = " "
        for i in A:
            temp = temp + i
        file.write(temp)
    
    F = open(os.getcwd() + "\\gadget.csv", "r")
    with open(n+"/gadget.csv", "w") as file:
        temp = " "
        for i in A:
            temp = temp + i
        file.write(temp)

namafolder =input("Masukkan nama folder penyimpanan: ")
if check(namafolder):
    save(namafolder)
    print ("Saving...")
    print("Data telah disimpan pada folder {}!".format(namafolder))
else:
    new(namafolder)
    save(namafolder)
    print ("Saving...")
    print("Data telah disimpan pada folder {}!".format(namafolder))
    

   
   

    