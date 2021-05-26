import cv2
from djitellopy import tello

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (720,360))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

me.takeoff()
me.send_rc_control(0,0,0,0)
sleep(2)
me.send_rc_control(0,30,0,0)
sleep(2)

me.land()