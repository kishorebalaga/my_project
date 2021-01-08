from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import re
import numpy as np
import argparse
import cv2
import random



EXTRACT_FREQUENCY = 10

def first():
    f = open("video1.txt","r")
    targetname = ""
    video_number = 00
    video =""
    images =[]
    for line in f:
           regex = re.compile('[.]')
           hours_starttime = 0
           hours_endtime = 0
           start_time=None
           end_time = 00
           print("lines=",line)
           if(regex.search(line)==None):
                print("seconds")
            #print(int(line.split('-')[0]))
                start_time = line.split('-')[0]
                start_time = start_time.strip()
                if(len(start_time)==5):
                          first_digit = start_time[0]
                          hours_starttime = first_digit*60*60
                print("start_time before",start_time)
                seconds_starttime = int(str(start_time[-2:]))
                minutes_starttime = int(str(start_time)[0:2])
                start_time = ((minutes_starttime*60)+(seconds_starttime)+hours_starttime)
                print("seconds_starttime",seconds_starttime)
                print("minutes_starttime",minutes_starttime)
                print("start_time",start_time)
                end_time = line.split('-')[1]
                end_time = (end_time.strip())
                
                print("end_time before strip",end_time)
                seconds_endtime = int(str(end_time)[-2:])
                minutes_endtime = int(str(end_time)[0:2])
                print("seconds_endtime",seconds_endtime)
                print("minutes_endtime",minutes_endtime) 
                
                print("end_time",end_time)
                video_number = video_number +1
                print(video_number)
           else:
                print("string is accepted",line)
                video = line.strip()
           print("--"+video+"--")
           if(start_time!=None):
                print('test')
                import os
                path = os.getcwd()
                path1 = path +"/AICCTV_CERTIS_Videos"
                os.mkdir(path1)                
                #folder_location = os.path.join(os.path.expanduser('~'),'Desktop','test1')
                #f1 = open(folder_location)
                print(path)
                ffmpeg_extract_subclip(video,start_time, end_time, targetname= path+"/AICCTV_CERTIS_Videos/"+video+"_"+str(start_time)+"-"+str(end_time)+".mp4")
                images.append(video+"_"+str(start_time)+"-"+str(end_time)+".mp4")
    i=0
    for img in images:
           print("images in folder",img)
           import os
           VIDEO_PATH = os.getcwd()+"/AICCTV_CERTIS_Videos/"+img 
           print(VIDEO_PATH) # Video address
           import os
           path = os.getcwd()
           path_images = path +"/AICCTV_CERTIS_CUT_IMAGES"
           os.mkdir(path_images)                
           EXTRACT_FOLDER = path+"/AICCTV_CERTIS_CUT_IMAGES/" # Where to store the frame image
           EXTRACT_FREQUENCY = 10 # Frame extraction frequency

           #import shutil
           #try:
            #   if(i<1):
            #        shutil.rmtree(EXTRACT_FOLDER)
           #except OSError:
            #   pass
           #import os
           #os.mkdir(EXTRACT_FOLDER)
           # Extract the frame image and save it to the specified path
           extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)
          # i=i+1
          # print(i)



def rotate(image, angle, center=None, scale=1.0):
    # Get image size
    (h, w) = image.shape[:2]
 
    # If the center of rotation is not specified, set the center of the image to the center of rotation
    if center is None:
        center = (w / 2, h / 2)
 
    # Perform rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
 
    # Return the rotated image
    return rotated


def extract_frames(video_path, dst_folder, index):
    # Main operation
    import cv2
    video = cv2.VideoCapture()
    if not video.open(video_path):
        print("can not open the video")
        exit(1)
    count = 1
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            save_path = "{0}/LTA-Ladder2_{1}{2}.jpg".format(dst_folder, index,random.randint(1,100000))
            #cv2.imwrite(save_path, frame)
            # Constructor parameter parser
            #ap = argparse.ArgumentParser()
            #ap.add_argument("-i", "--image", required=True, help="Path to the image")
            #args = vars(ap.parse_args())
 
            # Load image and display
            #image = cv2.imread(args["image"])
            #cv2.imshow("Original", image)
            #Rotate
            rotated = rotate(frame, 0)
            #cv2.imshow("Rotated by 90 Degrees", rotated)
            cv2.imwrite(save_path, rotated)
            index += 1
        count += 1
    video.release()
    # Print out the total number of extracted frames
    print("Totally save {:d} pics".format(index-1))

def main():
     first()
if __name__ == '__main__':
    main()


