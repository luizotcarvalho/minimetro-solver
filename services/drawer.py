# drawing configs
import math
import numpy as np
from cv2 import cv2

def draw_shape(image, contour):
    border_color = (71, 54, 51)
    thickness = 3
    cv2.polylines(image, contour, True, border_color, thickness)

def draw_path(image, route, index, stations):
    paths_color = [
        (10, 164, 62), #green
        (235, 23, 23), #red
        (8, 117, 191), #blue
        (254, 205, 0) #yellow
    ] 
    route_color = paths_color[index]

    if len(route['route']) > 1:
        for point_index, station_index in enumerate(route['route'][:-1]):
            station = stations[station_index]
            next_station_index = route['route'][point_index + 1]
            next_station = stations[next_station_index]
            pt1 = (station['centroid'][0], station['centroid'][1])
            pt2 = (next_station['centroid'][0], next_station['centroid'][1])
            cv2.arrowedLine(image, pt1, pt2, route_color, 3)

def draw_results(image, stations, rivers, routes):
    height, width = image.shape[:2]
    blank_image = 255 * np.ones(shape=[height, width, 3], dtype=np.uint8)
    output = blank_image

    # draw rivers
    #     rivers_rgb = cv2.cvtColor(rivers, cv2.COLOR_BGR2RGB)
    #     output_rgb = cv2.cvtColor(output_bgr, cv2.COLOR_BGR2RGB)
    #     output_combined = cv2.addWeighted(output_rgb,.1,rivers_rgb,1,0)

    # draw paths        
    for path_index, route in enumerate(routes):
        draw_path(output, route, path_index, stations)
    
    # draw stations
    for station in stations:
        draw_shape(output, station['contour'])

    return cv2.cvtColor(output, cv2.COLOR_BGR2RGB)