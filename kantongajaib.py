import argparse
import os
import time
from main import main

parser = argparse.ArgumentParser()
parser.add_argument('folder', type=str)
args = parser.parse_args()


def check_folder(n):
    return n in os.listdir()

print('Loading...')
time.sleep(1)

if (check_folder(args.folder)):
    print('Selamat datang di "Kantong Ajaib!"')

    f = open(args.folder + '\\gadget_return_history.csv','r')
    g = open(args.folder + '\\user.csv', 'r')
    h = open(args.folder + '\\gadget.csv', 'r')
    i = open(args.folder + '\\gadget_borrow_history.csv','r')
    j = open(args.folder + '\\consumable.csv','r')
    k = open(args.folder + '\\consumable_history.csv','r')
    raw_lines1 = f.readlines()
    f.close()
    line = [raw_line.replace('"', "") for raw_line in raw_lines1]
    lines = [raw_line.replace("\n","") for raw_line in line]

    raw_lines2 = g.readlines()
    g.close()
    line2 = [raw_line.replace('"', "") for raw_line in raw_lines2]
    lines2 = [raw_line.replace("\n","") for raw_line in line2]

    raw_lines3 = h.readlines()
    h.close()
    line3 = [raw_line.replace('"', "") for raw_line in raw_lines3]
    lines3 = [raw_line.replace("\n","") for raw_line in line3] 

    raw_lines4 = i.readlines()
    i.close()
    line4 = [raw_line.replace('"', "") for raw_line in raw_lines4]
    lines4 = [raw_line.replace("\n","") for raw_line in line4]

    raw_lines5 = j.readlines()
    j.close()
    line5 = [raw_line.replace('"', "") for raw_line in raw_lines5]
    lines5 = [raw_line.replace("\n","") for raw_line in line5]

    raw_lines6 = k.readlines()
    f.close()
    line6 = [raw_line.replace('"', "") for raw_line in raw_lines6]
    lines6 = [raw_line.replace("\n","") for raw_line in line6]

    def convert_array_data_to_real_values(array_data, n):
        arr_cpy = array_data[:]
        for i in range(n):
            if(i == 0) or (i == 1) or (i == 3):
                arr_cpy[i] = int(arr_cpy[i])
        return arr_cpy


    def convert_array_data_to_real_values2(array_data, n):
        arr_cpy = array_data[:]
        for i in range(n):
            if(i == 0):
                arr_cpy[i] = int(arr_cpy[i])
        return arr_cpy


    def convert_array_data_to_real_values3(array_data, n):
        arr_cpy = array_data[:]
        for i in range(n):
            if(i == 3) or (i == 5):
                arr_cpy[i] = int(arr_cpy[i])
        return arr_cpy


    def convert_array_data_to_real_values4(array_data, n):
        arr_cpy = array_data[:]
        for i in range(n):
            if(i == 0) or (i == 1) or (i == 4):
                arr_cpy[i] = int(arr_cpy[i])
        return arr_cpy

    def convert_array_data_to_real_values5(array_data, n):
        arr_cpy = array_data[:]
        for i in range(n):
            if(i == 3):
                arr_cpy[i] = int(arr_cpy[i])
        return arr_cpy

    def convert_array_data_to_real_values6(array_data, n):
        arr_cpy = array_data[:]
        for i in range(n):
            if(i == 0) or (i == 4):
                arr_cpy[i] = int(arr_cpy[i])
        return arr_cpy

    def convert_string_to_array(line):
        word = ""
        delete = ";"
        line += delete
        l = len(line)
        new_list = []
        for i in range(l):
            if (line[i] != delete):
                word += line[i]
            else:
                if (len(word) != 0):
                    new_list.append(word)
                word = ""
        return new_list

    raw_header = lines.pop(0)
    header = convert_string_to_array(raw_header)
    data_gadget_return = []
    for line in lines:
        array_of_data = convert_string_to_array(line)
        real_values = convert_array_data_to_real_values(array_of_data, len(lines))
        data_gadget_return.append(real_values)

    raw_header2 = lines2.pop(0)
    header2 = convert_string_to_array(raw_header2)
    data_user = []
    for line in lines2:
        array_of_data2 = convert_string_to_array(line)
        real_values2 = convert_array_data_to_real_values2(array_of_data2, len(lines2))
        data_user.append(real_values2)

    raw_header3 = lines3.pop(0)
    header3 = convert_string_to_array(raw_header3)
    data_gadget = []
    for line in lines3:
        array_of_data3 = convert_string_to_array(line)
        real_values3 = convert_array_data_to_real_values3(array_of_data3, len(lines3))
        data_gadget.append(real_values3)

    raw_header4 = lines4.pop(0)
    header4 = convert_string_to_array(raw_header4)
    data_gadget_borrow = []
    for line in lines4:
        array_of_data4 = convert_string_to_array(line)
        real_values4 = convert_array_data_to_real_values4(array_of_data4, len(lines4))
        data_gadget_borrow.append(real_values4)


    raw_header5 = lines5.pop(0)
    header5 = convert_string_to_array(raw_header5)
    data_consumable = []
    for line in lines5:
        array_of_data5 = convert_string_to_array(line)
        real_values5 = convert_array_data_to_real_values5(array_of_data5, len(lines5))
        data_consumable.append(real_values5)


    raw_header6 = lines6.pop(0)
    header6 = convert_string_to_array(raw_header6)
    data_consumable_history = []
    for line in lines6:
        array_of_data6 = convert_string_to_array(line)
        real_values6 = convert_array_data_to_real_values6(array_of_data6, len(lines6))
        data_consumable_history.append(real_values6)


    def convert_datas_to_string(header, data):
        string_data = ";".join(header) + "\n"
        for arr_data in data:
            arr_data_all_string = [str(var) for var in arr_data]
            string_data += ";".join(arr_data_all_string)
            string_data += "\n"
        return string_data
    
    main(data_user, data_gadget, data_consumable, data_gadget_borrow, data_gadget_return, data_consumable_history)

else:
    print("Tidak ada nama folder yang diberikan!")









