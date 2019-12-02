import sys, math, time
startTime = time.time()
inputs = [int(x) for x in sys.stdin]

# initialize answer vars
part1 = 0
part2 = 0

# part1: calculate total fuel required. mass divided by 3, round down (floor division), subtract 2.
# calculate sum to achieve result
for i in inputs:
    part1 += math.floor(i / 3) - 2

print("part1:",part1)    
print("part1 time: %s seconds" % (time.time() - startTime))
# reset the clock
startTime = time.time()