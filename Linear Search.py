from numpy.f2py.crackfortran import true_intent_list

pos = -1    #since the position starts from 0
def search(list, m):
    for i in list:
        if m == i:
            globals() ['pos'] = list.index(i)
            return True

    return False

list = [1,2,3,5,6,8]
n = int(input("Enter value to search: "))
if search(list, n):
    print("Value Found in index ", pos+1)
else:
    print("Value not Found.")