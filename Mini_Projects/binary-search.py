# naive search
# Match every element, if yes: return index, if no: return -1
def naive_search(l, target):
    for item in range(len(l)):
        if l[item] == target:
            return item
    return print("Element not found")


list = [1, 2, 3, 4, 5, 6, 7, 9]



# Binary search
# We leverage the fact that our list elements are sorted
def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2
    # [1,2,3,4,6]
    if list[midpoint] == target:
        return midpoint
    elif list[midpoint] > target:
        return binary_search(list, target, low, midpoint-1)
    else: 
        list[midpoint] < target
        return binary_search(list, target, midpoint+1, high)
# list = [23,34,54,567,67,78,89,90]
# naive_search(list, 899)
# binary_search(list,899)
import time, random

length = 10000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3 * length, 3 * length))
sorted_list = sorted(sorted_list)
# print("sorted_list-->",sorted_list)
start = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
end = time.time()
print("Naive search took ->", (end - start), "seconds")
print("Naive search took ->", (end - start) * 1000 / length, "milliseconds") # this will count time to iterate over a single target

start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
end = time.time()
print("Binary search took ->", (end - start) , "seconds")
print("Binary search took ->", (end - start) * 1000/length, "milliseconds") # this will count time to iterate over a single target