import sys
import cv2
from os import walk

BASE_PICTURE_PATH = './pictures/'


def main(argv):
    images = read_images_repository(BASE_PICTURE_PATH)
    for i in range(0, images.__len__()):
        show_image(BASE_PICTURE_PATH + images[i])


def show_image(path):
    image = cv2.imread(path)
    cv2.imshow("Picture", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def read_images_repository(path):
    images = []
    for (dirpath, dirnames, filenames) in walk(path):
        images.extend(filenames)
    return images


if __name__ == "__main__":
    main(sys.argv)
