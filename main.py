import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) + 6
    height = int(cap.get(4)) + 6

    image = np.zeros((height, width, 3), np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2 - 3, :width//2 - 3] = smaller_frame
    image[height//2 + 3:, :width//2 - 3] = smaller_frame
    image[:height//2 - 3, width//2 + 3:] = smaller_frame
    image[height//2 + 3:, width//2 + 3:] = smaller_frame

    line = cv2.line(image, (width//2, height), (width//2, 0), (255, 255, 255), 5)

    if not ret:
        break

    cv2.imshow("frame", image)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
