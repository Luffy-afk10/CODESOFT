
import cv2
import dlib
import numpy as np


detector = dlib.get_frontal_face_detector()


predictor = dlib.shape_predictor('C:/Users/Ereny/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/site-packages/dlib/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('C:/Users/Ereny/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/site-packages/dlib/dlib_face_recognition_resnet_model_v1.dat')

image = cv2.imread('image.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = detector(gray)

for face in faces:
    
    landmarks = predictor(gray, face)
    face_descriptor = facerec.compute_face_descriptor(image, landmarks)
    
  
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)


cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()