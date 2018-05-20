import cv2;
import sys;
import numpy as np;
clicked = False;
def onMouse(event,x,y,flags,param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

def face_rec():
    names = ['zhuhe','unknow'];
    X, y = [], [];
    c = 0;
    i=0;
    im = cv2.imread('D:/python_code/data/' + str(i) + '.pgm', cv2.IMREAD_GRAYSCALE);
    cv2.imshow("Image", im)
    for i in range(100):
        try:
            im = cv2.imread('D:/python_code/data/'+str(i)+'.pgm', cv2.IMREAD_GRAYSCALE);
            X.append(np.asarray(im, dtype=np.uint8));
            y.append(c);
        except IOError:
            print("I/O error");
        except:
            print("Unexpected error:", sys.exc_info()[0]);
    y=np.asarray(y,dtype=np.int32);
    model = cv2.face.EigenFaceRecognizer_create();
    model.train(np.asarray(X),np.asarray(y));
    cameraCapture = cv2.VideoCapture(0);
    face_cascade = cv2.CascadeClassifier('E:/anaconda/Library/etc/haarcascades/haarcascade_frontalface_default.xml');
    while (True):
        read, img = cameraCapture.read();
        faces = face_cascade.detectMultiScale(img, 1.3, 5);
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2);
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
            roi = gray[x:x + w, y:y + h];
            try:
                roi = cv2.resize(roi,(200,200),interpolation=cv2.INTER_LINEAR);
                params = model.predict(roi);
                print("Label:%s,Confidence:%.2f" %(params[0],params[1]));
                cv2.putText(img,names[params[0]],(x,y),1, 2, (0,255,0), 2);
            except:
                continue;
        cv2.imshow("Face_Classifier",img);
        cv2.setMouseCallback('Face_Classifier', onMouse);
        if cv2.waitKey(1) != -1 or clicked:
            break;
    cv2.destroyWindow("Face_Classifier");
    cameraCapture.release();

if __name__ == "__main__":
    face_rec();