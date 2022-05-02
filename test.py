import cv2
import numpy as np
import torch


model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')

cap = cv2.VideoCapture('Data_Training_Frame.mp4')
# cap = cv2.VideoCapture('a.jpg')
while True:
    _, frame = cap.read()
    results = frame
    # results = cv2.resize(frame, (569, 320), interpolation=cv2.INTER_AREA)
    results = model(results)
    cv2.imshow("Yolo", np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
