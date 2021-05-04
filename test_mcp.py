# Problem Number 1 
def solutionNumber1(nums):
    list_end = []
    for i in nums:
        count = 0
        for j in nums:
            if i - j > 0:
                count+= 1
        if count == len(nums)-1:
            list_end.append(i)
    return list_end
    
def solutionNumber1Second(nums):
    if len(nums) <= 0:
        return []
    return [sorted(nums, reverse=True)[0]]
    
# Problem Number 2 
def solutionNumber2(nums, x):
    for i in nums:
        for j in nums:
            if i / j == x:
                del nums[nums.index(i)]
    return nums
    
# Problem Number 3 
def solutionNumber3(word):
    return len(word.split(" "))

if __name__ == '__main__':
    # Input Problem Number 1
    nums = [3,1,2,4]
    print(f"Solution for problem 1 (First - with logic) = {solutionNumber1(nums)}")
    """
    For problem 1 the solution is simple only get the largest of data in list/array it should not even subtracted bellow zero
    """
    print(f"Solution for problem 1 (Second) = {solutionNumber1Second(nums)}")
    
    
    # Input Problem Number 2
    nums = [1,2,3,4]
    x = 4
    print(f"Solution for problem 2 = {solutionNumber2(nums, x)}")
    
    
    # Input Problem Number 3
    word = "souvenir loud four lost"
    print(f"Solution for problem 3 = {solutionNumber3(word)}")
