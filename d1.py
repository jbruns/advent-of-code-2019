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

# part2: also calculate the fuel required for the added fuel. same calc as for part1; for each input we do the fuel calc and then iterate 
# fuel required on the additional mass, until we reach negative fuel required (interpreted as zero)
for i in inputs:
    # do the initial calc (not accounting for additional mass added by this fuel)
    fuel = 0
    fuel = math.floor(i / 3) - 2
    # include the first calc in the final result
    part2 += fuel
    # if there is additional fuel required based on the mass we've just added, calc that too, and keep doing so until we reach zero additional fuel
    while (math.floor(fuel / 3) - 2) > 0:
        fuel = math.floor(fuel / 3) - 2
        # add the additional fuel required to the total result, reentering the loop until we've added all that is required
        part2 += fuel

print("part2:",part2)
print("part2 time: %s seconds" % (time.time() - startTime))