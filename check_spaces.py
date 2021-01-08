import os
#import fileinput
path ='/home/robert/darknet/data/kishore_dataset/1_backpack/backpack_annot/'
path_1 ='/home/robert/darknet/data/kishore_dataset/1_backpack/'

#path_1 = '/home/robert/Desktop/labels_2.0/'
#s.mkdir(path_1)

for file_name in os.listdir(path):
              print(file_name)
              file_data =""
              with open(path+file_name,'r') as file12:
                              file_data =file12.readlines()
                              #print(file_data[0])
                              for line_one in file_data:
                                            #print("lineoneeee",line_one[:3])
                                            if(line_one.count(' ')>5):
                                                          print("file_name=",file_name)
                                                          f1 = open(path_1+"test",'a')
                                                          f1.write(file_name)
                                                          f1.write('\n')
                                                          f1.close()
