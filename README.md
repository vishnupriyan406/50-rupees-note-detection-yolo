# Indian Currency Note Detection using YOLO11

## Project Overview
This project uses YOLO11 to detect Indian currency notes in real time through a webcam.

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
- PyTorch

## Features
- Real-time currency detection.
- Webcam-based detection.
- Custom-trained YOLO11 model.

## Model Performance
- Validation Precision: 97.2%
- Validation Recall: 97.7%
- Validation mAP50: 99.5%
- Validation mAP50-95: 91%

*Note: Metrics are based on a small validation dataset and do not guarantee real-world accuracy.*

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python webcam.py
```

Make sure your webcam is connected.

Press `q` to close the webcam window.

## Project Files
- `webcam.py` – Webcam detection code.
- `best.pt` – Trained YOLO11 model.
- `data.yaml` – Dataset configuration.
- `requirements.txt` – Required Python libraries.

## Dataset
The training dataset is not included in this repository.

## Author
**Vishnu Priyan K**
