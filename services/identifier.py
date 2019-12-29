import numpy as np
from cv2 import cv2


def get_type_by_edges(edges, tilted):
    if edges == 3:
        return 'triangle'
    elif edges == 4:
        if tilted:
            return 'rhombus'
        else:
            return 'square'
    elif edges == 5:
        # TODO: detect diamond
        return 'pentagon'
    elif edges == 6:
        return 'droplet'
    elif edges == 8:
        # TODO: detect footbal
        return 'circle'
    elif edges == 10:
        return 'star'
    elif edges == 12:
        return 'cross'
    else:
        return 'unknown'


def identify_countors(image):
    stations = []
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_invert = cv2.bitwise_not(image_gray)
    contours, _ = cv2.findContours(
        image_invert,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        M = cv2.moments(cnt)
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        x, y, w, h = cv2.boundingRect(cnt)

        # detect if the square is rotationed
        # TODO: detect in some other way
        tilted = cnt.ravel()[0] == cx

        station = {
            "type": get_type_by_edges(len(approx), tilted),
            "pos": (x, y),
            "centroid": (cx, cy),
            "size": (w, h),
            "contour": cnt
        }
        stations.append(station)

    return stations


def identify_interchange(stations):
    pass


def identify_rivers(image):
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 20, 38])
    upper_blue = np.array([110, 255, 255])
    rivers_mask = cv2.inRange(image_hsv, lower_blue, upper_blue)
    rivers_bgr = cv2.bitwise_and(image, image, mask=rivers_mask)
    rivers_gray = cv2.cvtColor(rivers_bgr, cv2.COLOR_BGR2GRAY)
    _, rivers_alpha = cv2.threshold(rivers_gray, 0, 255, cv2.THRESH_BINARY)
    rivers_b, rivers_g, rivers_r = cv2.split(rivers_bgr)
    rivers_bgra = [rivers_b, rivers_g, rivers_r, rivers_alpha]
    return cv2.merge(rivers_bgra, 4)
