def timesTable(nums):
    mainlist = []
    
    for i in range(1, nums + 1):
        templist = []
        for j in range(1, nums + 1):
          templist.append(i*j) 
        mainlist.append(templist) 
    return mainlist

# testing
nums = int(input())
print(timesTable(nums))
