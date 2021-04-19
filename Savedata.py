
import os
import shutil
import pandas as pd


os.chdir('../Desktop')

df1 = pd.read_csv(os.getcwd() + '\\consumable_history.csv')
df2 = pd.read_csv(os.getcwd() + '\\consumable.csv')
df3 = pd.read_csv(os.getcwd() + '\\gadget_borrow_history.csv')
df4 = pd.read_csv(os.getcwd() + '\\gadget_return_history.csv')
df5 = pd.read_csv(os.getcwd() + '\\User.csv')
df6 = pd.read_csv(os.getcwd() + '\\gadget.csv')


namafolder = input('Masukkan nama folder penyimpanan: ')

newpath = os.getcwd() + '\{}'.format(namafolder)
for parent, dirs, files in os.walk(os.getcwd()): # ini sesuaiin sama directory
    if(namafolder in dirs):
        shutil.rmtree(namafolder)
        break
        
os.mkdir(namafolder)

df1.to_csv(newpath +'/consumable_history.csv' ) 
df2.to_csv(newpath +'/consumable.csv' )
df3.to_csv(newpath +'/gadget_borrow_history.csv' )
df4.to_csv(newpath +'/gadget_return_history.csv' )
df5.to_csv(newpath +'/User.csv' )
df6.to_csv(newpath +'/gadget.csv' )

print('Files is saved in {}\{}'.format(os.getcwd(),namafolder))

