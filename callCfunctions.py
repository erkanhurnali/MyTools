from ctypes import *
# c_file="./mylibl.so"
c_file="C:/Users/erkan/OneDrive/Belgeler/GitHub/MyTools/mylibl.so"
c_fun=CDLL(c_file)
c_fun.swap(int(1))
