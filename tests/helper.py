def _filter_by_type(type, array):
    return list(filter(lambda item: item['type'] == type, array))


def filter_triangles(stations):
    return _filter_by_type('triangle', stations)


def filter_squares(stations):
    return _filter_by_type('square', stations)


def filter_rhombuses(stations):
    return _filter_by_type('rhombus', stations)


def filter_pentagons(stations):
    return _filter_by_type('pentagon', stations)


def filter_droplets(stations):
    return _filter_by_type('droplet', stations)


def filter_circles(stations):
    return _filter_by_type('circle', stations)


def filter_stars(stations):
    return _filter_by_type('star', stations)


def filter_crosses(stations):
    return _filter_by_type('cross', stations)
