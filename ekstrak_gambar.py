import cv2

cap = cv2.VideoCapture("Data_Training_Frame.mp4")
count = 0

while True:
    _, frame = cap.read()
    resized = cv2.resize(frame, (569, 320), interpolation=cv2.INTER_AREA)
    count += 1
    cv2.imwrite("Data/bola/frame"+str(count)+".jpg", frame)
    cv2.imshow("Frame", resized)
    if cv2.waitKey(1) and 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
