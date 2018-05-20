import cv2;
clicked = False;
def generate():
    face_cascade = cv2.CascadeClassifier('E:/anaconda/Library/etc/haarcascades/haarcascade_frontalface_default.xml');
    eye_cascade = cv2.CascadeClassifier('E:/anaconda/Library/etc/haarcascades/haarcascade_eye.xml');
    cameraCapture = cv2.VideoCapture(0);
    count = 0;
    while (True):
        ret,frame = cameraCapture.read();
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
        faces = face_cascade.detectMultiScale(gray,1.3,5);
        for (x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2);
            f = cv2.resize(gray[y:y+h,x:x+w],(200,200));
            cv2.imwrite('D:/python_code/data/%s.pgm' % str(count),f);
            count += 1;

        cv2.imshow('MyWindow', frame)
        if cv2.waitKey(1)!=-1:
            break;
    cv2.destroyWindow('MyWindow');
    cameraCapture.release();

if __name__ == "__main__":
    generate();