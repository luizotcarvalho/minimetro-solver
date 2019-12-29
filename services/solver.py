import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def calculate_distances(stations):
    all_distances = []

    for from_station in stations:
        distances = []

        for to_station in stations:
            x = to_station['centroid'][0] - from_station['centroid'][0]
            y = to_station['centroid'][1] - from_station['centroid'][1]
            distance = int(math.sqrt(math.pow(x) + math.pow(y)))
            distances.append(distance)

        all_distances.append(distances)

    return all_distances


def format_solution(data, manager, routing, solution):
    formated_solutions = []

    for vehicle_index in range(data['num_vehicles']):
        index = routing.Start(vehicle_index)
        formated_solution = {
            'vehicle_index': vehicle_index,
            'route': []
        }

        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            formated_solution['route'].append(node_index)
            index = solution.Value(routing.NextVar(index))

        formated_solutions.append(formated_solution)

    return formated_solutions


def solve(stations, rivers):
    data = {}
    data['distance_matrix'] = calculate_distances(stations)
    data['num_vehicles'] = 4
    data['depot'] = 0

    manager = pywrapcp.RoutingIndexManager(
        len(data['distance_matrix']),
        data['num_vehicles'],
        data['depot']
    )
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    distance_dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        distance_dimension_name)
    distance_dimension = routing.GetDimensionOrDie(distance_dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # def type_callback(from_index, to_index):
    #     from_node = manager.IndexToNode(from_index)
    #     to_node = manager.IndexToNode(to_index)
    #     from_station = stations[from_node]
    #     to_station = stations[to_node]

    #     if from_station['type'] == to_station['type']:
    #         return 100
    #     else:
    #         return 0

    # type_callback_index = routing.RegisterTransitCallback(type_callback)

    # routing.SetArcCostEvaluatorOfAllVehicles(type_callback_index)

    # # Station type dimension
    # type_dimension_name = 'Type'
    # routing.AddDimension(
    #     type_callback_index,
    #     0,
    #     3000,
    #     True,
    #     type_dimension_name)
    # type_dimension = routing.GetDimensionOrDie(type_dimension_name)
    # type_dimension.SetGlobalSpanCostCoefficient(200)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        return format_solution(data, manager, routing, solution)
    else:
        return []
