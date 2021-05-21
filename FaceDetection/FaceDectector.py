import cv2;
from random import randrange;



trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

# img=cv2.imread('Unknown.jpg');
webcam=cv2.VideoCapture(0);

while True:
      successfull_frame_read,frame = webcam.read();

      greyScale_img=cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY);

      cv2.imshow('Clever programmer ' ,greyScale_img);
      cv2.waitKey(1);



      faceCordinated=trained_face_data.detectMultiScale(greyScale_img);

      for(x,y,w,h) in faceCordinated:
            cv2.rectangle(frame ,(x,y),(x+w,y+h),(0,255,0),2);

      cv2.imshow('nafey' ,frame);
      key= cv2.waitKey(1);

      if key==83 or key==113:
            break;
webcam.release()        



print("hello world")