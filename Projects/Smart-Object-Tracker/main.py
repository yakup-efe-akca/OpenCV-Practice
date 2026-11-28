import cv2
import numpy as np

screenshot_count = 1
live = cv2.VideoCapture(0)

colors = {
    "Green": ([35, 50, 50], [85, 255, 255]),
    "Blue": ([100, 100, 50], [130, 255, 255]),
    "Yellow": ([20, 100, 100], [35, 255, 255])
}
bgr_colors = {
    "Green": (0, 255, 0),
    "Blue": (255, 0, 0),
    "Yellow": (0, 255, 255)
}
trails = {
    "Green": [],
    "Blue": [],
    "Yellow": []
}

while True:
    ret, frame = live.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1280, 720))
    
    
    live_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for name, (lower, upper) in colors.items():
        
        lowerLimit = np.array(lower)
        upperLimit = np.array(upper)

        mask = cv2.inRange(live_hsv, lowerLimit, upperLimit)
        
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), bgr_colors[name], 4)

                perimeter = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
                vertices = len(approx)
                if vertices == 3:
                    shape = 'Triangle'
                elif vertices == 4:
                    if 0.9 <= w/h <= 1.1:
                        shape = 'Square'
                    else:
                        shape = 'Rectangle'
                elif vertices > 6:
                    shape = 'Circle'
                else:
                    shape = 'Unknown'
                    
                label = name + " " + shape
                cv2.putText(
                    frame, 
                    label, 
                    (x, max(20, y - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
                    bgr_colors[name], 2)

                center_x = x + w//2
                center_y = y + h//2
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
                
                text_y = y + h + 20
                if text_y >= frame.shape[0] - 10:
                    text_y = max(20, y - 10)
                    
                cv2.putText(
                    frame, 
                    f"({center_x}, {center_y})", 
                    (x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
                    (255, 255, 255), 2)
    
                if trails[name]:
                    prev_x, prev_y = trails[name][-1]
                    distance = ((center_x - prev_x)**2 +
                                (center_y - prev_y)**2)**0.5
                    if distance > 100:
                        trails[name].clear()
                        
                trails[name].append((center_x, center_y))
                if len(trails[name]) > 30:
                    trails[name].pop(0)

                for i in range(1, len(trails[name])):
                    previous = trails[name][i - 1]
                    current = trails[name][i]
                    cv2.line(frame, previous, current, bgr_colors[name], 3)
    
    
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        cv2.imwrite(f"Screenshot_{screenshot_count}.png", frame)
        screenshot_count += 1
    elif key == ord("q"):
        break



live.release()
cv2.destroyAllWindows()