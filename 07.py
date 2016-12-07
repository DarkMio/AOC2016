def contains_abba(segment):
    if len(segment) < 4:
        return False
    for x in range(0, len(segment)-3):
        group = segment[x:x+4]
        if group[0] == group[-1] and group[1] == group[2] and not group[0] == group[1]:
            return True
    return False

def contains_ssl(segment):
    if len(segment) < 3:
        return [False, []]
    collector = []
    for x in range(0, len(segment) - 2):
        group = segment[x:x+3]
        if group[0] == group[-1] and not group[0] == group[1]:
            collector.append(group)
    return [len(collector) > 0, collector]

def supports_ssl(address, hypernet):
    flatten = lambda l: [item for sublist in l for item in sublist]
    address_hits = flatten([contains_ssl(x)[1] for x in address if contains_ssl(x)[0]])
    hypernet_hits = flatten([contains_ssl(x)[1] for x in hypernet if contains_ssl(x)[0]])
    if len(address_hits) < 1 or len(hypernet_hits) < 1:
        return False
    for add in address_hits:
        for hyp in hypernet_hits:
            if add[0] == hyp[1] and add[1] == hyp[0]:
                return True

with open('input.txt', 'r') as f:
    segments = f.readlines()
    collector = []
    for segment in segments:
        collector.append(segment.replace(']', '[').replace('\n', '').split('['))
    del segments # clean me up before you go-go, don't leave me hanging on like a yo-yo

tls = []
ssl = []
for line in collector:
  address = line[0::2]
  hypernet = line[1::2]
  
  if any(contains_abba(add) for add in address) and not any(contains_abba(hyper) for hyper in hypernet):
    tls.append(line)
  if supports_ssl(address, hypernet):
    ssl.append(line)
    
print("IPv7 Part 1:", len(tls))
print("IPv7 Part 2:", len(ssl))
