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
        draw_image = cv2.imread(save_as_img_path) # 이미지를 불러옴

        cv2.rectangle(draw_image,(x,y),(x+w,y+h),(255,255,0),2) # 불러온 이미지의 얼굴 부분 좌표에 네모를 그림

        draw_image_width = draw_image.shape[1] # 이미지의 width 길이
        draw_image_height = draw_image.shape[0] # 이미지의 height 높이

        cv2.imshow("draw_show", draw_image) # 네모가 그려진 이미지를 보여줌

        key_down_event = cv2.waitKeyEx(0) # 키를 입력받음
        key = chr(key_down_event) # key_down_event 변수에 입력된 키 값은 ascii 값으로 저장 되어 있는데 chr 함수를 사용해서 문자열로 바꿈

        cv2.destroyWindow("draw_show") # 키를 입력받는 동시에 네모가 그려진 이미지를 지움

        if key == 's': # 입력받은 키가 s면 이미지 저장 ( 특정 부분만 잘라서 ) # 대문자 S면 이미지 전체 저장 # s가 아니면 아무 동작도 X 
            if draw_image_width - (x + w + 20) > 0 and draw_image_height - (y + h + 20) > 0 and draw_image_width > (x + w + 20) and draw_image_height > y + h + 20 :
                slice_draw_image = draw_image[y - 20: y + h + 20, x - 20 : x + w + 20]
                cv2.imwrite(save_as_drwa_img_path + str((x + y + w + h)) + ".jpg", slice_draw_image)
            else:
                slice_draw_image = draw_image[y: y + h, x : x + w]
                cv2.imwrite(save_as_drwa_img_path + str((x + y + w + h)) + ".jpg", slice_draw_image)

        if key == 'S':
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
