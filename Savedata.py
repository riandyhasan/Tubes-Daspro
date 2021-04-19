
import os
import pandas as pd


os.chdir('../Desktop')

df1 = open(os.getcwd() + '\\consumable_history.csv','r+')
df2 = open(os.getcwd() + '\\consumable.csv','r+')
df3 = open(os.getcwd() + '\\gadget_borrow_history.csv','r+')
df4 = open(os.getcwd() + '\\gadget_return_history.csv','r+')
df5 = open(os.getcwd() + '\\User.csv', 'r+')
df6 = open(os.getcwd() + '\\gadget.csv', 'r+')


namafolder = input('Masukkan nama folder penyimpanan: ')

newpath = os.getcwd() + '\{}'.format(namafolder)
for parent, dirs, files in os.walk(os.getcwd()): # ini sesuaiin sama directory
    if(namafolder in dirs):
        for _,_,filex in os.walk(newpath):
            for i in filex:
                os.remove(newpath + '\\{}'.format(i))
        os.rmdir(newpath)
    break
        
os.mkdir(namafolder)

df1.to_csv(newpath +'/consumable_history.csv' ) 
df2.to_csv(newpath +'/consumable.csv' )
df3.to_csv(newpath +'/gadget_borrow_history.csv' )
df4.to_csv(newpath +'/gadget_return_history.csv' )
df5.to_csv(newpath +'/User.csv' )
df6.to_csv(newpath +'/gadget.csv' )

print('Files is saved in {}\{}'.format(os.getcwd(),namafolder))

