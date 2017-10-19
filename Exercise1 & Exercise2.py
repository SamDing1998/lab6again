def permute(nums):
    if len(nums) == 0 or len(nums) == 1:
        return [nums]
    else:
        result = []
        for i in nums:
            templist = nums[:]
            templist.remove(i)
            temp = permute(templist)
			
					 
            for j in temp:
                j[0:0] = [i]
                result.append(j)
    lists = []
    for k in result:
        if not k in lists:
            lists.append(k)
    lists.sort()
    return lists

print(permute([1,1,5]))

def next_permute(curr_perm):
    s = permute(curr_perm)
    t = s.index(curr_perm)
    if t == len(s) - 1:
        return s[0]
    else:
        return s[t+1]

"caonima"
