from cv2 import cv2
import numpy as np

white = [255, 255, 255]
black = [0, 0, 0]


# TODO
def detect_black_stations(image):
    return False


def remove_all_non_black_pixels(image):
    non_black_pixels_mask = np.any(image != black, axis=-1)
    image[non_black_pixels_mask] = white
    return image


def remove_ui_clock(image):
    h, w = image.shape[:2]
    var = int(w / 6)
    triangle = np.array([[w - var, 0], [w, 0], [w, var]])
    return cv2.fillConvexPoly(image, triangle, white)


# TODO
def remove_passengers(image):
    return image


def morpho_open(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


def flood(image):
    image_flooded = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(image_flooded, mask, (0, 0), (0, 0, 0))
    return image_flooded


def process(image):
    is_stations_black = detect_black_stations(image)
    threshold = 40 if is_stations_black else 115

    _, image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    image = remove_all_non_black_pixels(image)
    image = remove_ui_clock(image)

    if is_stations_black:
        image = remove_passengers(image)
    else:
        image = flood(image)
        image = cv2.bitwise_not(image)

    return image


def read(file_path):
    return cv2.imread(file_path)


def read_and_process(file_path):
    image = read(file_path)
    return process(image)
