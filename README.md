# Tap The Balls - Auto Bot

Automated bot for playing "Tap The Balls" using YOLO-based object detection.

Original Game: https://scratch.mit.edu/projects/1213053712

## Features

- YOLO v8 object detection for precise ball recognition
- Automatic clicking system
- Optimized for real-time gameplay

## Requirements

```bash
pip install ultralytics pyautogui pillow keyboard numpy
```

## Usage

```bash
python bot.py
```

Controls:
- Q - Exit bot

## Model

The trained model is located at:
```
runs/detect/train7/weights/best.pt
```

## Game Area

Default resolution: 1920x1440
- X: 431-2173
- Y: 124-1427

Adjust via `X_START`, `Y_START`, `X_END`, `Y_END` in `bot.py` if needed.
