import os
#import fileinput
path ='/home/robert/Desktop/person/clean_annot_person/'
path_1 = '/home/robert/Desktop/person/labels_changed/'
os.mkdir(path_1)

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
              print(file_name)
              file_data =""
              with open(path+file_name,'r') as file12:
                              file_data =file12.readlines()
                              print(file_data[0])
                              for line_one in file_data:
                                            print("lineoneeee",line_one[0])
                                            line_0 = line_one[0].replace('1','0')# change the number depends on your requirement
                                            line_1 = line_one[1:]
                                            line_one = line_0 + line_1
                                            print(line_one)
                                            f1 =open(path_1+file_name,'a')
                                            f1.write(line_one)
                                            f1.close()
                              print(file_data)
              
              #file_data = file_data.replace('5','2')
              #with open(path+file_name,'w') as file123:
              #                file123.write(file_data)
              
