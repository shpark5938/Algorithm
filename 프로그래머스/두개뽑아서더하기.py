def solution(numbers):
    answer = list()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                sum = numbers[i] + numbers[j]
                answer.append(sum)
    answer.sort()
    return answer


tnum = [2, 1, 3, 4, 1]
print(solution(tnum))