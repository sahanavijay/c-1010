import cv2
import numpy as np
black=np.zeros ([600,600])
black[200:400,200:400]=255
print(black)
#f_col=black[2:4,2:4]=255
#print(f_col)
cv2.imshow("black",black)
cv2.waitKey(0)