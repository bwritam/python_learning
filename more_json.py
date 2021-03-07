
######################################################################
# Reading and writing csv files using numpy
######################################################################
# import numpy as np

# # write a csv file 
# x = [[1, 2,3], [2,3,4], [4,5,6]]
# write_path = r'C:\Users\Anik\Desktop\Pyfiles\writam_1.csv'
# np.savetxt(write_path, x, delimiter = ',')


# # read a csv file
# read_path = r"C:\Users\Anik\Desktop\Pyfiles\writam_1.csv"
# data = np.genfromtxt(read_path, delimiter = ',')
# print(data)


######################################################################
# Reading and writing JSON files
######################################################################
import json

# create\write a json file
# test_dictionary = {"apple": 40, "banana": 7, "orange": 15}
# write_path = r'C:\Users\Anik\Desktop\Pyfiles\writam_2.json'
# with open(write_path, 'w') as f:
# 	json.dump(test_dictionary, f)

# read a json file
read_path = r'C:\Users\Anik\Desktop\Pyfiles\writam_2.json'   # setting the file path
# opening and reading the file from the defined path
with open(read_path, 'r') as f:
	data = json.load(f)
# picking up the particular value from the file
my_settings = data['interval']
print('The content of the file is: {} and the interval setting is: {} \n'.format(data, my_settings))