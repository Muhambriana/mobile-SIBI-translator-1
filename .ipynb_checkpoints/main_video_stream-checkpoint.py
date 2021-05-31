#Import the needed File for prediction
import os
import tensorflow as tf
import numpy as np
import cv2
import mediapipe as mp
import time
 
cap = cv2.VideoCapture(0)
 
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
 
pTime = 0
cTime = 0

gpu_devices = tf.config.experimental.list_physical_devices("GPU")
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)

#Define Classes in Dictionary and Load Created Model Previously
classes = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

model = tf.keras.models.load_model('model_SIBI.h5')
model.summary()

#Define the Input for the Inference
# Thumb Finger or Jari Jempol
thumb_fingerX = 0
thumb_fingerY = 0
# Index Finger or Jari Telunjuk
index_fingerX = 0
index_fingerY = 0
# Middle Finger or Jari Tengah
middle_fingerX = 0
middle_fingerY = 0
# Ring Finger or Jari Manis
ring_fingerX = 0
ring_fingerY = 0
# Pinky Finger or Jari Kelingking
pinky_fingerX = 0
pinky_fingerY = 0

while True:
    success, img = cap.read()
    results = hands.process(cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1))
    image_hight, image_width, _ = img.shape
    # print(results.multi_hand_landmarks)
    img = cv2.flip(img.copy(), 1)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Thumb Finger or Jari Jempol
            thumb_fingerX = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width
            thumb_fingerY = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_width
            # Index Finger or Jari Telunjuk
            index_fingerX = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
            index_fingerY = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_hight
            # Middle Finger or Jari Tengah
            middle_fingerX = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width
            middle_fingerY = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_width
            # Ring Finger or Jari Manis
            ring_fingerX = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width
            ring_fingerY = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_width
            # Pinky Finger or Jari Kelingking
            pinky_fingerX = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width
            pinky_fingerY = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_width
            # Print index finger tip coordinates.
            #print(
                #f'Index finger tip coordinate: (',
                #f'{index_fingerX}, '
                #f'{index_fingerY})')
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    
    input_IMG = [[[thumb_fingerX], [thumb_fingerY],
              [index_fingerX], [index_fingerY],
              [middle_fingerX], [middle_fingerY], 
              [ring_fingerX], [ring_fingerY], 
              [pinky_fingerX], [pinky_fingerY]]]
    IMG_array = np.array(input_IMG)
    IMG_array.shape
    predictions = model.predict_classes(IMG_array)
    for alphabets, values in classes.items():
        if values == predictions[0] :
            text_prediction = alphabets
    cv2.putText(img, str(text_prediction), (90, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()