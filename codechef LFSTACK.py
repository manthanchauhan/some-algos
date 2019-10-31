t = int(input())

for tc in range(0, t):
    n = int(input())

    nums_pushed = list()

    for thread in range(0, n):
        nums = input().split()
        nums = [int(num) for num in nums]
        a = nums[0]
        nums = nums[1:a + 1]
        nums_pushed.append(nums)

    seq = input().split()
    seq = [int(num) for num in seq]
    seq = seq[::-1]
    size = len(seq)
    used = [False] * size


    def check_occurence(nums):
        itr = 0

        for num in nums:
            while itr < size and (seq[itr] != num or used[itr]):
                itr += 1

            if itr == size:
                return False

            used[itr] = True
            itr += 1

        return True


    flag = False

    for nums in nums_pushed:
        if not check_occurence(nums):
            flag = True
            break

    if flag:
        print('No')
    else:
        print('Yes')
