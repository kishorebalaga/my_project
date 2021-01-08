import os
#import fileinput
#path ='/home/robert/Desktop/labels/'
path = '/home/robert/darknet/data/kishore_dataset/0_person/person_annot_final/'
#os.mkdir(path_1)

no_of_cls = 0
for file_name in os.listdir(path):
              #f =open(path+file_name)
              #for line in f.readlines():
              #         print("linesss",line)
              #         print("first number===",line[0])
              #         line[0]='2'
              #         print("first number after replacing",line[0])
              #print("entered first loop")
              #with fileinput.FileInput(path+file_name, inplace=True, backup='.bak') as file12:
              #               print("fileee12",file12)
              #               for line in file12 :
              #                   print('line is printing',line)
              #                   print('enteredd loooppp')
              #                   print(line.replace('5','2'),end=''
              #print(file_name)
              file_data =""
              with open(path+file_name,'r') as file12:
                              file_data =file12.readlines()
                              #print(file_data[0])
                              for line_one in file_data:
                                            #print("lineoneeee",line_one[:2])
                                            check_cls = line_one[:2].strip()
                                           # print("check_cls",check_cls)
                                            if(check_cls== '0'):
                                                          no_of_cls+=1
                                            else:
                                                          print("class name different",file_name)
                               
