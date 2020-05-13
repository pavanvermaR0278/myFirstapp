import cv2,time

camera_port = 0
camera = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
a=0
while True:
    a=a+1
    return_value, image = camera.read()
    #cv2.imwrite("image.jpg", image)
    #time.sleep(3)
    cv2.imshow("image_cam",image)
    #print(return_value)
    #print(image)
    key=cv2.waitKey(1)
    if key== ord('q'):
        break
print(a)
camera.release()
cv2.destroyAllWindows()