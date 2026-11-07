
from ultralytics import YOLO
import cv2

model = YOLO("best.pt")
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera not detected")
        break

    results = model(frame)

    output = results[0].plot()

    cv2.imshow("Indian Currency Detection", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
