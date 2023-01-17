import cv2
img=cv2.imread("butterfly.jpg")
text_to_show="I am a butterfly"
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,220))
cv2.imshow("das",img)
cv2.waitKey(0)