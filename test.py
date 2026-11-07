from ultralytics import YOLO
import cv2

# Load ONNX model
model = YOLO("weights/best.onnx", task="detect")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not opening")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera frame not received")
        break

    # Detect currency notes
    results = model(frame, conf=0.50, verbose=False)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            # Class ID 2 = 50 Rupees
            if class_id == 2:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                label = f"Rs.50 {confidence:.2f}"

                cv2.rectangle(
                    frame, (x1, y1), (x2, y2),
                    (0, 255, 0), 2
                )

                cv2.putText(
                    frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2
                )

    cv2.imshow("50 Rupees Note Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()