import sys
import cv2
from os import walk

PICTURE_BASE_PATH = './pictures/'
PICTURE_TITLE = 'Picture'
MAX_WIDTH = 1280
MAX_HEIGHT = 720


def main(argv):
    images = read_images_repository(PICTURE_BASE_PATH)
    while True:
        for i in range(0, images.__len__()):
            show_image(PICTURE_BASE_PATH + images[i])


def show_image(path):
    cv2.namedWindow(PICTURE_TITLE, cv2.WINDOW_NORMAL)
    image = cv2.imread(path)
    image_resized = cv2.resize(image, (MAX_WIDTH, MAX_HEIGHT))
    image_resized = cv2.copyMakeBorder(image_resized, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[20, 250, 150])
    cv2.imshow(PICTURE_TITLE, image_resized)
    cv2.resizeWindow(PICTURE_TITLE, MAX_WIDTH, MAX_HEIGHT)
    cv2.waitKey()
    cv2.destroyAllWindows()


def read_images_repository(path):
    images = []
    for (dirpath, dirnames, filenames) in walk(path):
        images.extend(filenames)
    return images


if __name__ == "__main__":
    main(sys.argv)
