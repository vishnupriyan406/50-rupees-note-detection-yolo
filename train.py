from ultralytics import YOLO

# Load YOLO11 model
model = YOLO("yolo11n.pt")

# Train the model
model.train(
    data="dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=8
)

print("Training completed!")