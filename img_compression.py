import cv2
img = cv2.imread("building.jpg")
cv2.imwrite("compressed_image.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,50])
cv2.imwrite("compressed_image.png",img,[cv2.IMWRITE_PNG_COMPRESSION,9])
cv2.imwrite("compressed_image.webp",img,[cv2.IMWRITE_WEBP_QUALITY,50])