import cv2
import mysql.connector
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)



cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('D:\\facedetect\\haarcascade_frontalface_default.xml')
db_connection = mysql.connector.connect(
        host='localhost',
             user='root',
             password='root',
             database='africoding-db'
)
cursor = db_connection.cursor()
cursor.execute("SELECT id_condidat FROM user ORDER BY id_condidat DESC LIMIT 1;")
last_id = cursor.fetchone()
cursor.close()
#print( last_id[0]) if last_id else None
Id = last_id[0] +1

#def capture_image():
    # Capture de l'image depuis la webcam
   # camera = cv2.VideoCapture(0)
   # _, image = camera.read()
    #camera.release()
    #return image


#def convert_image_to_binary(image):
    # Conversion de l'image en données binaires
   # retval, buffer = cv2.imencode('.jpg', image)
  #  return buffer.tobytes()
#def save_image_to_database(image_data):
    #id_condidat = data.get('id_condidat')
    #image = data.get('image')  
    # Connexion à la base de données MySQL
   # connection = mysql.connector.connect(
       # host='localhost',
       # user='root',
       # password='root',
       # database='africoding-db'
   # )    
   # cursor = connection.cursor()    
    # Requête SQL pour insérer l'image dans la table appropriée    
    #sql_query = "INSERT INTO users (id_condidat ,image) VALUES (%s,%s)"
    #cursor.execute(sql_query ,(Id,image_data))
      # Valider la transaction
    #connection.commit()    
    # Fermer la connexion
    #cursor.close()
    #connection.close()
#if __name__ == "__main__":
    # Capturer l'image
    #image = capture_image()                    
    # Convertir l'image en données binaires
   # image_data = convert_image_to_binary(image)   
    # Enregistrer l'image dans la base de données
    #save_image_to_database(image_data)
    #product = {'name': name, 'description': description, 'price': price}
    
@app.route('/ma_fonction', methods=['GET'])
def test():
 sampleNum=0
 while(True):
    cam = cv2.VideoCapture(0)
    ret, img = cam.read()
    gray = cv2.cvtColor(img,0)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite('D:\\facedetect\dataSet\\.'+str(Id) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    #wait for 100 miliseconds
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>20:
   # return ("123")
        break
    cam.release()
    cv2.destroyAllWindows()
    #return ("captures enregistrées");     
if __name__ == '__main__':
    app.run()

    
    
