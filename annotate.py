import numpy as np
import os
import cv2


def image_read(path):
    """
    画像を読み込む

    parametors
    ___________
    path: string
        画像のパス
    ___________
    """

    image_list = os.listdir(path)
    for i in range(len(image_list)):
        filepath = os.path.join(path, image_list[i])
        image = cv2.imread(filepath)
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    image_path_OK = '../../Pictures/solar_trim/OK'
    image_path_NG = '../../Pictures/solar_trim/NG'
    image_read(image_path_OK)
