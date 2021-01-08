# coding=utf-8
import numpy as np
import argparse
import cv2
# 全局变量
#VIDEO_PATH = 'Ch15_20160801072000_20160801081259.avi' # 视频地址
VIDEO_PATH = 'bag.mp4' # 视频地址
EXTRACT_FOLDER = 'bag/' # 存放帧图片的位置
EXTRACT_FREQUENCY =30 # 帧提取频率

# 定义旋转rotate函数
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]
 
    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)
 
    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
 
    # 返回旋转后的图像
    return rotated


def extract_frames(video_path, dst_folder, index):
    # 主操作
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
            save_path = "{}/bag_01{:>03d}.jpg".format(dst_folder, index)
            #cv2.imwrite(save_path, frame)
            # 构造参数解析器
            #ap = argparse.ArgumentParser()
            #ap.add_argument("-i", "--image", required=True, help="Path to the image")
            #args = vars(ap.parse_args())
 
            # 加载图像并显示
            #image = cv2.imread(args["image"])
            #cv2.imshow("Original", image)
            #旋轉
            rotated = rotate(frame, 0)
            #cv2.imshow("Rotated by 90 Degrees", rotated)
            cv2.imwrite(save_path, rotated)
            index += 1
        count += 1
    video.release()
    # 打印出所提取帧的总数
    print("Totally save {:d} pics".format(index-1))


def main():
    # 递归删除之前存放帧图片的文件夹，并新建一个
    import shutil
    try:
        shutil.rmtree(EXTRACT_FOLDER)
    except OSError:
        pass
    import os
    os.mkdir(EXTRACT_FOLDER)
    # 抽取帧图片，并保存到指定路径
    extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)


if __name__ == '__main__':
    main()
