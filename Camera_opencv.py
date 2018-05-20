import cv2;
clicked = False;
def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


face_cascade = cv2.CascadeClassifier('E:/anaconda/Library/etc/haarcascades/haarcascade_frontalface_default.xml');
eye_cascade = cv2.CascadeClassifier('E:/anaconda/Library/etc/haarcascades/haarcascade_eye.xml');

cameraCapture = cv2.VideoCapture(0);
cv2.namedWindow("MyWindow");
cv2.setMouseCallback('MyWindow',onMouse);

print('Showing camera feed.Click window or press any key to stop');
success,frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    success,frame = cameraCapture.read();
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
    faces = face_cascade.detectMultiScale(gray,1.3,5);
    for (x,y,w,h) in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2);
        roi_gray = gray[y:y+h,x:x+w];

    eyes = eye_cascade.detectMultiScale(roi_gray,1.03,5,0,(40,40));
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2);
    cv2.imshow('MyWindow', frame)

cv2.destroyWindow('MyWindow');
cameraCapture.release();