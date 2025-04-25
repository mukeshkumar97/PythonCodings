
pos = -1    #since the position starts from 0
def search(list, n):
    l, u = 0, len(list)-1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

list = [1,2,3,5,6,8,10]
n = int(input("Enter value to search: "))
if search(list, n):
    print("Value Found in index ", pos+1)
else:
    print("Value not Found.")