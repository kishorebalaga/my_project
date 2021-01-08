# coding=utf-8
import numpy as np
import argparse
import cv2

# Global variable
VIDEO_PATH = '/home/robert/Desktop/test1/' # Video address
EXTRACT_FOLDER = '/home/robert/Desktop/test/' # Where to store the frame image
EXTRACT_FREQUENCY = 10 # Frame extraction frequency

# Defining a rotation function
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
            save_path = "{}/LTA-Ladder2_{:>03d}.jpg".format(dst_folder, index)
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
    # Recursively delete the folder where the frame image was stored before, and create a new one.
    import shutil
    try:
        shutil.rmtree(EXTRACT_FOLDER)
    except OSError:
        pass
    import os
    os.mkdir(EXTRACT_FOLDER)
    # Extract the frame image and save it to the specified path
    extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)


if __name__ == '__main__':
    main()

    
