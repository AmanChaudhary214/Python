# Bubble Sort

def bubble_sort(list):

    n = len(list)
    swapped = 0
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                swapped = 1
                list[j], list[j+1] = list[j+1], list[j]
                
            if swapped == 0:
                return


list = [5,3,8,6,7,2]

bubble_sort(list)

print(list)




# Selection Sort

def selection_sort(nums):

    n = len(nums)
    
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if nums[j] < nums[min]:
                min = j

        nums[i], nums[min] = nums[min], nums[i]


nums = [5,3,8,6,7,2]

selection_sort(nums)

print(nums)
