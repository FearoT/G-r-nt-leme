import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret, kare = kamera.read()
    hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)
    kirmizi_alt_sinir = np.array([0, 120, 40])  # renk, doygunluk, parlaklık.
    kirmizi_ust_sinir = np.array([10, 220, 90])
    maske = cv2.inRange(hsv, kirmizi_alt_sinir, kirmizi_ust_sinir)
    sonuc = cv2.bitwise_and(kare, kare, mask=maske)
    cv2.imshow('Kirmizi Nesne Tespit Etme', sonuc)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # q ya basarak programdan çıkma.
        break
kamera.release()
cv2.destroyAllWindows()