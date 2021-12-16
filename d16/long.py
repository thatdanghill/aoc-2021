import sys

hex_str, = open(sys.argv[1])
hex_str = hex_str[:-1]
bin_str = bin(int(hex_str, 16))[2:]

def process_packet(packet):
    if int(packet, 2) == 0:
        return None, ''

    version = int(packet[0:3], 2)
    type_id = int(packet[3:6], 2)
    packet_desc = {
        'version_code': version,
        'type_id': type_id
    }

    if type_id == 4:
        literal, remaining = process_literal_packet_data(packet[6:])
        packet_desc['literal'] = literal
    else:
        length_type_id = int(packet[6])
        packet_desc['length_type_id'] = length_type_id
        if length_type_id:
            num_subpackets = int(packet[7:18],2)
            remaining = packet[18:]
            subpacket_descs = []
            for _ in range(num_subpackets):
                subpacket_desc, remaining = process_packet(remaining)
                subpacket_descs.append(subpacket_desc)
            packet_desc['subpackets'] = subpacket_descs
        else:
            subpackets_len = int(packet[7:22],2)
            subpacket_descs = []
            subpackets = packet[22:22+subpackets_len]
            while len(subpackets) > 0:
                subpacket_desc, subpackets = process_packet(subpackets)
                subpacket_descs.append(subpacket_desc)
            packet_desc['subpackets'] = subpacket_descs
            remaining = packet[22+subpackets_len:]

    return packet_desc, remaining

def process_literal_packet_data(packet_data):
    i = 0
    parsing_packet = True
    literal = ''
    while parsing_packet:
        if packet_data[5*i] == '0':
            parsing_packet = False
        literal += packet_data[5*i+1:5*(i+1)]
        i += 1
    return int(literal, 2), packet_data[5*i:]

def get_version_code_sum(packet_desc):
    version_sum = packet_desc['version_code']
    for subpacket in packet_desc.get('subpackets', []):
        version_sum += get_version_code_sum(subpacket)
    return version_sum

def get_operation_value(packet_desc):
    type_id = packet_desc['type_id']
    if type_id == 4:
        return packet_desc['literal']
    subpacket_vals = [
        get_operation_value(subpacket)
        for subpacket in packet_desc['subpackets']
    ]
    if type_id == 0:
        return sum(subpacket_vals)
    if type_id == 1:
        product = 1
        for val in subpacket_vals:
            product *= val
        return product
    if type_id == 2:
        return min(subpacket_vals)
    if type_id == 3:
        return max(subpacket_vals)
    if type_id == 5:
        return int(subpacket_vals[0] > subpacket_vals[1])
    if type_id == 6:
        return int(subpacket_vals[0] < subpacket_vals[1])
    if type_id == 7:
        return int(subpacket_vals[0] == subpacket_vals[1])

packet_desc = process_packet(bin_str)[0]
print(f'Silver: {get_version_code_sum(packet_desc)}')
print(f'Gold: {get_operation_value(packet_desc)}')

