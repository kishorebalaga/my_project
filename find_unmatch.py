path_1 = '/home/robert/darknet/data/kishore_dataset/5_escooter/esctr_annot/labels_2.0/'
path='/home/robert/darknet/data/kishore_dataset/5_escooter/esctr_obj/obj/'
import os
import shutil
#os.mkdir(path_1)

list_img =[]
list_txt = []
for file_name in os.listdir(path):
         file_name = file_name.rstrip('.jpg')
         list_img.append(file_name)
         
         #if file_name.endswith('.txt'):
                      #shutil.copy(path+file_name,path_1+file_name)
                      #os.remove(path+file_name)
                      
for file_name in os.listdir(path_1):
         file_name = file_name.rstrip('.txt')
         list_txt.append(file_name)


for img in list_img:
        
         if img in list_txt:
                pass
         else:
                print("image not there",img)

for txt in list_txt:
        
         if txt in list_img:
                pass
         else:
                print("text not there",txt)
