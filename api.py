import cv2

def detect_face(img, mtcnn):
    try:
        bboxs, scores = mtcnn.detect(img)
        print('Detected',len(scores),'faces')
        for num ,(bbox, score) in enumerate(zip(bboxs, scores)):
            b = [int(bb) for bb in bbox]
            face = img[b[1]:b[3],b[0]:b[2]]
            cv2.imshow('face_'+str(num), face)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    except:
        print('Can\'t detect face')

