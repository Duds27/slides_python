import sys
import cv2
import time
from os import walk

PICTURE_BASE_PATH = './pictures/'
PICTURE_TITLE = 'Picture'
MAX_WIDTH = 1280
MAX_HEIGHT = 720


def main(argv):
    images = read_images_repository(PICTURE_BASE_PATH)
    stop = False
    while True:
        if stop:
            break
        for i in range(0, images.__len__() - 1):
            print("Picture {} - {}".format(i.__str__(), images[i]))
            if i == images.__len__() - 1:
                if show_image(PICTURE_BASE_PATH + images[images.__len__() - 1], PICTURE_BASE_PATH + images[0]):
                    stop = True
                    break
            else:
                if show_image(PICTURE_BASE_PATH + images[i], PICTURE_BASE_PATH + images[i + 1]):
                    stop = True
                    break
    cv2.destroyAllWindows()


def show_image(path_image_1, path_image_2):
    cv2.namedWindow(PICTURE_TITLE, cv2.WINDOW_NORMAL)
    image_1 = cv2.imread(path_image_1)
    image_resized_1 = cv2.resize(image_1, (MAX_WIDTH, MAX_HEIGHT))
    image_resized_1 = cv2.copyMakeBorder(image_resized_1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[20, 250, 150])
    image_2 = cv2.imread(path_image_2)
    image_resized_2 = cv2.resize(image_2, (MAX_WIDTH, MAX_HEIGHT))
    image_resized_2 = cv2.copyMakeBorder(image_resized_2, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[20, 250, 150])
    # cv2.imshow(PICTURE_TITLE, image_resized_1)
    return blending_fade(image_resized_1, image_resized_2)


def stop_program():
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True
    return False


def blending_fade(first_image, second_image):
    for i in range(1, 42):
        fadein = i / 42.0
        dst = cv2.addWeighted(first_image, 1 - fadein, second_image, fadein, 0)
        cv2.imshow(PICTURE_TITLE, dst)
        if stop_program():
            return True
        # print(fadein)
        time.sleep(0.05)
        cv2.resizeWindow(PICTURE_TITLE, MAX_WIDTH, MAX_HEIGHT)
    return False


def read_images_repository(path):
    images = []
    for (dirpath, dirnames, filenames) in walk(path):
        images.extend(filenames)
    return images


if __name__ == "__main__":
    main(sys.argv)
