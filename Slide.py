import sys
from os import walk

BASE_PICTURE_PATH = './pictures/'


def main(argv):
    images = read_images_repository(BASE_PICTURE_PATH)
    print(images.__str__())


def read_images_repository(path):
    images = []
    for (dirpath, dirnames, filenames) in walk(path):
        images.extend(filenames)
    return images


if __name__ == "__main__":
    main(sys.argv)
