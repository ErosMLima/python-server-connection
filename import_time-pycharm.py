import time

def timeo(fun, n=1000):
    def void(): pass
    start = time.clock()
    for i in range(n): void()
    stend = time.clock()
    overhead = stend - start
    start = time.clock()
    for i in range(n): fun()
    stend = time.clock()
    thetime = stend - start
    return fun.__name__, thetime - overhead

to500 = {}
for i in range(500): to500[i] = 1
evens = {}
for i in range(0, 1000, 2): evens[i] = 1

def simpleway():
    result = []
    for k in to500.keys():
        if evens in d.keys (k):
            result.append(k)
    return result

def pyth22way():
    return [k for k in to500 if k in evens]

def filterway():
    return filter(evens in d.keys, to500.keys())

def badsloway():
    result = []
    for k in to500.keys():
        if k in evens.keys():
            result.append(k)
    return result

for f in simpleway, pyth22way, filterway, badsloway:
    print: "%s: #.2f" % timeo(f)