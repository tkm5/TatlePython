from glob import glob
import os

# get dir info
Curdir = os.getcwd()[:15]
path = Curdir + "/Documents/T&H_share/AGAROOT/1_民法"
# print(path)

# make file object
files = glob(path + "/*")
# print(files)

# return rename
leave_file_name_num = -8
# Change number here ↓
file_name_num = -3

final_file_name_num = leave_file_name_num + file_name_num
for f in files:
    os.rename(f, os.path.basename(f)[final_file_name_num:])
