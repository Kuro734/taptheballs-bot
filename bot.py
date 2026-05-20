import pyautogui
from PIL import ImageGrab
import keyboard
import time
import sys
from ultralytics import YOLO
import numpy as np

# -----------------------------------
# LOAD YOLO MODEL
# -----------------------------------
print("Loading YOLO model...")
model = YOLO(r"runs\detect\train7\weights\best.pt")

# -----------------------------------
# GAME AREA
# -----------------------------------
X_START = 431
Y_START = 124
X_END = 2173
Y_END = 1427

print("=== RED BALL AUTO BOT ===")
print("Q = Quit")
print("--------------------------------")

# -----------------------------------
# ENTER FULLSCREEN
# -----------------------------------
print("Entering fullscreen...")
time.sleep(1)

pyautogui.moveTo(1296, 235, duration=0)
pyautogui.click()

# -----------------------------------
# START GAME
# -----------------------------------
print("Starting game...")
time.sleep(1)

pyautogui.moveTo(1309, 759, duration=0)
pyautogui.click()

print("Bot is running.")

# -----------------------------------
# MAIN LOOP
# -----------------------------------
while True:

    # Quit program
    if keyboard.is_pressed('q'):
        print("Program closed.")
        sys.exit()

    # Take screenshot of game area
    screenshot = ImageGrab.grab(
        bbox=(X_START, Y_START, X_END, Y_END)
    )

    # Convert to numpy array for YOLO
    frame = np.array(screenshot)

    # Run YOLO detection
    results = model(frame)

    # -----------------------------------
    # PROCESS DETECTIONS
    # -----------------------------------
    if results[0].boxes:
        # Get first detection (highest confidence)
        boxes = results[0].boxes
        
        # Sort by confidence (descending)
        confidences = boxes.conf
        best_idx = int(confidences.argmax())
        
        box = boxes[best_idx]
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        # Calculate center of bounding box
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        
        # Convert to screen coordinates
        real_x = X_START + center_x
        real_y = Y_START + center_y
        
        # Click on detected ball
        pyautogui.moveTo(real_x, real_y, duration=0.05)
        pyautogui.click()
        
        confidence = float(box.conf[0])
        print(f"Ball detected at X={real_x}, Y={real_y} (confidence: {confidence:.2f})")

    # Original safer delay
    time.sleep(0.3)