path='/home/robert/darknet/data/kishore_dataset/0_person/person_annot/'
path_1 = '/home/robert/darknet/data/kishore_dataset/0_person/person_obj/'

import os

for file_name in os.listdir(path):
              #print("file namee",file_name)
              nam = file_name.rstrip('.txt')
              ren = "person_"+file_name.rstrip('.txt')[-10:]
              print("renameee",ren)
              if nam+".jpg" in os.listdir(path_1):
                           print("entered loop")
                           os.rename(path_1+nam+".jpg",path_1+ren+".jpg")#(test2 empty test2 to test1)
                           os.rename(path+nam+".txt",path+ren+".txt")
