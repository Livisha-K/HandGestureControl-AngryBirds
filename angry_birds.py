import cv2 as cv
from mediapipe import solutions
import pyautogui
import math

pyautogui.FAILSAFE = False  # Disable PyAutoGUI fail-safe

cap = cv.VideoCapture(0)
hand = solutions.hands
hands = solutions.hands.Hands()
draw = solutions.drawing_utils

pinch_position = []
direction = [0, 0]
slope = 8

def moveCursor():
    try:
        X = pyautogui.position().x
        Y = pyautogui.position().y
        new_x = X + direction[0] * 8
        new_y = Y + direction[1] * slope * (-X + new_x)
        pyautogui.moveTo(new_x, new_y)
    except:
        pass

def changeDirections(pinch_position, curr_pos):
    global slope
    if curr_pos[0] > pinch_position[0]:
        direction[0] = -1
    elif curr_pos[0] == pinch_position[0]:
        direction[0] = 0
    else:
        direction[0] = 1
    
    if curr_pos[1] > pinch_position[1]:
        direction[1] = -1
    elif curr_pos[1] == pinch_position[1]:
        direction[1] = 0
    else:
        direction[1] = 1
    if pinch_position[0] != curr_pos[0]:
        slope = (curr_pos[1] - pinch_position[1]) / (curr_pos[0] - pinch_position[0])

def currPos(landmarks):
    (h, w, c) = video.shape
    thumb = []
    index = []
    for ind, lm in enumerate(landmarks.landmark):
        if ind == 8:
            index = (lm.x * w, lm.y * h)
        if ind == 4:
            thumb = (lm.x * w, lm.y * h)
    if len(index) == 2 and len(thumb) == 2:
        return ((thumb[0] + index[0]) / 2, (thumb[1] + index[1]) / 2)
    return []

def pinch(landmarks):
    global pinch_position
    (h, w, c) = video.shape
    thumb = []
    index = []
    for ind, lm in enumerate(landmarks.landmark):
        if ind == 8:
            index = (lm.x * w, lm.y * h)
        if ind == 4:
            thumb = (lm.x * w, lm.y * h)
    if len(index) == 2 and len(thumb) == 2:
        distance = math.dist(index, thumb)
        if distance <= 50:
            if not pinch_position:
                pinch_position = ((thumb[0] + index[0]) / 2, (thumb[1] + index[1]) / 2)
            return True
        else:
            return False
    else:
        return False

while True:
    success, video = cap.read()
    result = hands.process(video)
    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            draw.draw_landmarks(video, landmarks, hand.HAND_CONNECTIONS)
            if pinch(landmarks):
                pyautogui.mouseDown()
                curr_pos = currPos(landmarks)
                changeDirections(pinch_position, curr_pos)
                moveCursor()
            else:
                pyautogui.mouseUp()
                pinch_position = []
                direction = [0, 0]
    cv.imshow('Output', video)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()