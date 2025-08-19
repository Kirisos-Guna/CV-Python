import cv2
import matplotlib.pyplot as plt

img= cv2.imread("image.jpg")
h,w=img.shape[:2]
m=cv2.getRotationMatrix2D((w//2,h//2),180,1)
rotated=cv2.warpAffine(img,m,(w,h))
plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
