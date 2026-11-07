# Indian Currency Note Detection using YOLO11

## Project Overview
This project uses a custom-trained YOLO11 model to detect Indian currency notes in real time using a webcam.

## Supported Currency Notes
- ₹10
- ₹20
- ₹50
- ₹100
- ₹200
- ₹500

## Technologies Used
- Python
- YOLO11
- OpenCV
- Ultralytics
- ONNX

## Features
- Real-time currency note detection.
- Webcam-based detection.
- Detects six Indian currency denominations.
- Displays bounding boxes and confidence scores.
- ONNX model for inference.

## Model Performance
- Precision: 97.2%
- Recall: 97.7%
- mAP50: 99.5%
- mAP50-95: 91%

*Note: These metrics are based on a small validation dataset and do not guarantee real-world accuracy.*

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Run

Download `best.onnx` from the v1.0 Release and place it inside the `weights` folder.

Run:

```bash
python test.py
```

Make sure your webcam is connected. Press `q` to close the webcam window.

## Training

Training code is available in `train.py`.

The training dataset is available as `dataset.zip` in the v1.0 Release.

## Project Files
- `test.py` – Webcam currency detection.
- `train.py` – YOLO11 model training.
- `requirements.txt` – Required Python packages.
- `weights/best.onnx` – Trained ONNX model (download from Release).
- `dataset.zip` – Training dataset (download from Release).

## Release
Download the model and dataset from the [v1.0 Release](../../releases/tag/v1.0).

## Author
Vishnu Priyan K
