import cv2

img=cv2.imread("Galaxy.jpg",0)
"""print(img)
print(type(img))
print(img.shape)
print(img.ndim)
cv2.imshow("galaxy",img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("galaxy",resized_image)
cv2.imwrite("Galaxy_resized_img.jpg",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()