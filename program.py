import cv2
import os
import numpy as np


def rotateImage(image, angle):

    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rotation_matrix = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rotation_matrix, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def plato(x, y, h, w, img):

    bool = 0;

    cv2.rectangle(img, (25, 11), (160, 31), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 11), (308, 31), (255, 125, 224), 2)

    if x + w > 25 and x + w <= 160:
        if y + h > 11 and y + h <= 31:
            bool = 1
    if x > 160 and x < 308:
        if y + h > 11 and y + h <= 31:
            bool = 1



    cv2.rectangle(img, (43, 31), (160, 51), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 31), (280, 51), (255, 125, 224), 2)

    if x + w > 43 and x + w <= 160:
        if y + h > 31 and y + h <= 51:
            bool = 1
    if x > 160 and x < 280:
        if y + h > 31 and y + h <= 51:
            bool = 1



    cv2.rectangle(img, (50, 51), (160, 71), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 51), (265, 71), (255, 125, 224), 2)

    if x + w > 50 and x + w <= 160:
        if y + h > 51 and y + h <= 71:
            bool = 1
    if x > 160 and x < 265:
        if y + h > 51 and y + h <= 71:
            bool = 1



    cv2.rectangle(img, (60, 71), (160, 91), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 71), (250, 91), (255, 125, 224), 2)

    if x + w > 60 and x + w <= 160:
        if y + h > 71 and y + h <= 91:
            bool = 1
    if x > 160 and x < 250:
        if y + h > 71 and y + h <= 91:
            bool = 1



    cv2.rectangle(img, (72, 91), (160, 171), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 91), (240, 171), (255, 125, 224), 2)

    if x + w > 72 and x + w <= 160:
        if y + h > 91 and y + h <= 171:
            bool = 1
    if x > 160 and x < 240:
        if y + h > 91 and y + h <= 171:
            bool = 1



    cv2.rectangle(img, (80, 171), (160, 191), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 171), (240, 191), (255, 125, 224), 2)

    if x + w > 80 and x + w <= 160:
        if y + h > 171 and y + h <= 191:
            bool = 1
    if x > 160 and x < 240:
        if y + h > 171 and y + h <= 191:
            bool = 1



    cv2.rectangle(img, (80, 191), (160, 231), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 191), (235, 231), (255, 125, 224), 2)

    if x + w > 80 and x + w <= 160:
        if y > 191 and y <= 231:
            bool = 1
    if x > 160 and x < 235:
        if y > 191 and y <= 231:
            bool = 1



    cv2.rectangle(img, (75, 231), (160, 251), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 231), (238, 251), (255, 125, 224), 2)

    if x + w > 75 and x + w <= 160:
        if y > 231 and y <= 251:
            bool = 1
    if x > 160 and x < 238:
        if y > 231 and y <= 251:
            bool = 1



    cv2.rectangle(img, (80, 251), (160, 271), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 251), (240, 271), (255, 125, 224), 2)

    if x + w > 80 and x + w <= 160:
        if y > 251 and y <= 271:
            bool = 1
    if x > 160 and x < 240:
        if y > 251 and y <= 271:
            bool = 1



    cv2.rectangle(img, (75, 271), (160, 311), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 271), (250, 311), (255, 125, 224), 2)

    if x + w > 75 and x + w <= 160:
        if y > 271 and y <= 311:
            bool = 1
    if x > 160 and x < 250:
        if y > 271 and y <= 311:
            bool = 1



    cv2.rectangle(img, (45, 311), (160, 331), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 311), (252, 331), (255, 125, 224), 2)

    if x + w > 45 and x + w <= 160:
        if y > 311 and y <= 331:
            bool = 1
    if x > 160 and x < 252:
        if y > 311 and y <= 331:
            bool = 1



    cv2.rectangle(img, (0, 331), (160, 351), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 331), (255, 351), (255, 125, 224), 2)

    if x + w > 0 and x + w <= 160:
        if y > 331 and y <= 351:
            bool = 1
    if x > 160 and x < 255:
        if y > 331 and y <= 351:
            bool = 1



    cv2.rectangle(img, (0, 351), (160, 364), (255, 125, 224), 2)
    cv2.rectangle(img, (160, 351), (348, 364), (255, 125, 224), 2)

    if x + w > 0 and x + w <= 160:
        if y > 351 and y <= 364:
            bool = 1
    if x > 160 and x < 384:
        if y > 351 and y <= 364:
            bool = 1

    return bool


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

counter_1 = 0
counter_2 = 0

pocetni = 0
sledeci = 0
kaunter = 0

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

    contours_plato = []

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
        dilate = cv2.dilate(inverse, rectangle_kernel, iterations = 1)
        # cv2.imshow('Dilate', dilate)

        image = frame_rotate.copy()

        contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:

            x, y, w, h = cv2.boundingRect(cnt)

            if plato(x, y, h, w, image) is 1:
                contours_plato.append(cnt)

        # print('Ovde')

        cv2.drawContours(image, contours_plato, -1, (0, 0, 255), 2)

        cv2.imshow('Contours', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if pocetni is not 0:

            sve = len(contours)
            print('Sve sledece %d' % sve)

            kaunter += sve
            print('Kaunter %d' % kaunter)

            cv2.rectangle(image, (20, 11), (310, 50), (255, 0, 0), 2)
            cv2.rectangle(image, (1, 320), (348, 364), (255, 0, 0), 2)

        counter_2 += 1
        # print('DRUGO %d' % counter_2)

        print('DRUGO')

        if counter_2 is 1:
            pocetni = len(contours)
            print('Pocetni 1 %d' % pocetni)
        else:
            pocetni = kaunter
            print('Pocetni RESTO %d' % pocetni)

        kaunter = pocetni
        print('Kaunter II %d' % kaunter)

    # counter_1 += 1
    # print('PRVO %d' % counter_1)

    print('PRVO')

    oldi = frame_gray

capture.release()
