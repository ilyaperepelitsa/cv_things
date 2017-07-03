import cv2
import numpy as np

canvas = np.zeros((500, 500, 3), dtype = "uint8")
# print(canvas.shape[1])
cv2.rectangle(canvas, (0, 0), (canvas.shape[1], canvas.shape[0]), (0, 0, 255), -1)
for i in range(0, 501, 50):
    cv2.rectangle(canvas, (i , 0), (i + 50, 25), (0, 0, 0), -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# import cv
# [i for i in range(0, 501, 25)]
