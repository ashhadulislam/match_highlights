import numpy as np
import cv2
import time
import os

# folder_name = "resources"


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

play_folder = '../frames/plays/'
goal_folder = '../frames/goals/'

# os.mkdir(folder)

# start_time= ["01:09","01:51","02:03"]
# end_time= ["01:12", "01:59","02:06"]

capture_duration = [
    (52000, 54000),
    (92000, 101000),
    (105000, 109000),
    (114000,120000),
    (165000,165001),
]

count = 0
success = True


# start from 0
start_time=0

for the_file in files:
    file_name=the_file.split(".")[0]
    frame_rate = int(get_frame_rate("../videos/"+the_file))
    count=0
    vidcap = cv2.VideoCapture("../videos/"+the_file)
    for goal_start, goal_end in capture_duration:
        # this part to get frames
        # of the non goal part
        vidcap.set(cv2.CAP_PROP_POS_MSEC, start_time)
        time_temp=start_time
        print("At the beginning, this will run from {}, till {}".format(time_temp,goal_start))

        
        success=True
        while success and time_temp<goal_start:
            success, image = vidcap.read()
            count+=1
            # save only the nth frame
            if count%frame_rate==0:
                to_save=os.path.join(play_folder,file_name+ "_frame{:d}.jpg".format(count))
                print("Saving goals at ",to_save)
                cv2.imwrite(to_save, image)
            
            time_temp=vidcap.get(cv2.CAP_PROP_POS_MSEC)
            # print(time_temp)





        # this part to get frames
        # of the goal part
        # now the frames before the goal have been proessed
        # we can now read the frames from 
        # goal_start to goal_end
        time_temp=goal_start
        print("The goal part, this will run from {}, till {}".format(time_temp,goal_end))
        while success and time_temp<goal_end:
            success, image = vidcap.read()
            count+=1
            to_save=os.path.join(goal_folder,file_name+ "_frame{:d}.jpg".format(count))
            print("Saving plays at ",to_save)
            cv2.imwrite(to_save, image)            
            time_temp=vidcap.get(cv2.CAP_PROP_POS_MSEC)
            # print(time_temp)

        start_time=vidcap.get(cv2.CAP_PROP_POS_MSEC)


# for start_time_ms, end_time_ms in capture_duration:
#     vidcap.set(cv2.CAP_PROP_POS_MSEC, start_time_ms)
#     while success and vidcap.get(cv2.CAP_PROP_POS_MSEC) <= end_time_ms:
#         success, image = vidcap.read()
#         print('Read a new frame: ', success)
#         cv2.imwrite(os.path.join(folder, "frame{:d}.jpg".format(count)), image)
#         count += 1
#     print("{} images are extacted in {}.".format(count, folder))

# for one_file in files:

#     while (vidcap.get(cv2.CAP_PROP_POS_MSEC) < start_time_ms and cv2.CAP_PROP_POS_MSEC) > end_time_ms:
#         count_save = 0
#         path_to_file = folder_name + "/" + one_file
#         frame_rate = int(get_frame_rate(path_to_file))
#         i = 0
#         while (vidcap.isOpened()):
#             ret, frame = vidcap.read()
#             if ret == False:
#                 break
#             if i % frame_rate == 0:
#                 cv2.imwrite(os.path.join(folder2, "frame{:d}.jpg".format(count_save)), frame)
#                 count_save += 1
#                 print("{} images are extacted in {}.".format(count_save, folder2))
#             i += 1

