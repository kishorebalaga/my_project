path='/home/robert/darknet/data/kishore_dataset/0_person/person_annot/'#old annotation folder
path_1 = '/home/robert/darknet/data/kishore_dataset/0_person/person_annotation/'#tar file extracted folder
#path_3 =path+"/new_person_annotation/"#new annotation folder
import os
from shutil import copyfile
#os.mkdir(path_3)
for file_name in os.listdir(path):
              print("fileeee_nameee",file_name)
              if file_name in os.listdir(path_1):
                          print("entered loops")
                          #copyfile(path_1+file_name,path_3+file_name)
                          os.replace(path_1+file_name,path+file_name)
