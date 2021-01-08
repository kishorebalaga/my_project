path = '/home/robert/Desktop/4_smoking/obj/'
import os 
for file_name in os.listdir(path):
         if file_name.endswith('.txt'):
                      os.remove(path+file_name)
