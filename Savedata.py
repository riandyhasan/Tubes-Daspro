import os

def checkFolder(n):
    return n in os.listdir()

def newFolder(n):
    os.makedirs(n)

def saveFolder(n):
    A = open(os.getcwd() + '\\consumable_history.csv','r')
    with open(n+"/consumable_history.csv", "w") as file:
        data = ''
        for i in A:
            data = data + i
        file.write(data)

    B = open(os.getcwd() + '\\consumable.csv','r')
    with open(n+"/consumable.csv", "w") as file:
        data = ''
        for i in B:
            data = data + i
        file.write(data)
    
    C = open(os.getcwd() + '\\gadget_borrow_history.csv','r')
    with open(n+"/gadget_borrow_history.csv", "w") as file:
        data = ''
        for i in C:
            data = data + i
        file.write(data)

    D = open(os.getcwd() + '\\gadget_return_history.csv','r')
    with open(n+"/gadget_return_history.csv", "w") as file:
        data = ''
        for i in D:
            data = data + i
        file.write(data)

    E = open(os.getcwd() + '\\User.csv', 'r')
    with open(n+"/user.csv", "w") as file:
        data = ''
        for i in E:
            data = data + i
        file.write(data)
    
    F = open(os.getcwd() + '\\gadget.csv', 'r')
    with open(n+"/gadget.csv", "w") as file:
        data = ''
        for i in F:
            data = data + i
        file.write(data)

namafolder =input("Masukkan nama folder penyimpanan: ")
if checkFolder(namafolder):
    saveFolder(namafolder)
else:
    newFolder(namafolder)
    saveFolder(namafolder)
    print ("Saving...")
    print("Data telah disimpan pada folder {}!".format(namafolder))
    

   
   

    
