# This problem is maximum matching in a non-bipartite graph
# The standard solution is Blossom Algorithm, which is very complicated
# I guess the rank of graph matrix is somehow related to the maximum matching
# After searching online, I found Tutte Theorem
import numpy as np

def isInfinite(a, b):
    # Check if game (a, b) is infinite
    if a == b: # equal: end
        return False
    elif (a % 2) != (b % 2): # 1 odd, 1 even: Infinite
        return True
    elif (a % 2) == 0: # both even: both /2
        return isInfinite(a//2, b//2)
    else: # both odd: small, big -> small*2, big-small -> small, (big-small)/2
        return isInfinite(min(a, b), abs(a - b)//2)

def list2Tutte(nums):
    # transfer banana list to graph matrix's Tutte matrix
    # t[i][j] =  Xij, if i < j and game(a, b) is infinite
    # t[i][j] = -Xij, if i > j and game(a, b) is infinite
    # t[i][j] = 0, otherwise
    # where Xij is a random positive number
    n = len(nums)
    t = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if isInfinite(nums[i], nums[j]):
                xij = np.random.randint(1, 2**30)
                t[i][j] =  xij
                t[j][i] = -xij
    return t
    
def solution(banana_list):
    #Your code here
    t = list2Tutte(banana_list)
    return len(banana_list) - np.linalg.matrix_rank(t)


if __name__ == "__main__":
    print(solution([1, 7, 3, 21, 13, 19]))
    print(solution([1, 1]))
    print(solution([1, 2, 3, 4, 5]))


# Distract the Trainers
# =====================

# The time for the mass escape has come, and you need to distract the bunny trainers so that the workers can make it out! Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working as first a minion and then a henchman means that you know the trainers are fond of bananas. And gambling. And thumb wrestling.

# The bunny trainers, being bored, readily accept your suggestion to play the Banana Games.

# You will set up simultaneous thumb wrestling matches. In each match, two trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet all their bananas, and the other trainer will match the bet. The winner will receive all of the bet bananas. You don't pair off trainers with the same number of bananas (you will see why, shortly). You know enough trainer psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, both of them will lose interest and go back to supervising the bunny workers, and you don't want THAT to happen!

# For example, if the two trainers that were paired started with 3 and 5 bananas, after the first round of thumb wrestling they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to training bunnies.

# How is all this useful to distract the bunny trainers? Notice that if the trainers had started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

# Now your plan is clear. You must pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop!

# Write a function solution(banana_list) which, given a list of positive integers depicting the amount of bananas the each trainer starts with, returns the fewest possible number of bunny trainers that will be left to watch the workers. Element i of the list will be the number of bananas that trainer i (counting from 0) starts with.

# The number of trainers will be at least 1 and not more than 100, and the number of bananas each trainer starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.
