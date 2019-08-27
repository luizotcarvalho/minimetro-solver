from cv2 import cv2
from tabulate import tabulate

def resize_image(image, scale):
    new_width = int(image.shape[1] * scale)
    new_height = int(image.shape[0] * scale)
    return cv2.resize(image, (new_width, new_height))

def format_to_tabulate(items, hide_columns):
    first = items[0]
    keys = list(first.keys())
    values = []
        
    for index, item in enumerate(items):
        value = [index]
        for key in keys:
            if key not in hide_columns:
                value.append(item[key])
        values.append(value)
    
    keys.insert(0, 'index')

    return {
        'keys': keys,
        'values': values
    }

def print_table(items, title='Title', hide_columns=[]):
    if(len(items) == 0):
        return
    formated = format_to_tabulate(items, hide_columns);
    print()
    print(title)
    print()
    print(tabulate(formated['values'], headers=formated['keys'], tablefmt="github"))