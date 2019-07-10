import cv2
import os
import numpy as np

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rotation_matrix = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rotation_matrix, image.shape[1::-1], flags = cv2.INTER_LINEAR)
  return result

# ime foldera u kojem se nalaze video snimci
folder_name = 'videos/'

# lista sa imenima svih 10 videa kroz koju moze da se prodje da bi se svaki video ucitao i analizirao
video_paths = []

for video_name in os.listdir(folder_name):
    video_path = os.path.join(folder_name, video_name)
    video_paths.append(video_path)

# print(video_paths)
# print("Broj video snimaka: ", len(video_paths))

# za sada se radi sa samo jednim videom
name = 'videos/video4.mp4'

# ucitavanje videa

frame_id = 0  # index frejma
capture = cv2.VideoCapture(name)  # open video
# print(capture.isOpened())  # true ako je otvoren - *** da se doda za GRESKU
capture.set(1, frame_id)  # napravljen property za indeksiranje frejmova

oldi = None

counter = 0

# analiza videa frejm po frejm

while True:
    frame_id += 1
    return_value, frame = capture.read()  # ret je true or false, cita frejm po frejm
    # cv2.imshow('Frame', frame)

    # ako frejm nije zahvacen - javi se greska kad nema ovog dela koda zato sto se ne uhvati bas svaki
    # frejm pa onda ovo ispod nema s cim da radi
    if not return_value:
        break

    '''if ret_val == 'false':
        break'''  # ne radi - zasto? ** probati sa !=

    # dalje se sa frejmom radi kao sa bilo kojom drugom slikom

    frame_crop = frame[90:460, 170:530]  # brojevi su rucno podeseni - mozda je moglo i malo drugacije
    # cv2.imshow('Crop', frame_crop)

    frame_rotate = rotateImage(frame_crop, -4)
    # cv2.imshow('Rotate', frame_rotate)

    frame_rgb = cv2.cvtColor(frame_rotate, cv2.COLOR_BGR2RGB)
    # cv2.imshow('RGB', frame_rgb)

    frame_gray = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2GRAY)
    # cv2.imshow('Gray', frame_gray)

    # print('00')

    if oldi is not None:
        # cv2.imshow('Oldi', oldi)
        # print(oldi)

        difference = cv2.subtract(frame_gray, oldi)
        # cv2.imshow('Difference', difference)

        binary = cv2.adaptiveThreshold(difference, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3)
        # cv2.imshow('Binary', binary)

        inverse = ~binary
        # cv2.imshow('Inverse', inverse)

        kernel = np.ones((3, 3))
        rectangle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 10))
        dilate = cv2.dilate(inverse, rectangle_kernel, iterations=1)
        # cv2.imshow('Dilate', dilate)

        # OBICNA DIL ?!

        contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        image = frame_rotate.copy()
        cv2.drawContours(image, contours, -1, (0, 0, 255), 2)

        cv2.imshow('Contours', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    oldi = frame_gray

    # counter += 1
    # print('PRVO %d' % counter)

    # print('PRVO')

capture.release()
