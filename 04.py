def caesar_shift(char, n):
    return chr((ord(char.lower()) - 97 + n) % 26 + 97)

with open('input.txt', 'r') as f:
    data = f.readlines()
    data = [line.replace('\n', '').split('-') for line in data]
    for line in data:
        line[-1] = line[-1].replace(']', '').split('[')

values = []
for line in data:
    char_count = {}
    for segment in line:
        if segment is line[-1]:
            continue
        for char in segment:
            if not char in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    count_map = {'max': 0}
    for k, v in char_count.items():
        count_map['max'] = max(v, count_map['max'])
        if not v in count_map:
            count_map[v] = [k]
        else:
            count_map[v].append(k)
    for k, v in count_map.items():
        if k is 'max':
            continue
        count_map[k] = sorted(v)
    myChecksum = []
    for count in range(10, 0, -1):
        if not count in count_map:
            continue
        myChecksum.extend(count_map[count])
    myChecksum = ''.join(myChecksum)[0:5]
    if myChecksum == line[-1][-1]:
        values.append(line[-1][0])
print("Checksum Part 1:", sum(int(i) for i in values))

for line in data:
    pass_phrase = ""
    elements = line[:-1]
    for element in elements:
        for char in element:
            pass_phrase += caesar_shift(char, int(line[-1][0]))
        pass_phrase += " "
    if "north" in pass_phrase:
        print("Checksum Part 2:", pass_phrase, line[-1][0])
