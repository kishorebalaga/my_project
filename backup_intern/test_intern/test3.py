from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import re
import numpy as np
import argparse
import cv2


def first():
    f = open("video1.txt","r")
    targetname = ""
    video_number = 00
    video =""
    for line in f:
           regex = re.compile('[.]')
       
           start_time=None
           end_time = 00
           print("lines=",line)
           if(regex.search(line)==None):
                print("seconds")
            #print(int(line.split('-')[0]))
                start_time = line.split('-')[0]
                print(start_time)
                start_time = int(float(start_time.strip()))
                print("start_time",start_time)
                end_time = line.split('-')[1]
                end_time = int(float(end_time.strip()))
                print("end_time",end_time)
                video_number = video_number +1
                print(video_number)
           else:
                print("string is accepted",line)
                video = line.strip()
           print("--"+video+"--")
           if(start_time!=None):
                ffmpeg_extract_subclip(video,start_time, end_time, targetname= video+"_"+str(start_time)+"-"+str(end_time)+".mp4")
                print(targetname)


def main():
     first()
if __name__ == '__main__':
    main()
