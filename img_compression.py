import cv2
img = cv2.imread("building.jpg")
cv2.imwrite("compressed_image_30.jpg",img,[(cv2.IMWRITE_JPEG_QUALITY),30])
cv2.imwrite("compressed_image_90.jpg",img,[(cv2.IMWRITE_JPEG_QUALITY),90])