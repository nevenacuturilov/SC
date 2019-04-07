import cv2
import os
import numpy as np

# lista sa imenima svih 10 videa kroz koju moze da se prodje da bi se svaki video ucitao i analizirao

folder_name = 'videos/'

video_paths = []

for video_name in os.listdir(folder_name):
    video_path = os.path.join(folder_name, video_name)
    print(video_path)
    video_paths.append(video_path)

print("Broj video snimaka: ", len(video_paths))

# za sada se radi sa samo jednim videom

name = "videos/video6.mp4"

# ucitavanje videa

frame_id = 0  # index frejma
capture = cv2.VideoCapture(name)  # open video
print(capture.isOpened())  # true ako je otvoren - ** da se doda za GRESKU
capture.set(1, frame_id)  # napravljen property za indeksiranje frejmova

# analiza videa frejm po frejm

while True:
    frame_id += 1
    return_value, frame = capture.read()  # ret je true or false, cita frejm po frejm

    # ako frejm nije zahvacen - javi se greska kad nema ovog dela koda zato sto se ne uhvati bas svaki
    # frejm pa onda ovo ispod nema s cim da radi
    if not return_value:
        break

    '''if ret_val == 'false':
        break'''  # ne radi - zasto? ** probati sa !=

    # dalje se sa frejmom radi kao sa bilo kojom drugom slikom

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_gray = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2GRAY)

    frame_blur = cv2.GaussianBlur(frame_gray, (0, 0), 3)
    cv2.addWeighted(frame_gray, 1.5, frame_blur, -0.5, 0)

    frame_crop = frame_gray[90:460, 170:530]  # brojevi su rucno podeseni - **mozda je moglo i drugacije

capture.release()

# **upis
