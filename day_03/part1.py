
def trace_wire(code, wire_set):
    position = (0, 0)
    for cmd in code.split(','):
        position = move(position, cmd, wire_set)


def move(position, cmd, wire_set):
    direction = cmd[0]
    distance = int(cmd[1:])

    if direction in ['U', 'D']:
        mod = 1 if direction == 'U' else -1
        y_vals = list(range(position[1], 
            position[1] + (mod * (distance + 1)),
            mod))
        positions = [(position[0], y_val) for y_val in y_vals]
    elif direction in ['R', 'L']:
        mod = 1 if direction == 'R' else -1
        x_vals = list(range(position[0], 
            position[0] + (mod * (distance + 1)),
            mod))
        positions = [(x_val, position[1]) for x_val in x_vals]
    else:
        raise Exception(f'Invalid command: {cmd}')

    wire_set.update(set(positions))
    return positions[-1]


def sorted_intersections(wire_set1, wire_set2):
    """Given two wire sets, return the intersections sorted by manhattan
    dist to the origin.
    """
    intersections = list(wire_set1.intersection(wire_set2))
    
    intersections.sort(key=manhattan_dist)
    return intersections

def manhattan_dist(point):
    return abs(point[0]) + abs(point[1])

def closest_intersection(code1, code2):
    wire_set1 = set()
    wire_set2 = set()

    trace_wire(code1, wire_set1)
    trace_wire(code2, wire_set2)

    intersections = sorted_intersections(wire_set1, wire_set2)
    return intersections[1]  # [0] is the origin
