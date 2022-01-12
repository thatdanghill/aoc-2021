import sys
import copy

_,_,r1,r2,_ = open(sys.argv[1])

row1 = r1.split('#')[3:7]
row2 = r2.split('#')[1:-1]

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

initial_state = '.......'

for amp1, amp2 in zip(row1, row2):
    initial_state += amp1
    initial_state += amp2

print(initial_state)


def all_free(hall, hall_ind, room_num):
    if hall_ind < room_num + 2:
        return all([hall[i]=='.' for i in range(hall_ind+1, room_num + 2)])
    else:
        return all([hall[i]=='.' for i in range(room_num + 2,hall_ind)])


#############
#01.2.3.4.56#
###C#C#A#B###
  #D#D#B#A#
  #########



def parse_state_str(state):
    hall = state[0:7]
    rooms = [state[7:9], state[9:11], state[11:13], state[13:]]
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
            if rooms[room_nums[amp]] == '..':
                new_hall = hall[:hall_num] + '.' + hall[hall_num + 1:]
                new_rooms = copy.deepcopy(rooms)
                new_rooms[room_nums[amp]] = new_rooms[room_nums[amp]][0] + amp
                if hall_num < room_nums[amp] + 2:
                    distance = (room_nums[amp] + 1 - hall_num) * 2 + 3 - (hall_num==0)
                else:
                    distance = (hall_num - room_nums[amp] - 2) * 2 + 3 - (hall_num == 6)
                next_states.append(
                    [
                        make_state_str(new_hall, new_rooms),
                        energy + distance * energies[amp],
                        path + [state],
                    ]
                )
            elif rooms[room_nums[amp]] == '.' + amp:
                new_hall = hall[:hall_num] + '.' + hall[hall_num + 1:]
                new_rooms = copy.deepcopy(rooms)
                new_rooms[room_nums[amp]] = amp + new_rooms[room_nums[amp]][1]
                if hall_num < room_nums[amp] + 2:
                    distance = (room_nums[amp] + 1 - hall_num) * 2 + 2 - (hall_num == 0)
                else:
                    distance = (hall_num - room_nums[amp] - 2) * 2 + 2 - (hall_num == 6)
                next_states.append(
                    [
                        make_state_str(new_hall, new_rooms),
                        energy + distance * energies[amp],
                        path + [state],
                    ]
                )

    for room_num, room in enumerate(rooms):
        if room[0] != '.' and room[1] != '.' and (
                room_nums[room[0]] != room_num or room_nums[room[1]] != room_num):
            amp = room[0]
            for hall_num, spot in enumerate(hall):
                if spot == '.' and all_free(hall, hall_num, room_num):
                    new_hall = hall[:hall_num] + amp + hall[hall_num+1:]
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_num] = '.' + new_rooms[room_num][1]
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
        elif (room[0] == '.' and room[1] != '.' and
              room_nums[room[1]] != room_num):
            amp = room[1]
            for hall_num, spot in enumerate(hall):
                if spot == '.' and all_free(hall, hall_num, room_num):
                    new_hall = hall[:hall_num] + amp + hall[hall_num+1:]
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_num] = new_rooms[room_num][0] + '.'
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
    return next_states


def find_next_states_1(state):
    next_states = []
    energy = state[1]
    poses = state[0]
    hall = poses['h']
    rooms = poses['r']
    acc_states = state[2]
    #moves = state[3]
    # See if hallway items can be moved
    for i, amp in enumerate(hall):
        if amp == '':
            continue
        if all_free(hall, i, room_nums[amp]):
            if rooms[room_nums[amp]] == ['','']:
                new_hall = hall.copy()
                new_hall[i] = ''
                new_rooms = copy.deepcopy(rooms)
                new_rooms[room_nums[amp]][1] = amp
                if i < room_nums[amp] + 2:
                    distance = (room_nums[amp] + 1 - i) * 2 + 3 - (i==0)
                else:
                    distance = (i - room_nums[amp] - 2) * 2 + 3 - (i == 6)
                #new_moves = moves.copy()
                #new_moves[amp] += distance
                next_states.append(
                    [
                        {
                            'h': new_hall,
                            'r': new_rooms
                        },
                        energy + distance * energies[amp],
                        acc_states + [poses],
                        #new_moves,
                        #dist_from_done(new_hall, new_rooms)
                    ]
                )
            elif rooms[room_nums[amp]] == ['', amp]:
                new_hall = hall.copy()
                new_hall[i] = ''
                new_rooms = copy.deepcopy(rooms)
                new_rooms[room_nums[amp]][0] = amp
                if i < room_nums[amp] + 2:
                    distance = (room_nums[amp] + 1 - i) * 2 + 2 - (i == 0)
                else:
                    distance = (i - room_nums[amp] - 2) * 2 + 2 - (i == 6)
                #new_moves = moves.copy()
                #new_moves[amp] += distance
                next_states.append(
                    [
                        {
                            'h': new_hall,
                            'r': new_rooms
                        },
                        energy + distance * energies[amp],
                        acc_states + [poses],
                        #new_moves,
                        #dist_from_done(new_hall, new_rooms)
                    ]
                )

    for room_num, room in enumerate(rooms):
        if room[0] != '' and room[1] != '' and (
                room_nums[room[0]] != room_num or room_nums[room[1]] != room_num):
            amp = room[0]
            for hall_num, spot in enumerate(hall):
                if spot == '' and all_free(hall, hall_num, room_num):
                    new_hall = hall.copy()
                    new_hall[hall_num] = amp
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_num][0] = ''
                    if hall_num < room_num + 2:
                        distance = (room_num + 1 - hall_num) * 2 + 2 - (hall_num
                                                                        == 0)
                    else:
                        distance = (hall_num - room_num - 2) * 2 + 2 - (hall_num == 6)
                    #new_moves = moves.copy()
                    #new_moves[amp] += distance
                    next_states.append(
                        [
                            {
                                'h': new_hall,
                                'r': new_rooms
                            },
                            energy + distance * energies[amp],
                            acc_states + [poses],
                            #new_moves,
                            #dist_from_done(new_hall, new_rooms)
                        ]
                    )
        elif (room[0] == '' and room[1] != '' and
              room_nums[room[1]] != room_num):
            amp = room[1]
            for hall_num, spot in enumerate(hall):
                if spot == '' and all_free(hall, hall_num, room_num):
                    new_hall = hall.copy()
                    new_hall[hall_num] = amp
                    new_rooms = copy.deepcopy(rooms)
                    new_rooms[room_num][1] = ''
                    if hall_num < room_num + 2:
                        distance = (room_num + 1 - hall_num) * 2 + 3 - (
                                hall_num == 0)
                    else:
                        distance = (hall_num - room_num - 2) * 2 + 3 - (hall_num == 6)
                    #new_moves = moves.copy()
                    #new_moves[amp] += distance
                    next_states.append(
                        [
                            {
                                'h': new_hall,
                                'r': new_rooms
                            },
                            energy + distance * energies[amp],
                            acc_states + [poses],
                            #new_moves,
                            #dist_from_done(new_hall, new_rooms)
                        ]
                    )

    return next_states

def print_cave(state):
    print('#############')
    hall = state['h']
    hallstr = '#'
    for h in hall:
        hallstr += '.' if h == '' else h
    hallstr += '#'


def finished(states):
    for state, energy, path in states:
        if state['r'] == [['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]:
            for s in path:
                print(s)
            print(state)
            return energy
    return False


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
        if minstate == '.......AABBCCDD':
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


print(f'Silver: {run_dijkstra(initial_state)}')
