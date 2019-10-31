def bubblesort(vec):
    n = len(vec)

    for last_set in range(n, 0, -1):
        for i in range(0, last_set-1):
            if vec[i] > vec[i+1]:
                vec[i], vec[i+1] = vec[i+1], vec[i]

    return vec


a = [5, 4, 3, 2, 1]
print(bubblesort(a))
