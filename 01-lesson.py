# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def removeGap(B):
    start, end = -1, -1
    start = B.find("1")
    if start == -1:
        return 0, 0
    else:
        end = B.find("1", start+1)
        if end == -1:
            return "0", 0
        #print(B, start, end, B[end:])
        return B[end:], end-start-1

def solution(N):
    # write your code in Python 3.6
    B = "{0:b}".format(N)
    print(B)
    if len(B) < 3: return 0

    gaps = []
    while len(B) >= 3:
        B, gap = removeGap(B)
        gaps.append(gap)
    return max(gaps)

    pass
