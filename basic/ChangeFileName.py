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
leave_file_name_num = -10
for f in files:
    os.rename(f, os.path.basename(f)[leave_file_name_num:])
