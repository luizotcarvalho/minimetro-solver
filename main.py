from services import reader, identifier, solver, drawer, utils
from cv2 import cv2
import sys
import os

file_path = sys.argv[1]
image = reader.read(file_path)
proc_image = reader.process_image(image)

# detect stations
stations = identifier.identify_countors(proc_image)
utils.print_table(stations, title='Stations', hide_columns=['contour'])

# detect rivers
rivers = identifier.identify_rivers(image)

# optimize routes
routes = solver.solve(stations, rivers)
utils.print_table(routes, title='Routes')

# draw
results = drawer.draw_results(proc_image, stations, rivers, routes)

file_name = os.path.basename(file_path)
cv2.imwrite('output/%s' % file_name, results)
print()
print('Results saved in output/%s' % file_name)