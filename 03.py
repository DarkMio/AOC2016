collector = []
with open("test_input.txt", "r") as f:
    for line in f.readlines():
        group = pattern.search(line).groups()
        a, b, c = map(lambda x: int(x), group)
        collector.append((a, b, c))

i = 0
for line in data:
    group = pattern.search(line).groups()
    a, b, c = map(lambda x: int(x), group)
    if (a + b) > c and (a + c) > b and (b + c) > a:
        i += 1
print("Solution Part 1:", i)

i = 0
while collector:
    # disposes data
    group = [collector.pop() for _ in range(3)]
    for tri in [[group[y][x] for y in range(3)] for x in range(3)]:
        if tri[0] + tri[1] > tri[2] and tri[1] + tri[2] > tri[0] and tri[0] + tri[2] > tri[1]:
            i += 1

print("Solution Part 2:", len(triangles))
