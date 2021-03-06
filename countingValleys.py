# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Function Description
#
# Complete the countingValleys function in the editor below.
# It must return an integer that denotes the number of valleys Gary traversed.
#
# countingValleys has the following parameter(s):
#
# n: the number of steps Gary takes
# s: a string describing his path (ie "U" or "D" for up and down)


# Stategy: we only care about the number of valleys, so figure out how many times
# Gary came back to sea level.

def countingValleys(n, s):
    # I'm not sure what to do with "n" so I am just adding it here so we can
    #       still pass it as an argument in this function for the program
    n = 0
    # lvl variable will keep track of times Gary comes to sea level
    lvl = 0
    # valleys variable will record total number of valleys
    valleys = 0
    # loop through s string and record lvl
    for x in range(len(s)):
        if x == "D":
            lvl -= 1
        elif x == "U":
            lvl += 1
            # if we just came UP to sea level
            if lvl == 0 & x == "U":
                valleys += 1

    print(valleys)
    return valleys



if __name__ == '__main__':
    countingValleys(8, "DDUUDDUU")



# Questions I still have:
# 1) only prints / returns 0 with this code; should print / return 2
