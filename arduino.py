import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

fingerUpRecords = {
    "Gibson": [1, 1, 0, 0, 1],
    "Darwin": [0, 1, 1, 0, 0],
    "Leena": [1, 1, 0, 0, 0],
    "Diana": [1, 1, 1, 1, 1],
}

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        for name, record in fingerUpRecords.items():
            if fingerUp == record:
                print(f"Match found for {name}: {record}")
                cnt.led(record)  
                cv2.putText(frame, 'Finger count:2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            elif fingerUp == [0,1,0,0,0]:
                print("Door closed")
                cv2.putText(frame, 'Finger count:0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            else:
                print("No match found")
                cv2.putText(frame, 'Finger count:0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()
