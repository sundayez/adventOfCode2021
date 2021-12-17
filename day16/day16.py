def read_file(filename):
    file_obj = open(filename, "r")  # opens the file in read mode
    lines = file_obj.read().splitlines()  # puts the file into an array
    file_obj.close()
    return lines


class Packet:
    def __init__(self, packet_version, packet_type_id, literal=-1, acc=-1, remaining_binary=""):
        self.packet_version = packet_version
        self.packet_type_id = packet_type_id
        self.literal = literal
        self.acc = acc
        self.remaining_binary = remaining_binary
        self.subpackets = []

    def add_subpacket(self, subpacket):
        self.subpackets.append(subpacket)

    def version_sum(self):
        total = self.packet_version
        for subpacket in self.subpackets:
            total += subpacket.version_sum()
        return total

    def evaluate(self):
        if self.packet_type_id == 0:
            result = 0
            for subpacket in self.subpackets:
                result += subpacket.evaluate()
            return result
        if self.packet_type_id == 1:
            result = 1
            for subpacket in self.subpackets:
                result *= subpacket.evaluate()
            return result
        if self.packet_type_id == 2:
            result = 100000
            for subpacket in self.subpackets:
                result = min(result, subpacket.evaluate())
            return result
        if self.packet_type_id == 3:
            result = -100000
            for subpacket in self.subpackets:
                result = max(result, subpacket.evaluate())
            return result
        if self.packet_type_id == 4:
            return self.literal
        if self.packet_type_id == 5:
            if self.subpackets[0].evaluate() > self.subpackets[1].evaluate():
                return 1
            return 0
        if self.packet_type_id == 6:
            if self.subpackets[0].evaluate() < self.subpackets[1].evaluate():
                return 1
            return 0
        if self.packet_type_id == 7:
            if self.subpackets[0].evaluate() == self.subpackets[1].evaluate():
                return 1
            return 0


def binary_string_to_decimal(binary):
    return int(binary, 2)


def read_packet_version(binary):
    packet_version = binary[0:3]
    binary = binary[3:]
    return binary, binary_string_to_decimal(packet_version), 3


def read_length(binary):
    length = binary[:15]
    binary = binary[15:]
    return binary, binary_string_to_decimal(length), 15


def read_subpackets_number(binary):
    length = binary[:11]
    binary = binary[11:]
    return binary, binary_string_to_decimal(length), 11


def read_packet_type_id(binary):
    packet_type_id = binary[0:3]
    binary = binary[3:]
    return binary, binary_string_to_decimal(packet_type_id), 3


def read_packet(binary):
    if len(binary) < 6:
        return Packet(0, 0)
    acc = 0
    binary, packet_version, count = read_packet_version(binary)
    acc += count
    # print(packet_version)
    binary, packet_type_id, count = read_packet_type_id(binary)
    acc += count
    # print(packet_type_id)
    if packet_type_id == 4:
        literal = ""
        while binary[0] == '1':
            literal += binary[1:5]
            binary = binary[5:]
            acc += 5
        literal += binary[1:5]
        binary = binary[5:]
        acc += 5
        return Packet(packet_version, packet_type_id, literal=binary_string_to_decimal(literal), acc=acc,
                      remaining_binary=binary)
    packet = Packet(packet_version, packet_type_id)
    type_id = binary[0]
    binary = binary[1:]
    acc += 1
    if type_id == '0':
        binary, length, count = read_length(binary)
        acc += count
        partial = 0
        while partial != length:
            subpacket = read_packet(binary)
            packet.add_subpacket(subpacket)
            binary = subpacket.remaining_binary
            partial += subpacket.acc
        acc += length
        packet.acc = acc
        packet.remaining_binary = binary
        return packet
    binary, subpackets_number, count = read_subpackets_number(binary)
    acc += count
    for i in range(subpackets_number):
        subpacket = read_packet(binary)
        acc += subpacket.acc
        packet.add_subpacket(subpacket)
        binary = subpacket.remaining_binary
    packet.acc = acc
    packet.remaining_binary = binary
    return packet


def part_one(binary):
    packet = read_packet(binary)
    print(packet.version_sum())
    print(packet.evaluate())


def part_two(binary):
    1


def hex_string_to_bin_string(hex_string):
    conversion = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
                  '7': '0111',
                  '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
                  'F': '1111'}
    return ''.join([conversion[c] for c in hex_string])


def main():
    lines = read_file("input.txt")
    binary = hex_string_to_bin_string(lines[0])
    part_one(binary)
    part_two(binary)


main()
