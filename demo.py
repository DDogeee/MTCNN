from modules.mtcnn import MTCNN
import cv2
import warnings

from api import detect_face
warnings.filterwarnings("ignore")

import argparse


if __name__ == '__main__':
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('--device', type=str, help='example cpu, cuda:0, cuda:1,...', default='cpu')
    parser_.add_argument('--path', type=str, help='path to image directory',default='image_example/img_1.jpg')
    mtcnn = MTCNN()
    opt = parser_.parse_args()
    img = cv2.imread(opt.path)
<<<<<<< HEAD
    detect_face(img, mtcnn)
=======
    detect_face(img, mtcnn)
>>>>>>> 1bcff4621591fc421a52663e2fac1ee7aa1c264e
