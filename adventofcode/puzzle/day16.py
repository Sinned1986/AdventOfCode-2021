# Day 16: Packet Decoder


class Packet:
    def __init__(self, version, type_id, queue):
        self.version = version
        self.type_id = type_id


class ValuePacket(Packet):

    def __init__(self, version, type_id, queue):
        super(ValuePacket, self).__init__(version, type_id, queue)
        value = 0
        value_length = 0
        new_bits = read_bits(queue, 5)

        while True:
            value <<= 4
            value |= new_bits & 0xf
            value_length += 4
            if new_bits & 0x10 != 0:
                new_bits = read_bits(queue, 5)
            else:
                break
        self.value = value
        self.value_length = value_length


class OperatorPacket(Packet):
    def __init__(self, version, type_id, queue):
        super(OperatorPacket, self).__init__(version=version, type_id=type_id, queue=queue)

        length_type_id = read_bits(queue, 1)
        objects = []
        if length_type_id == 0:
            field_len = read_bits(queue, 15)
            raw_data = []
            for _ in range(field_len):
                raw_data.append(queue.pop(0))
            objects = parse_queue(raw_data)
        else:
            field_len = read_bits(queue, 11)
            objects = parse_queue(queue, field_len)

        self.packets = objects


def read_bits(my_queue, length):
    value = 0
    if len(my_queue) < length:
        raise OutOfBitsException
    for i in range(0, length):
        value <<= 1
        value |= my_queue.pop(0)
    return value


def read_file(file_name):
    queues = []
    with open(file_name) as fv:
        for row in fv:
            queue = []
            if len(row) == 0:
                break
            if row[0] == '\n':
                continue
            inputs = row[:-1]
            for char in inputs:
                val = int(char, 16)
                for i in range(0, 4):
                    bit = (val >> (3-i)) & 0x1
                    queue.append(bit)
            queues.append(queue)
    return queues


class OutOfBitsException(Exception):
    pass


def parse_queue(queue, limit=-1):
    objects = []
    try:
        while len(queue) > 6 and limit != 0:
            version = read_bits(queue, 3)
            type_id = read_bits(queue, 3)
            if type_id == 4:
                paket = ValuePacket(version=version, type_id=type_id, queue=queue)
                objects.append(paket)
            else:
                paket = OperatorPacket(version=version, type_id=type_id, queue=queue)
                objects.append(paket)

            if limit > 0:
                limit -= 1
    except OutOfBitsException as e:
        print('OutOfBitsException occured')
    return objects


def calc_version_sum(objects):
    version_sum = 0

    for object in objects:
        version_sum += object.version
        if object.type_id != 4:
            version_sum += calc_version_sum(object.packets)

    return version_sum


def day16a(file_name):
    queue = read_file(file_name)
    objects =parse_queue(queue[0])
    return calc_version_sum(objects)




if __name__ == '__main__':
    print(day16a('day/16/input.txt'))

