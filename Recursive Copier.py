# Copies all your files from multiple sources to the destination recursively

import os
import shutil

cnt=1

def copier(src, destination):
    global cnt
    allFiles = os.listdir(src)

    for file in allFiles:   
        if os.path.isdir(src+file):
            copier(src+file+'/', destination)

        else:           # else is used to avoid copying folders also
            shutil.copyfile(src + file, destination + file)
            print("Copied file #", cnt)
            cnt+=1

source = list(input("Enter multiple source directories separated by spaces : \n").strip().split())
destination = input("Enter Destination : ")


# Validating Sources
invalid_srcs = []
valid_srcs = []
for src in source:
    if os.path.isdir(src):
        valid_srcs.append(src)
    else:
        invalid_srcs.append(src)

if len(invalid_srcs) > 0:
    print("Following source directories does not exist and will be ignored :")
    for src in invalid_srcs:
        print(src)
    source = valid_srcs


# Creating destination if doesn't exists
if not os.path.exists(destination):
    os.makedirs(destination)

for src in source:
    copier(src, destination)
