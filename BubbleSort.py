#Bubble Sort

def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

n = int(input("Enter the lenght of the list: "))
mklist = []
for i in range(n):
    m = int(input("Enter value {}: ".format(i+1)))
    mklist.append(m)

sort(mklist)
print(mklist)