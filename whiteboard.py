# Given nums  [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.
# Example 2:
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five elements being
# the elements that are not val, in their original order.


def removeElement(list1, value):
    # FIX: O(n) two-pointer in-place overwrite. The original pop(i) in a
    # loop shifted the whole tail on every removal, making it O(n^2).
    write = 0
    for read in range(len(list1)):
        if list1[read] != value:
            list1[write] = list1[read]
            write += 1
    return write

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))


def rem_value(a_list, num):
    # FIX: same O(n^2) problem as above (while num in a_list: remove(num)).
    a_list[:] = [x for x in a_list if x != num]
    print(a_list)

rem_value([3,2,2,3], 3)
