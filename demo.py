from modules.mtcnn import MTCNN
import cv2
import warnings
warnings.filterwarnings("ignore")

import argparse



def detect_face(img):
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



if __name__ == '__main__':
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('--device', type=str, help='example cpu, cuda:0, cuda:1,...', default='cpu')
    parser_.add_argument('--path', type=str, help='path to image directory',default='image_example/img_1.jpg')
    mtcnn = MTCNN()
    opt = parser_.parse_args()
    img = cv2.imread(opt.path)
    detect_face(img)
