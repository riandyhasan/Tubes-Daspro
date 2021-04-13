f = open("user.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace('"', "") for raw_line in raw_lines]

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(6):
    if(i == 0):
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

def validate_account(log_username, log_password, data, n):
  idx = -1
  for i in range (n):
    if log_username == data[i][1] and log_password  == data[i][4]:
      idx = i
  return (idx)

raw_header = lines.pop(0)
header = convert_string_to_array(raw_header)
data_akun = []
for line in lines:
  array_of_data = convert_string_to_array(line)
  real_values = convert_array_data_to_real_values(array_of_data)
  data_akun.append(real_values)