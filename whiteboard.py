def countDuplicates(string1):
    d = {}
    for char in string1.upper():
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    print(d)

    answer = 0
    for uniqueChar in d:
        if d[uniqueChar] > 1:
            answer += 1
    return answer

print(countDuplicates("aabBcde"))