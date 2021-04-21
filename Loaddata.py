import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('Folder')
args = parser.parse_args()

os.chdir('../Desktop/' + args.Folder)
print('Loading...')

print('Selamat datang di "Kantong Ajaib!"')

df1 = open(os.getcwd() + '\\consumable_history.csv','r')
df2 = open(os.getcwd() + '\\consumable.csv','r')
df3 = open(os.getcwd() + '\\gadget_borrow_history.csv','r')
df4 = open(os.getcwd() + '\\gadget_return_history.csv','r')
df5 = open(os.getcwd() + '\\User.csv', 'r')
df6 = open(os.getcwd() + '\\gadget.csv', 'r')


