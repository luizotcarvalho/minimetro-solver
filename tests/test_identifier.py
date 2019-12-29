from services import identifier, reader

def _filter_by_type(type, array):
    return list(filter(lambda item : item['type'] == type, array))

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

def test_input_1():
    image = reader.read_and_process('tests/fixtures/1.jpg')
    stations = identifier.identify_countors(image)
    triangles = filter_triangles(stations)
    squares = filter_squares(stations)
    rhombus = filter_rhombuses(stations)
    pentagons = filter_pentagons(stations)
    droplets = filter_droplets(stations)
    circles = filter_circles(stations)
    stars = filter_stars(stations)
    crosses = filter_crosses(stations)

    assert len(triangles) == 9
    assert len(squares) == 1
    assert len(rhombus) == 1
    assert len(pentagons) == 1
    assert len(droplets) == 1
    assert len(circles) == 18
    assert len(stars) == 1
    assert len(crosses) == 1
    # total
    assert len(stations) == 33

def test_input_2():
    image = reader.read_and_process('tests/fixtures/2.jpg')
    stations = identifier.identify_countors(image)
    triangles = filter_triangles(stations)
    squares = filter_squares(stations)
    pentagons = filter_pentagons(stations)
    droplets = filter_droplets(stations)
    circles = filter_circles(stations)
    crosses = filter_crosses(stations)

    assert len(triangles) == 6
    assert len(squares) == 3
    assert len(pentagons) == 1
    assert len(droplets) == 1
    assert len(circles) == 12
    assert len(crosses) == 1
    # total
    assert len(stations) == 24

def test_input_3():
    image = reader.read_and_process('tests/fixtures/3.jpg')
    stations = identifier.identify_countors(image)
    triangles = filter_triangles(stations)
    squares = filter_squares(stations)
    circles = filter_circles(stations)

    assert len(triangles) == 5
    assert len(squares) == 2
    assert len(circles) == 6
    # total
    assert len(stations) == 13

def test_input_4():
    image = reader.read_and_process('tests/fixtures/4.jpg')
    stations = identifier.identify_countors(image)
    triangles = filter_triangles(stations)
    squares = filter_squares(stations)
    circles = filter_circles(stations)

    assert len(triangles) == 5
    assert len(squares) == 2
    assert len(circles) == 10
    # total
    assert len(stations) == 17

def test_input_5():
    image = reader.read_and_process('tests/fixtures/5.jpg')
    stations = identifier.identify_countors(image)
    triangles = filter_triangles(stations)
    squares = filter_squares(stations)
    droplets = filter_droplets(stations)
    circles = filter_circles(stations)
    crosses = filter_crosses(stations)

    assert len(triangles) == 4
    assert len(squares) == 2
    assert len(droplets) == 1
    assert len(circles) == 10
    assert len(crosses) == 1
    # total
    assert len(stations) == 18