import cv2
import cv2.aruco as aruco


def findaruco(img, markerSize = 6, totalMarkers=50, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(aruco.DICT_6X6_50)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters = arucoParam)
    print(ids)
    print(bboxs)

def main():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (640,480))

    while(True):
        ret, img = cap.read()
        if ret == False:
            continue
        cv2.imshow('test', img)
        writer.write(img)
        findaruco(img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()