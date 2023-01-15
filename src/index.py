import cv2
import sys

save_as_img_path = "./assets/capture_image.jpg"

save_as_drwa_img_path = "./assets/draw_image"

vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('./assets/haarcascade_frontalface_default.xml')

def Detect_Face():
    capture_face_image = cv2.imread(save_as_img_path)

    gray_capture_face_image = cv2.cvtColor(capture_face_image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_capture_face_image, 1.1, 4)

    if len(faces) == 0:
        return
    
    for (x,y,w,h) in faces:
        draw_image = cv2.imread(save_as_img_path)

        cv2.rectangle(draw_image,(x,y),(x+w,y+h),(255,255,0),2) 

        cv2.imshow("draw_show", draw_image)

        key_down_event = cv2.waitKeyEx(0)
        key = chr(key_down_event)

        cv2.destroyWindow("draw_show")

        if key == 's':
            cv2.imwrite(save_as_drwa_img_path + str((x + y + w + h)) + ".jpg", draw_image)

def Show_Capture_Face_Image():
    capture_face_image = cv2.imread(save_as_img_path)

    cv2.imshow("capture_img", capture_face_image)

    cv2.destroyWindow("cam")

    key_down_event = cv2.waitKeyEx(0)
    key = chr(key_down_event)

    cv2.destroyWindow("capture_img")

    if key == 'g':
        Detect_Face()

while(True):
    _, cam_image = vid.read()

    cam_image = cv2.flip(cam_image, 2)
  
    cv2.imshow('cam', cam_image)
      
    key_down_event = cv2.waitKeyEx(10)

    if key_down_event != -1:
        key = chr(key_down_event)

        if key == 'e':
            break

        elif key == 'c':
            cv2.imwrite(save_as_img_path, cam_image)
            Show_Capture_Face_Image()
            
vid.release()
cv2.destroyAllWindows()
sys.exit()
