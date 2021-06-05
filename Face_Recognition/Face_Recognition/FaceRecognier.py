import numpy as np
import cv2
import numpy as np
from GetImageToData import *
from Train_Data import *
import sys
import platform
from Main import *

def GetProfile(id):
    myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "@nvp111111", database = "nhan_dien_sv")
    query = "SELECT * FROM people WHERE id="+str(id)
    cur = myconn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    
    profile=None
    for row in records:
        profile=row

    cur.close()
    myconn.close()
    return profile


def Recognize(idList):
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainningData.yml')
   
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    fontface=cv2.FONT_HERSHEY_SIMPLEX

    while (True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            id,confidence=recognizer.predict(roi_gray)
            if(confidence<43):
                profile=GetProfile(id)
                if(profile!=None):
                    cv2.putText(frame,""+profile[1]+" "+str(100-round(confidence, 2)),(x+10,y+h+30),fontface,1,(0,255,0),2)
                    if id not in idList:
                        idList.append(id)
                       
            else:
                cv2.putText(frame,"UnKnown"+" "+str(round(confidence, 2)),(x+10,y+h+30),fontface,1,(0,0,255),2)
       
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    #out.release()
    cv2.destroyAllWindows()