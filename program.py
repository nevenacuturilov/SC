import cv2

# **lista sa imenima svih 10 videa kroz koju moze da se prodje da bi se svaki video ucitao i analizirao
# za sada se radi sa samo jednim videom
name = "videos/video6.mp4"

# ucitavanje videa
frame_num = 0  # index frejma
cap = cv2.VideoCapture(name)  # open video
print(cap.isOpened())  # true ako je otvoren - **da se doda za GRESKU
cap.set(1, frame_num)  # napravljen property za indeksiranje frejmova

# analiza videa frejm po frejm
while True:
    print(frame_num)
    frame_num += 1
    ret_val, frame = cap.read()  # ret je true or false, cita frejm po frejm
    
    # ako frejm nije zahvacen - javi se greska kad nema ovog dela koda zato sto se ne uhvati bas svaki
    # frejm pa onda ovo ispod nema s cim da radi
    if not ret_val:
        break

    '''if ret_val == 'false':
        break'''  # ne radi - zasto?

cap.release()
