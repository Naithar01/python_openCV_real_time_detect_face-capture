import cv2
import sys

save_as_img_path = "./assets/capture_image.jpg"  # 캠의 이미지를 저장할 경로 변수

save_as_drwa_img_path = "./assets/draw_image"  # 얼굴로 검출된 이미지를 저장할 경로 변수

vid = cv2.VideoCapture(0)  # VideoCapture 함수를 사용해서 캠을 vid 변수에 넣음
face_cascade = cv2.CascadeClassifier(
    './assets/haarcascade_frontalface_default.xml')


def Detect_Face():
    capture_face_image = cv2.imread(save_as_img_path)

    gray_capture_face_image = cv2.cvtColor(
        capture_face_image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_capture_face_image, 1.1, 4)

    if len(faces) == 0:
        return

    for (x, y, w, h) in faces:
        draw_image = cv2.imread(save_as_img_path)  # 이미지를 불러옴

        cv2.rectangle(draw_image, (x, y), (x+w, y+h),
                      (255, 255, 0), 2)  # 불러온 이미지의 얼굴 부분 좌표에 네모를 그림

        draw_image_width = draw_image.shape[1]  # 이미지의 width 길이
        draw_image_height = draw_image.shape[0]  # 이미지의 height 높이

        cv2.imshow("draw_show", draw_image)  # 네모가 그려진 이미지를 보여줌

        key_down_event = cv2.waitKeyEx(0)  # 키를 입력받음
        # key_down_event 변수에 입력된 키 값은 ascii 값으로 저장 되어 있는데 chr 함수를 사용해서 문자열로 바꿈
        key = chr(key_down_event)

        cv2.destroyWindow("draw_show")  # 키를 입력받는 동시에 네모가 그려진 이미지를 지움

        # 입력받은 키가 s면 이미지 저장 ( 특정 부분만 잘라서 ) # 대문자 S면 이미지 전체 저장 # s가 아니면 아무 동작도 X
        if key == 's':
            # 이미지의 얼굴 부분만(특정 부분) 저장할 때 얼굴로 인식된 부분의 네모보다 좀 더 길게 저장하는데 그 길이가 이미지보다 길어지면 네모 부분만 저장하는 조건문
            # 길이뿐만 아니라 높이도 똑같이
            if draw_image_width - (x + w + 20) > 0 and draw_image_height - (y + h + 20) > 0 and draw_image_width > (x + w + 20) and draw_image_height > (y + h + 20) and (x - 20) > 0 and (y - 20) > 0:
                slice_draw_image = draw_image[y -
                                              20: y + h + 20, x - 20: x + w + 20]
                cv2.imwrite(save_as_drwa_img_path +
                            str((x + y + w + h)) + ".jpg", slice_draw_image)
            else:
                slice_draw_image = draw_image[y: y + h, x: x + w]
                cv2.imwrite(save_as_drwa_img_path +
                            str((x + y + w + h)) + ".jpg", slice_draw_image)

        if key == 'S':
            cv2.imwrite(save_as_drwa_img_path +
                        str((x + y + w + h)) + ".jpg", draw_image)


def Show_Capture_Face_Image():
    capture_face_image = cv2.imread(save_as_img_path)  # 캠에서 저장한 이미지를 변수에 넣음

    cv2.imshow("capture_img", capture_face_image)  # 위 변수에 담긴 이미지를 봄

    cv2.destroyWindow("cam")  # 캠은 잠시 닫음

    key_down_event = cv2.waitKeyEx(0)  # 키를 입력받음
    # key_down_event 변수에 입력된 키 값은 ascii 값으로 저장 되어 있는데 chr 함수를 사용해서 문자열로 바꿈
    key = chr(key_down_event)

    cv2.destroyWindow("capture_img")  # 키를 입력받으면 위의 이미지도 닫음

    # 만약에 입력받은 키가 g면 얼굴 검출*인식 Detect_Face 함수로 # 그게 아니면 그냥 다시 캠으로 (이미지 저장)
    if key == 'g':
        Detect_Face()


while (True):
    _, cam_image = vid.read()  # vid 변수에는 캠이 담겨있는데 캠이 담고있는 이미지를 cam_image 변수에 담음

    cam_image = cv2.flip(cam_image, 2)  # 이미지를 좌우반전 | x축 혹은 y축을 기준으로 뒤집기 혹은 x, y 축을 기준으로 뒤집기

    cv2.imshow('cam', cam_image)  # 좌우반전한 이미지를 보여줌

    key_down_event = cv2.waitKeyEx(10)  # 키를 입력받는 부분

    if key_down_event != -1:
        # 키 값은 ascii 값으로 저장 되어 있는데 chr 함수를 사용해서 문자열로 바꿈
        key = chr(key_down_event)

        # e 를 입력하면 반복문 종료 -> 프로그램 종료
        if key == 'e':
            break
        # c 를 입력하면 이미지를 저장 & Show_Capture_Face_Image 함수 실행
        elif key == 'c':
            cv2.imwrite(save_as_img_path, cam_image)
            Show_Capture_Face_Image()

vid.release()
cv2.destroyAllWindows()
sys.exit()
