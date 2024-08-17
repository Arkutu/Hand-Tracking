import cv2
import mediapipe as mp
import numpy as np
import pygame
import os

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize Pygame for audio
pygame.init()
pygame.mixer.init()

# Define piano keys and their corresponding filenames
KEY_FILES = {
    'C': 'do-80236.mp3',
    'D': 'd6-82020.mp3',
    'E': 'e6-82016.mp3',
    'F': 'f6-102819.mp3',
    'G': 'g6-82013.mp3',
    'A': 'si-80238.mp3',  # Note: 'A' is typically 'la' in solfege, but using 'si' as per your files
    'B': 'b6-82017.mp3'
}

# Load sound files
KEY_SOUNDS = {}
for key, filename in KEY_FILES.items():
    file_path = os.path.join('sound', filename)  # Assuming 'sound' is the directory name
    if os.path.exists(file_path):
        KEY_SOUNDS[key] = pygame.mixer.Sound(file_path)
    else:
        print(f"Warning: {file_path} not found.")

# Define key rectangles
key_width = 90
key_height = 200
key_rects = [pygame.Rect(i * key_width, 0, key_width, key_height) for i in range(len(KEY_FILES))]

# Tracking variables
last_key_pressed = None
key_press_cooldown = 0

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)

    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and find hands
    results = hands.process(rgb_image)

    # Draw piano keys
    for i, (key, rect) in enumerate(zip(KEY_FILES.keys(), key_rects)):
        cv2.rectangle(image, (rect.x, rect.y), (rect.x + rect.width, rect.y + rect.height), (255, 255, 255), 2)
        cv2.putText(image, key, (rect.x + 35, rect.y + 280), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index finger tip coordinates
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * image.shape[1]), int(index_finger_tip.y * image.shape[0])

            # Check if index finger is on a key
            for i, (key, rect) in enumerate(zip(KEY_FILES.keys(), key_rects)):
                if rect.collidepoint(x, y):
                    if last_key_pressed != key and key_press_cooldown == 0:
                        KEY_SOUNDS[key].play()
                        last_key_pressed = key
                        key_press_cooldown = 10  # Set cooldown to prevent rapid repeats
                    cv2.rectangle(image, (rect.x, rect.y), (rect.x + rect.width, rect.y + rect.height), (0, 255, 0), -1)
                    break
            else:
                last_key_pressed = None

            # Draw a circle at the index finger tip
            cv2.circle(image, (x, y), 10, (0, 255, 0), -1)

    # Decrease cooldown
    if key_press_cooldown > 0:
        key_press_cooldown -= 1

    cv2.imshow('Virtual Piano', image)
    if cv2.waitKey(5) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()