nums = list(map(int, input().split()))
max_i, min_i = nums[0], nums[-1]
a, b = set(), set()
for i in range(len(nums)):
    # max_i = max(max_i, nums[i])
    if nums[i] >= max_i:
        max_i = nums[i]
        a.add(i)
    if nums[-1-i] <= min_i:
        min_i = nums[-1-i]
        b.add(len(nums)-1-i)
a.intersection_update(b)
print(len(a))
print(('%d '*len(a)).strip() % tuple(nums[i] for i in sorted(a)))
