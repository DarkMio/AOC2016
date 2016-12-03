def is_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a

# after conforming the input
collector = []
with open('test_input.txt', 'r') as f:
    for line in f.readlines():
        # explicit, because otherwise it's ugly
        a, b, c = map(lambda x: int(x), line.split())
        collector.append((a, b, c))

i = 0
for line in collector:
    if is_triangle(*line):
        i += 1
print("Triangles Part 1:", i)

i = 0
while collector:
    # get a group of 3 - and this disposes the initial data, too
    group = [collector.pop() for _ in range(3)]
    # build a patch of 3 row values per column
    for tri in [[group[y][x] for y in range(3)] for x in range(3)]:
        if is_triangle(*tri):
            i += 1

print("Triangles Part 2:", i)
