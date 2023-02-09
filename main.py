import cv2

video = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fps = video.get(5)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps, width, height)
out = cv2.VideoWriter(r"test.avi", fourcc, fps, (width, height))
i = 1
while True:
    fps = video.get(5)
    state, frame = video.read()
    cv2.imshow("test", frame)
    out.write(frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()
out.release()
cv2.destroyAllWindows()