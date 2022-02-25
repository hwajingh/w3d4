# Given nums  [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.
# Example 2:
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five eleme


def removeElement(list1, value):
  
    i = 0
    while i < len(list1):
        if list1[i] == value:
            list1.pop(i)
        else:
            i+=1

    return(len(list1))

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))


def  rem_value(a_list, num):
    while num in a_list:
        a_list.remove(num)
    print(a_list)        

rem_value([3,2,2,3], 3)