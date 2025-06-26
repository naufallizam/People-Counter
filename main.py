import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import*
import cvzone


model=YOLO('yolov8s.pt')



def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
  
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap=cv2.VideoCapture('vidp.mp4')


my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

count=0
tracker=Tracker()
counter1 = []
counter2 = []
previous_positions = {}

cy1 = 194
offset = 6

while True:
    ret, frame = cap.read()
    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (1020, 500))

    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    list = []

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])

        c = class_list[d]
        if 'person' in c:
            list.append([x1, y1, x2, y2])

    bbox_id = tracker.update(list)

    for bbox in bbox_id:
        x3, y3, x4, y4, id = bbox
        cx = int(x3 + x4) // 2
        cy = int(y3 + y4) // 2

        # Draw point for every person
        cv2.circle(frame, (cx, cy), 4, (255, 0, 255), -1)

        # Draw bounding box and ID only if near the line
        if cy1 - offset <= cy <= cy1 + offset:
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)
            cvzone.putTextRect(frame, f'{id}', (x3, y3), 1, 2)

        # Check if the person crossed the line
        if id in previous_positions:
            prev_cy = previous_positions[id]
            # Crossing from above to below the line (down)
            if prev_cy < cy1 <= cy:
                if id not in counter1:
                    counter1.append(id)
            # Crossing from below to above the line (up)
            elif prev_cy > cy1 >= cy:
                if id not in counter2:
                    counter2.append(id)

        previous_positions[id] = cy

    # Draw the counting line
    cv2.line(frame, (3, cy1), (1018, cy1), (0, 255, 0), 2)

    down = len(counter1)
    up = len(counter2)
    cvzone.putTextRect(frame, f"Down {down}", (50, 60), 2, 2)
    cvzone.putTextRect(frame, f"Up {up}", (50, 30), 2, 2)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
