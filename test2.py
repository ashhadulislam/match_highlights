import numpy as np
import cv2
import time
import os

folder_name = "resources"


def get_frame_rate(file_name):
    video = cv2.VideoCapture(file_name);

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    video.release();
    return fps


# files=["vid1.mp4","vid2.mp4","vid3.mp4"]

files = ["merged.mov"]

folder = 'test'
folder2 = 'test2'

os.mkdir(folder)

# start_time= ["01:09","01:51","02:03"]
# end_time= ["01:12", "01:59","02:06"]

capture_duration = [
    (65400, 67200),
    (90600, 95400),
    (120000, 123600),
]
vidcap = cv2.VideoCapture('resources/merged.mov')
count = 0
success = True

for start_time_ms, end_time_ms in capture_duration:
    vidcap.set(cv2.CAP_PROP_POS_MSEC, start_time_ms)
    while success and vidcap.get(cv2.CAP_PROP_POS_MSEC) <= end_time_ms:
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        cv2.imwrite(os.path.join(folder, "frame{:d}.jpg".format(count)), image)
        count += 1
    print("{} images are extacted in {}.".format(count, folder))

for one_file in files:

    while (vidcap.get(cv2.CAP_PROP_POS_MSEC) < start_time_ms and cv2.CAP_PROP_POS_MSEC) > end_time_ms:
        count_save = 0
        path_to_file = folder_name + "/" + one_file
        frame_rate = int(get_frame_rate(path_to_file))
        i = 0
        while (vidcap.isOpened()):
            ret, frame = vidcap.read()
            if ret == False:
                break
            if i % frame_rate == 0:
                cv2.imwrite(os.path.join(folder2, "frame{:d}.jpg".format(count_save)), frame)
                count_save += 1
                print("{} images are extacted in {}.".format(count_save, folder2))
            i += 1

