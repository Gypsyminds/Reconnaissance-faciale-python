# server.py
import cv2
import time
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)


@app.route('/mafonctions', methods=['GET'])
def capture_face():
    output_folder='D:\\facedetect\\capturesdutest';
    os.makedirs(output_folder, exist_ok=True)
    # Initialisation de la capture vidéo
    cap = cv2.VideoCapture(0)  # Utilisez la webcam par défaut (0) ou spécifiez le chemin vers une caméra si nécessaire
    capture_counter = 0
    while True:
        ret, frame = cap.read()  # Capture une image depuis la caméra
        if ret:
            capture_counter += 1
            # Traitez l'image (détection de visage, etc.) si nécessaire
            # Sauvegardez l'image capturée dans un fichier ou envoyez-la au client Angular
            file_name = os.path.join(output_folder, f'capture_{capture_counter}.png')
            cv2.imwrite(file_name, frame)
            time.sleep(30)  # Capture d'image toutes les 30 secondes
            
        else:
            print("Erreur lors de la capture de l'image")
    
    cap.release()
    cv2.destroyAllWindows()

@app.route('/api/close-camera', methods=['GET'])
def close_camera():
  cap = cv2.VideoCapture(0)  # 0 indique la caméra par défaut, mais vous pouvez spécifier un autre numéro si vous avez plusieurs caméras.

  if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra.")
    exit()

# Lire des images de la caméra (à faire tant que nécessaire)
  while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Erreur: Impossible de lire la trame.")
        break
    
    # Vous pouvez faire du traitement d'image ici, si nécessaire.
    
    # Afficher la trame (facultatif)
    cv2.imshow('Camera', frame)

    # Attendre la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra et fermer toutes les fenêtres
    cap.release()
    cv2.destroyAllWindows()
    return "Caméra fermée avec succès"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200)
