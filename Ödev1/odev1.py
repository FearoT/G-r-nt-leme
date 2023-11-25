import cv2
import matplotlib.pyplot as plt

foto = cv2.imread('tango.jpg')
gri_foto = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
cv2.imshow("Tango", gri_foto)
histogram = [0] * 256

for satir in gri_foto:
    for sutun in satir:
        histogram[sutun] += 1

plt.figure(figsize=(10, 7))
plt.bar(range(256), histogram, color='red')
plt.title('Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()
