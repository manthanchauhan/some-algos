def pivot(vec, beg, end):
    mid = vec[(end + beg)//2]
    ans = beg-1

    for i in range(beg, end):
        if vec[i] <= mid:
            vec[ans+1], vec[i] = vec[i], vec[ans+1]
            ans += 1
    return ans


def quick_sort(vec, beg, end):
    if end-beg <= 1:
        return vec
    print(beg, end)
    p = pivot(vec, beg, end)
    quick_sort(vec, beg, p)
    quick_sort(vec, p+1, end)
    return vec


a = [2, 4, 1, 3, 6]
print(quick_sort(a, 0, len(a)))
