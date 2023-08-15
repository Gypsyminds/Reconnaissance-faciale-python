import cv2
import numpy as np
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

@app.route('/detect/<name>')
def detect():
    detector = cv2.CascadeClassifier('D:\\facedetect\\haarcascade_frontalface_default.xml');
    cap=cv2.VideoCapture(0);

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read('D:\\facedetect\\trainner\\trainner.yml')
    name=''
    id=0
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_thickness = 3
    line_type = cv2.LINE_AA

# Create a font object
    font = cv2.putText(font, 'Hello', (50, 50), font, font_scale, (0, 0, 255), font_thickness, line_type)
    while(True):
     ret,img=cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = detector.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        # Connexion à la base de données MySQL
    connection = mysql.connector.connect(
        host='localhost',
        password='root',
        database='africoding-db'
    )
    
    cursor = connection.cursor()
    #cursor.execute("SELECT full_name FROM condidat ;")
    cursor.execute("SELECT id_condidat , full_name FROM condidat ;")
   
    results = cursor.fetchall()
    for id_condidat , full_name in results:
     
     if id==id_condidat:
            id=id_condidat
            name=full_name
     
        #if id==2 :
         #   id="khouloud"
        #elif (id!=1):
         #   id = input('enter your id')


    x = 100  # Example value for the x-coordinate
    y = 200  # Example value for the y-coordinate
    h = 50   # Example value for the height

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 0, 0)  # Example value for the text color (in BGR format)
    thickness = 2            
    cv2.putText(img, name, (x, y+h), font, font_scale, color, thickness)
    cv2.imshow('frame',img);
    return print('hello' ,name)
    if cv2.waitKey(100) & 0xFF == ord('q'):
       #break
      cam.release();
      cap.release();
      cv2.destroyAllWindows();

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
   
