import shutil
import os 

path ='/home/robert/Desktop/4_smoking/obj/'
path_1 = '/home/robert/Desktop/4_smoking/annotation_txt/'
os.mkdir(path_1)


for file_name in os.listdir(path):
         if file_name.endswith('.txt'):
                      print(file_name)
                      shutil.copy(path+file_name,path_1+file_name)

              
           



