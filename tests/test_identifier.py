from services import identifier, reader
import tests.helper as helper


def test_input_1():
    image = reader.read_and_process('tests/fixtures/1.jpg')
    stations = identifier.identify_countors(image)
    triangles = helper.filter_triangles(stations)
    circles = helper.filter_circles(stations)
    squares = helper.filter_squares(stations)
    rhombus = helper.filter_rhombuses(stations)
    pentagons = helper.filter_pentagons(stations)
    droplets = helper.filter_droplets(stations)
    stars = helper.filter_stars(stations)
    crosses = helper.filter_crosses(stations)

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
    triangles = helper.filter_triangles(stations)
    squares = helper.filter_squares(stations)
    pentagons = helper.filter_pentagons(stations)
    droplets = helper.filter_droplets(stations)
    circles = helper.filter_circles(stations)
    crosses = helper.filter_crosses(stations)

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
    triangles = helper.filter_triangles(stations)
    squares = helper.filter_squares(stations)
    circles = helper.filter_circles(stations)

    assert len(triangles) == 5
    assert len(squares) == 2
    assert len(circles) == 6
    # total
    assert len(stations) == 13


def test_input_4():
    image = reader.read_and_process('tests/fixtures/4.jpg')
    stations = identifier.identify_countors(image)
    triangles = helper.filter_triangles(stations)
    squares = helper.filter_squares(stations)
    circles = helper.filter_circles(stations)

    assert len(triangles) == 5
    assert len(squares) == 2
    assert len(circles) == 10
    # total
    assert len(stations) == 17


def test_input_5():
    image = reader.read_and_process('tests/fixtures/5.jpg')
    stations = identifier.identify_countors(image)
    triangles = helper.filter_triangles(stations)
    squares = helper.filter_squares(stations)
    droplets = helper.filter_droplets(stations)
    circles = helper.filter_circles(stations)
    crosses = helper.filter_crosses(stations)

    assert len(triangles) == 4
    assert len(squares) == 2
    assert len(droplets) == 1
    assert len(circles) == 10
    assert len(crosses) == 1
    # total
    assert len(stations) == 18
