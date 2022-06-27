import cv2

def detect_face(img, mtcnn):
    try:
        bboxs, scores = mtcnn.detect(img)
        print('Detected',len(scores),'faces')
        for num ,(bbox, score) in enumerate(zip(bboxs, scores)):
            b = [int(bb) for bb in bbox]
            # face = img[b[1]:b[3],b[0]:b[2]]
            point1 =(b[0],b[1])
            point2 = (b[0], b[3])
            point3 = (b[2],b[3])
            point4 = (b[2],b[1])
            cv2.line(img, point1, point2, (255,255,0), 3)
            cv2.line(img, point3, point2, (255, 255, 0), 3)
            cv2.line(img, point3, point4, (255,255,0), 3)
            cv2.line(img, point4, point1, (255,255,0), 3)

        cv2.imshow('face_'+str(num), img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print('Can\'t detect face')
