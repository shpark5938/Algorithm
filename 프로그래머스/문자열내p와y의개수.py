def solution(s):
    answer = True
    pnum = 0
    ynum = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pnum += 1
        elif s[i] == 'y' or s[i] == 'Y':
            ynum += 1
    if pnum == ynum:
        return True
    else:
        return False


print(solution("pPoooyY"))