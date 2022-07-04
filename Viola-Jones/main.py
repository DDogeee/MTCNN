import cv2 as cv
import time
# Read image from your local file system
# original_image = cv.imread('C:\\Users\\GS75\\PycharmProjects\\open_cv_MTCNN\\MTCNN\\image_example\\img_3.jpg')
original_image = cv.imread('C:\\Users\\GS75\\Desktop\\3.jpg')
# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

# Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier('C:\\Users\\GS75\\PycharmProjects\\open_cv_MTCNN\\python-opencv-detect\\haarcascade_frontalface_alt.xml')
start = time.time()
detected_faces = face_cascade.detectMultiScale(grayscale_image)
end = time.time()
print("Viola-Jones time: ", end-start)
print(len(detected_faces))
for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )
img = cv.resize(original_image, (800, 600))
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()