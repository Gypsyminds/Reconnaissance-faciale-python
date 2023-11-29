import cv2
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
import base64

CORS(app)  # Pour activer la prise en charge de CORS

# Charger le classificateur de cascade et le modèle de reconnaissance
detector = cv2.CascadeClassifier('D:\\facedetect\\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('D:\\facedetect\\trainner\\trainner.yml')

# Autres paramètres
font_scale = 2
font_thickness = 3
line_type = cv2.LINE_AA

@app.route('/detect_faces', methods=['GET'])
def detect_faces():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    id = 0  # Initialisez id avec une valeur par défaut

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        id, conf = recognizer.predict(gray[y:y+h, x:x+w])

    x = 100
    y = 200
    h = 50
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 0, 0)
    thickness = 2
    cv2.putText(img, str(id), (x, y+h), font, font_scale, color, thickness)
    #cv2.imshow('frame',img);
    # Convertir l'image en format JSON pour la réponse
    #_, buffer = cv2.imencode('.jpg', img)
    #g_base64 = base64.b64encode(buffer).decode()
    #buffer = cv2.imencode('.jpg', img)
    #frame_base64 = base64.b64encode(buffer).decode()
  #  response_data = {
   #     'id': id,
    #    'frame_base64': frame_base64
    #}
    if cv2.waitKey(100) & 0xFF == ord('q'):
    #break
        
     cam.release();
     cap.release();
     cv2.destroyAllWindows();
    #return cv2.imshow('frame',img);
    return jsonify(id);

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5202)
