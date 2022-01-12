import copy

energies = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

room_nums = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3
}

initial_state = '.......CDDDCCBDABABBACA'

print(initial_state)


def all_free(hall, hall_ind, room_num):
    if hall_ind < room_num + 2:
        return all([hall[i]=='.' for i in range(hall_ind+1, room_num + 2)])
    else:
        return all([hall[i]=='.' for i in range(room_num + 2,hall_ind)])


def parse_state_str(state):
    hall = state[0:7]
    rooms = [state[7:11], state[11:15], state[15:19], state[19:]]
    return hall, rooms


def make_state_str(hall, rooms):
    room_str = rooms[0] + rooms[1] + rooms[2] + rooms[3]
    return hall + room_str


def find_next_states(state, energy, path):
    next_states = []
    hall, rooms = parse_state_str(state)

    for hall_num, amp in enumerate(hall):
        if amp == '.':
            continue
        if all_free(hall, hall_num, room_nums[amp]):
            if rooms[room_nums[amp]] == '....':
                new_hall = hall[:hall_num] + '.' + hall[hall_num + 1:]
                new_rooms = copy.deepcopy(rooms)
                new_rooms[room_nums[amp]] = '...' + amp
                if hall_num < room_nums[amp] + 2:
                    distance = (room_nums[amp] + 1 - hall_num) * 2 + 5 - (
                            hall_num==0)
                else:
                    distance = (hall_num - room_nums[amp] - 2) * 2 + 5 - (
                            hall_num == 6)
                next_states.append(
                    [
                        make_state_str(new_hall, new_rooms),
                        energy + distance * energies[amp],
                        path + [state],
                    ]
                )
            elif rooms[room_nums[amp]] == '...' + amp:
                new_hall = hall[:hall_num] + '.' + hall[hall_num + 1:]
                new_rooms = copy.deepcopy(rooms)
                new_rooms[room_nums[amp]] = '..' + amp + amp
                if hall_num < room_nums[amp] + 2:
                    distance = (room_nums[amp] + 1 - hall_num) * 2 + 4 - (
                            hall_num == 0)
                else:
                    distance = (hall_num - room_nums[amp] - 2) * 2 + 4 - (
                            hall_num == 6)
                next_states.append(
                    [
                        make_state_str(new_hall, new_rooms),
                        energy + distance * energies[amp],
                        path + [state],
                    ]
                )
            elif rooms[room_nums[amp]] == '..' + amp + amp:
                new_hall = hall[:hall_num] + '.' + hall[hall_num + 1:]
                new_rooms = copy.deepcopy(rooms)
                new_rooms[room_nums[amp]] = '.' + amp + amp + amp
                if hall_num < room_nums[amp] + 2:
                    distance = (room_nums[amp] + 1 - hall_num) * 2 + 3 - (
                            hall_num == 0)
                else:
                    distance = (hall_num - room_nums[amp] - 2) * 2 + 3 - (
                            hall_num == 6)
                next_states.append(
                    [
                        make_state_str(new_hall, new_rooms),
                        energy + distance * energies[amp],
                        path + [state],
                    ]
                )
            elif rooms[room_nums[amp]] == '.' + amp + amp + amp:
                new_hall = hall[:hall_num] + '.' + hall[hall_num + 1:]
                new_rooms = copy.deepcopy(rooms)
                new_rooms[room_nums[amp]] = amp + amp + amp + amp
                if hall_num < room_nums[amp] + 2:
                    distance = (room_nums[amp] + 1 - hall_num) * 2 + 2 - (
                            hall_num == 0)
                else:
                    distance = (hall_num - room_nums[amp] - 2) * 2 + 2 - (
                            hall_num == 6)
                next_states.append(
                    [
                        make_state_str(new_hall, new_rooms),
                        energy + distance * energies[amp],
                        path + [state],
                    ]
                )

    for room_num, room in enumerate(rooms):
        if (room[0] != '.' and room[1] != '.' and room[2] != '.' and room[3]
            != '.'
        ) and (
                room_nums[room[0]] != room_num or room_nums[room[1]] !=
                room_num or room_nums[room[2]] != room_num or room_nums[
                    room[3]] != room_num):
            amp = room[0]
            for hall_num, spot in enumerate(hall):
                if spot == '.' and all_free(hall, hall_num, room_num):
                    new_hall = hall[:hall_num] + amp + hall[hall_num+1:]
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_num] = '.' + new_rooms[room_num][1:]
                    if hall_num < room_num + 2:
                        distance = (room_num + 1 - hall_num) * 2 + 2 - (hall_num
                                                                        == 0)
                    else:
                        distance = (hall_num - room_num - 2) * 2 + 2 - (hall_num == 6)
                    next_states.append(
                        [
                            make_state_str(new_hall, new_rooms),
                            energy + distance * energies[amp],
                            path + [state],
                        ]
                    )
        elif (room[0] == '.' and room[1] != '.' and room[2] != '.' and room[
            3] != '.') and (room_nums[room[1]] != room_num or room_nums[
            room[2]] !=
             room_num or room_nums[room[3]] != room_num):
            amp = room[1]
            for hall_num, spot in enumerate(hall):
                if spot == '.' and all_free(hall, hall_num, room_num):
                    new_hall = hall[:hall_num] + amp + hall[hall_num+1:]
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_num] = '..' + new_rooms[room_num][2:]
                    if hall_num < room_num + 2:
                        distance = (room_num + 1 - hall_num) * 2 + 3 - (
                                hall_num == 0)
                    else:
                        distance = (hall_num - room_num - 2) * 2 + 3 - (hall_num == 6)
                    next_states.append(
                        [
                            make_state_str(new_hall, new_rooms),
                            energy + distance * energies[amp],
                            path + [state],
                        ]
                    )
        elif (room[0] == '.' and room[1] == '.' and room[2] != '.' and room[
            3] != '.') and (room_nums[
            room[2]] !=
             room_num or room_nums[room[3]] != room_num):
            amp = room[2]
            for hall_num, spot in enumerate(hall):
                if spot == '.' and all_free(hall, hall_num, room_num):
                    new_hall = hall[:hall_num] + amp + hall[hall_num+1:]
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_num] = '...' + new_rooms[room_num][3]
                    if hall_num < room_num + 2:
                        distance = (room_num + 1 - hall_num) * 2 + 4 - (
                                hall_num == 0)
                    else:
                        distance = (hall_num - room_num - 2) * 2 + 4 - (
                                hall_num == 6)
                    next_states.append(
                        [
                            make_state_str(new_hall, new_rooms),
                            energy + distance * energies[amp],
                            path + [state],
                        ]
                    )
        elif (room[0] == '.' and room[1] == '.' and room[2] == '.' and room[
            3] != '.') and (room_nums[room[3]] != room_num):
            amp = room[3]
            for hall_num, spot in enumerate(hall):
                if spot == '.' and all_free(hall, hall_num, room_num):
                    new_hall = hall[:hall_num] + amp + hall[hall_num+1:]
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_num] = '....'
                    if hall_num < room_num + 2:
                        distance = (room_num + 1 - hall_num) * 2 + 5 - (
                                hall_num == 0)
                    else:
                        distance = (hall_num - room_num - 2) * 2 + 5 - (
                                hall_num == 6)
                    next_states.append(
                        [
                            make_state_str(new_hall, new_rooms),
                            energy + distance * energies[amp],
                            path + [state],
                        ]
                    )
    return next_states


def run_dijkstra(start_state):
    state_energies = {
        start_state: 0
    }
    state_paths = {
        start_state: []
    }
    popped_states = []
    all_states = [start_state]
    while True:
        min_energy = 10**100
        minstate = None
        for state in all_states:
            if state_energies[state] < min_energy:
                min_energy = state_energies[state]
                minstate = state
        print(f'{min_energy}, {len(all_states)}, {len(popped_states)}')
        if minstate == '.......AAAABBBBCCCCDDDD':
            for p in state_paths[minstate]:
                print(p)
            return state_energies[minstate]
        next_states = find_next_states(minstate, state_energies[minstate],
                                       state_paths[minstate])
        all_states.remove(minstate)
        popped_states.append(minstate)
        for next_state, next_energy, next_path in next_states:
            if next_state not in popped_states:
                if (next_state in state_energies and state_energies[
                    next_state] > next_energy) or (next_state not in
                state_energies):
                        state_energies[next_state] = next_energy
                        state_paths[next_state] = next_path
                        all_states.append(next_state)


print(f'Gold: {run_dijkstra(initial_state)}')
