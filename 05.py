import hashlib

def find_code(door_id):
    first = []
    second = [None] * 8
    i = 0
    while None in second:
        m = hashlib.md5(door_id + str(i).encode('utf-8')).hexdigest()
        if m.startswith('00000'):
            print("{}: {}".format(door_id + str(i).encode('utf-8'), m))
            location = int(m[5], 16)
            first.append(m[5])
            if location < 8 and second[location] is None:
                second[location] = m[6]
        i += 1
    return [''.join(first[:8]), ''.join(second)]

door_id = 'uqwqemis'.encode('utf-8')
code_part = find_code(door_id)
print('MD5 Part1: {} \nMD5 Part2: {}'.format(code_part[0], code_part[1]))
