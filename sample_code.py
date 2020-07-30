import cv2
import time
# Opens the Video file
folder_name="playvids"

def get_frame_rate(file_name):
    video = cv2.VideoCapture(file_name);

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    video.release(); 
    return fps


# files=["vid1.mp4","vid2.mp4","vid3.mp4"]

files=["vid1.mp4"]

# Let us go for 1 frame at every second this means that we will have to skip the number of frames as returned by get_fram_rate() function

for one_file in files:
    count_save=0
    file_precedent=one_file.split(".")[0]
    path_to_file=folder_name+ "/"+one_file
    frame_rate=int(get_frame_rate(path_to_file))
    print(file_precedent,frame_rate)
    cap= cv2.VideoCapture(path_to_file)
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if i%frame_rate==0:
            cv2.imwrite(folder_name+'/'+file_precedent+'/'+file_precedent+"_"+str(count_save)+'.jpg',frame)
            count_save+=1
        i+=1
    print("Number of frames saved ",count_save)
    print("Number of frames processed ",i)


cap.release()
cv2.destroyAllWindows()
