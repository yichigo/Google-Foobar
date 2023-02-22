def intPartitions(n, minSize = 1):
    # INPUT : integer "n", minimum partition size "minSize"
    # OUTPUT: list[list of integer partition]
    result = [[n]]
    # iterate 1st partition's size
    for n1 in range(minSize, n//2 + 1):
        result.extend([ [n1] + pRes for pRes in intPartitions(n - n1, minSize = n1) ])
    return result

def countPermutations(disjointCyclePartition):
    # INPUT : list of disjoint cycle partition
    # OUTPUT: number of permutations for this partition 
    # for 1st cycle (size = n1)
    # number of choices = n!/(n1!(n-n1)!)
    # number of orders  = n1!/n1
    # so, 1st cycle's number of permutations = n!/n1/(n-n1)!
    # so, 2nd cycle's number of permutations = (n-n1)!/n2/(n-n1-n2)!
    # ...... 
    # Vanish common factors:
    # so, number of permutations = n!/(n1*n2....)
    # Remove duplicated countings:
    # so, number of permutations = n!/(n1*n2....)/(count(distinct n1)!*...)
    n = sum(disjointCyclePartition)
    counts = {}
    result = factorial(n)
    for ni in disjointCyclePartition:
        counts[ni] = counts.get(ni, 0) + 1
        result //= ni * counts[ni]
    return result

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def solution(w, h, s):
    # Define a map X: A -> S
    # where A is the set of elements in matrix, S is the set of states
    # Define a permutation group G = {g}
    # where g is a permutation of A
    
    # Burnside's Lemma:
    # num of orbits |X/G| = SUM_g{num of fixed points of g} / |G|
    
    # Polya Enumeration Theorem:
    # num of orbits |X/G| = SUM_g{|S|^c(g)} / |G|
    # where c(g) is the number of cycles of g

    # |G|
    sizeG = factorial(w)*factorial(h)
    # initialize the number of fixed points
    numFixedPoint = 0
    # iterate disjoint cycle partitions
    for p1 in intPartitions(w):
        for p2 in intPartitions(h):
            cg = sum([ sum([ gcd(n1, n2) for n1 in p1 ]) for n2 in p2 ])
            numFixedPoint += (s**cg) * countPermutations(p1) * countPermutations(p2)
    numOrbit = numFixedPoint // sizeG
    return str(numOrbit)


if __name__ == "__main__":
    print(solution(1, 2, 2))
    print(solution(2, 1, 2))
    # Output:
    #     3
    print(solution(2, 2, 2))
    # Output:
    #     7
    print(solution(2, 3, 4))
    # Output:
    #     430
    print(solution(12, 12, 20))
    # Output:
    # 97195340925396730736950973830781340249131679073592360856141700148734207997877978005419735822878768821088343977969209139721682171487959967012286474628978470487193051591840


# Disorderly Escape
# =================

# Oh no! You've managed to free the bunny workers and escape Commander Lambdas exploding space station, but Lambda's team of elite starfighters has flanked your ship. If you dont jump to hyperspace, and fast, youll be shot out of the sky!

# Problem is, to avoid detection by galactic law enforcement, Commander Lambda planted the space station in the middle of a quasar quantum flux field. In order to make the jump to hyperspace, you need to know the configuration of celestial bodies in the quadrant you plan to jump through. In order to do *that*, you need to figure out how many configurations each quadrant could possibly have, so that you can pick the optimal quadrant through which youll make your jump. 

# There's something important to note about quasar quantum flux fields' configurations: when drawn on a star grid, configurations are considered equivalent by grouping rather than by order. That is, for a given set of configurations, if you exchange the position of any two columns or any two rows some number of times, youll find that all of those configurations are equivalent in that way -- in grouping, rather than order.

# Write a function solution(w, h, s) that takes 3 integers and returns the number of unique, non-equivalent configurations that can be found on a star grid w blocks wide and h blocks tall where each celestial body has s possible states. Equivalency is defined as above: any two star grids with each celestial body in the same state where the actual order of the rows and columns do not matter (and can thus be freely swapped around). Star grid standardization means that the width and height of the grid will always be between 1 and 12, inclusive. And while there are a variety of celestial bodies in each grid, the number of states of those bodies is between 2 and 20, inclusive. The solution can be over 20 digits long, so return it as a decimal string.  The intermediate values can also be large, so you will likely need to use at least 64-bit integers.

# For example, consider w=2, h=2, s=2. We have a 2x2 grid where each celestial body is either in state 0 (for instance, silent) or state 1 (for instance, noisy).  We can examine which grids are equivalent by swapping rows and columns.

# 00
# 00

# In the above configuration, all celestial bodies are "silent" - that is, they have a state of 0 - so any swap of row or column would keep it in the same state.

# 00 00 01 10
# 01 10 00 00

# 1 celestial body is emitting noise - that is, has a state of 1 - so swapping rows and columns can put it in any of the 4 positions.  All four of the above configurations are equivalent.

# 00 11
# 11 00

# 2 celestial bodies are emitting noise side-by-side.  Swapping columns leaves them unchanged, and swapping rows simply moves them between the top and bottom.  In both, the *groupings* are the same: one row with two bodies in state 0, one row with two bodies in state 1, and two columns with one of each state.

# 01 10
# 01 10

# 2 noisy celestial bodies adjacent vertically. This is symmetric to the side-by-side case, but it is different because there's no way to transpose the grid.

# 01 10
# 10 01

# 2 noisy celestial bodies diagonally.  Both have 2 rows and 2 columns that have one of each state, so they are equivalent to each other.

# 01 10 11 11
# 11 11 01 10

# 3 noisy celestial bodies, similar to the case where only one of four is noisy.

# 11
# 11

# 4 noisy celestial bodies.

# There are 7 distinct, non-equivalent grids in total, so solution(2, 2, 2) would return 7.
