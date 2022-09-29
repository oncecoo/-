import os
import numpy as np

def read_cls(file_name):
    file = open(file_name,'r').readlines()

    f = [l.split(' ') for l in file]
    return f

def read_list(l):

    for i in range(len(l)):
        if float(l[i][0]) == 0:
            return True
    return False

def remove_file(file_name):
    os.remove(file_name)

path = './src/labels'
img_path = './src/images'
path_list = os.listdir(path)
num = 0
for file in path_list:
    file_list = read_cls(os.path.join(path,file))
    name,_ = file.split('.')
    ret = read_list(file_list)
    if ret == True:
        num += 1

        os.remove(os.path.join(path,name+'.txt'))
        os.remove(os.path.join(img_path,name+'.jpg'))
print('error file has {}'.format(num))
