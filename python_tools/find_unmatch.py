path = '/home/robert/Desktop/4_smoking/obj/'
path_1='/home/robert/Desktop/4_smoking/annotation_txt_ver2.0/'
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
