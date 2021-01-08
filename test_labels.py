from zipfile import ZipFile
import cv2


path_video = "/home/robert/labels_videos/Test/traffic.avi"
filename_zipfile = '29_CAR_Traffic.zip'
vidObj = cv2.VideoCapture(path_video)
with ZipFile(filename_zipfile, 'r') as zipObj:
           listfiles = zipObj.namelist()
           for filename in listfiles :
                     zipObj.extract(filename)
                     success, image = vidObj.read()
                     file_name_video = str(filename).rstrip('.text')
                     print(file_name_video)
                     cv2.imwrite(file_name_video+".jpg", image)
                     
                    
   
                       
                      
