#Selection Sort

def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i+1,len(nums),1):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)

n = int(input("Enter the length of the list: "))
mklist = []
for i in range(n):
    m = int(input(f"Enter the value {i+1}: "))
    mklist.append(m)

sort(mklist)
print(mklist)