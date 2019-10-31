def merge(vec1, vec2):
    n1 = len(vec1)
    n2 = len(vec2)
    vec = list()
    i1, i2 = 0, 0

    while True:
        if i1 < n1 and i2 < n2:
            if vec1[i1] < vec2[i2]:
                vec.append(vec1[i1])
                i1 += 1
            else:
                vec.append(vec2[i2])
                i2 += 1
        elif i1 < n1:
            vec += vec1[i1:]
            break
        else:
            vec += vec2[i2:]
            break
    return vec


def mergesort(vec):
    if len(vec) <= 1:
        return vec

    mid = len(vec)//2
    vec1 = vec[:mid]
    vec2 = vec[mid:]

    vec1 = mergesort(vec1)
    vec2 = mergesort(vec2)

    return merge(vec1, vec2)


a = [5, 4, 3, 2, 1]
print(mergesort(a))
