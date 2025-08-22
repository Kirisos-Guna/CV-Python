import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2D Translation
M = np.float32([[1, 0, 50],[0,1,50]])
translate = cv2.warpAffine(img, M, (img.shape[1],img.shape[0]))

# 2D Rotation
m= cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 45, 1)
Rotate = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# 3D Prespective Transform
pts1 = np.float32([[50,50],[200,50],[50,200],[200,200]])
pts2 = np.float32([[10,100],[200,50],[100,200],[220,220]])
M = cv2.getPerspectiveTransform(pts1, pts2)
Prespective = cv2.warpPerspective(img,M,(img.shape[1],img.shape[0]))

titiles = ["Original","Translation","Rotation","Prespective"]
images = [img,translate,Rotate,Prespective]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i]),plt.title(titiles[i])
    plt.axis("off")
plt.show()