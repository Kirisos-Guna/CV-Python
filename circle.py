import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
cv2.circle(img,(130,100),50,(0,0,255),2)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()