import decimal
decimal.getcontext().prec = 101
r = decimal.Decimal(2).sqrt() # r = sqrt(2)
s = r + 2 # s = r/(r-1) = sqrt(2) + 2 = r + 2

def summation(n):
    # Beatty sequence: 
    # Br = [r], [2r], [3r], ...
    # where irrational number r > 1
    # Complementary Beatty sequences:
    # Bs = [s], [2s], [3s], ...
    # where s = r/(r-1)

    # Rayleigh Theorem:
    # Beatty sequences Br and Bs partition the set of positive integers
    # so, SUM_n{Br} + SUM_m{Bs} = SUM_Br(n){i} = Br(n)(Br(n)+1)/2
    # where m = [Br(n)/s]
    # because s = r + 2 here,
    # so, SUM_m{Bs} = SUM_m{Br} + m(m+1)
    # so, SUM_n{Br} = Br(n)(Br(n)+1)/2 - m(m+1) - SUM_m{Br}
    if n < 0.5:
        return 0
    Br_n = int(n*r)
    m = int(Br_n/s)
    return int( Br_n*(Br_n+1)/2 - m*(m+1) - summation(m) )
    
def solution(string):
    n = decimal.Decimal(string)
    return str(summation(n))


if __name__ == "__main__":
    print(solution('77'))
    # 4208
    print(solution('5'))
    # 19
    print(solution(str(10E100)))
    # 7071067811865475244008443621048490392848359376884740365883398689953662392310535194251937671638207863330094484323978218044033126805859358563835451103567853545228205032881160502041536154870126895628306898


# Dodge the Lasers!
# =================

# Oh no! You've managed to escape Commander Lambda's collapsing space station in an escape pod with the rescued bunny workers - but Commander Lambda isnt about to let you get away that easily. Lambda sent an elite fighter pilot squadron after you -- and they've opened fire!

# Fortunately, you know something important about the ships trying to shoot you down. Back when you were still Lambda's assistant, the Commander asked you to help program the aiming mechanisms for the starfighters. They undergo rigorous testing procedures, but you were still able to slip in a subtle bug. The software works as a time step simulation: if it is tracking a target that is accelerating away at 45 degrees, the software will consider the targets acceleration to be equal to the square root of 2, adding the calculated result to the targets end velocity at each timestep. However, thanks to your bug, instead of storing the result with proper precision, it will be truncated to an integer before adding the new velocity to your current position.  This means that instead of having your correct position, the targeting software will erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas testing, but enough that it might just save your life.

# If you can quickly calculate the target of the starfighters' laser beams to know how far off they'll be, you can trick them into shooting an asteroid, releasing dust, and concealing the rest of your escape.  Write a function solution(str_n) which, given the string representation of an integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range 1 to n, it adds up all of the integer portions of i*sqrt(2).

# For example, if str_n was "5", the solution would be calculated as
# floor(1*sqrt(2)) +
# floor(2*sqrt(2)) +
# floor(3*sqrt(2)) +
# floor(4*sqrt(2)) +
# floor(5*sqrt(2))
# = 1+2+4+5+7 = 19
# so the function would return "19".

# str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.
# Fortunately, you know something important about the ships trying to shoot you down. Back when you were still Commander Lambdas assistant, she asked you to help program the aiming mechanisms for the starfighters. They undergo rigorous testing procedures, but you were still able to slip in a subtle bug. The software works as a time step simulation: if it is tracking a target that is accelerating away at 45 degrees, the software will consider the targets acceleration to be equal to the square root of 2, adding the calculated result to the targets end velocity at each timestep. However, thanks to your bug, instead of storing the result with proper precision, it will be truncated to an integer before adding the new velocity to your current position.  This means that instead of having your correct position, the targeting software will erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas testing, but enough that it might just save your life.

# If you can quickly calculate the target of the starfighters' laser beams to know how far off they'll be, you can trick them into shooting an asteroid, releasing dust, and concealing the rest of your escape.  Write a function solution(str_n) which, given the string representation of an integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range 1 to n, it adds up all of the integer portions of i*sqrt(2).

# For example, if str_n was "5", the solution would be calculated as
# floor(1*sqrt(2)) +
# floor(2*sqrt(2)) +
# floor(3*sqrt(2)) +
# floor(4*sqrt(2)) +
# floor(5*sqrt(2))
# = 1+2+4+5+7 = 19
# so the function would return "19".

# str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.