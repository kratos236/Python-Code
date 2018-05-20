import cv2;
import os,sys;
import numpy as np;
def read_images(path,sz=None):
    c=0;
    X,y=[],[];
    for dirname,dirnames,filenames in os.walk(path):
         for subdirname in dirnames:
             subject_path = os.path.join(dirname,subdirname);
             for filename in os.listdir(subject_path):
                try:
                    if(filename == ".directory"):
                        continue;
                    filepath = os.path.join(subject_path,filename);
                    im = cv2.imread(os.path.join(subject_path,filename),cv2.IMREAD_GRAYSCALE);
                    if (sz is not None):
                        im = cv2.resize(im,(200,200));
                    X.append(np.asarray(im,dtype=np.uint8));
                    y.append(c);
                except IOError:
                    print("I/O error");
                except:
                    print("Unexpected error:",sys.exc_info()[0]);
                    raise;
             c = c + 1;
    return [X,y];

