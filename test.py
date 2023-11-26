def isss():
    nums = [0,4,3,0]
    target = 0
    result =[]
    for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i] > target or i == j:
                        continue
                    elif (nums[i] + nums[j]) == target:
                        return [i,j]
print(isss())