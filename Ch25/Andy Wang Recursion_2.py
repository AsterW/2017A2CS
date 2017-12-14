# Andy Wang
# This is the solutions to recursion_2 in Coding Bat


def groupSum(start, array, target):
    if target == 0:
        return True
    if start == len(array):
        return False
    return groupSum(start+1, array, target-array[start]) or groupSum(start+1, array, target)


def groupSum6(start, array, target):
    if target == 0:
        return True
    if start == len(array):
        return False
    if array[start] == 6:
        return groupSum6(start+1, array, target-array[start])
    return groupSum6(start+1, array, target-array[start]) or groupSum(start+1, array, target)


def groupNoAdj(start, array, target):
    if target == 0:
        return True
    if start >= len(array):
        return False
    return groupNoAdj(start+2, array, target-array[start]) or groupNoAdj(start+1, array, target)


def groupSum5(start, array, target):
    if target == 0:
        return True
    if start >= len(array):
        return False
    if array[start] % 5 == 0:
        if array[start+1] == 1:
            return groupSum5(start+2, array, target-array[start])
        return groupSum5(start+1, array, target-array[start])
    return groupSum5(start+1, array, target-array[start]) or groupSum5(start+1, array, target)


def groupSumClump(start, array, target, x=1):
    if target == 0:
        return True
    if start >= len(array):
        return False
    while array[start+1] == array[start]:
        x = x+1
        start += 1
    return groupSumClump(start+x, array, target-array[start]*x) or groupSumClump(start+x, array, target)


def splitArray(array, target=0, start=0):
    if target == sum(array)/2:
        return True
    if start >= len(array):
        return False
    return splitArray(array, target=target+array[start], start=start+1) \
           or splitArray(array, target=target, start=start+1)


def splitOdd10(array, target=0, start=0):
    if target % 10 == 0 and (sum(array)-target) % 2 == 1:
        return True
    if start >= len(array):
        return False
    return splitOdd10(array, target=target+array[start], start=start+1) \
           or splitOdd10(array, target=target, start=start + 1)


def split53(array, target=0, start=0):
    if target == sum(array)-target:
        return True
    if start >= len(array):
        return False
    if array[start] % 5 == 0:
        return split53(array, target=target+array[start], start=start+1)
    if array[start] % 3 == 0:
        return split53(array, target=target, start=start+1)
    return split53(array, target=target+array[start], start=start+1) or split53(array, target=target, start=start+1)


print("groupSum(0,[2,4,8],10)", groupSum(0, [2, 4, 8], 10))
print("groupSum6(0,[5,6,2],7)", groupSum6(0, [5, 6, 2], 7))
print("groupNoAdj(0, [2,5,10,4], 12)", groupNoAdj(0, [2, 5, 10, 4], 12))
print("groupSum5(0, [2,5,1,10,1,4], 18)", groupSum5(0, [2, 5, 1, 10, 1, 4], 18))
print("groupSumClump(0, [2,4,4,8], 14)", groupSumClump(0, [2, 4, 4, 8], 14))
print("splitArray([5,2,3])", splitArray([5, 2, 3]))
print("splitOdd10([5,5,6,1])", splitOdd10([5, 5, 6, 1]))
print("split53([2,4,2])", split53([3, 5, 5, 3]))
