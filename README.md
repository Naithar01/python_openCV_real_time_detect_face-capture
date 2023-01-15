# Real-time capture Cam & detect Face

## 작동 방식 
1. 파일 실행시에 캠이 켜짐과 동시에 키 입력을 받음
    1. e를 누르면 프로그램 종료
    2. c를 누르면 현재 캠을 캡처 - 저장 | 저장된 이미지를 보여주는 Show_Capture_Face_Image 함수 실행
    <hr />
2. Show_Capture_Face_Image 함수는 저장된 이미지를 보여주는데 현재 이미지에서 얼굴을 검출할지 그게 아니면 다시 캠을 캡처할지 키를 입력 받음
    1. g를 누르면 현재 이미지에서 얼굴을 검출하는 | Detect_Face 함수 실행
    2. g를 제외한 키를 누르면 다시 캠 캡처로
    <hr />
3. Detect_Face 함수에서는 얼굴을 검출*인식 하는데 만약에 이미지에 인식된 얼굴이 없으면 다시 캡처 모드로
    <hr />
4. (3) 검출된 이미지가 있으면 순차적으로 캡처 이미지에 얼굴이라고 검출된 부분에 네모를 그려줌
    1. s를 누르면 네모가 그려진 버전의 이미지를 저장
    2. s를 제외한 키를 누르면 다음 이미지, 마지막 이미지면 다시 캡처로 