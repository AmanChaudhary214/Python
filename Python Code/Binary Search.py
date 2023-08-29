# Binary Search


pos = -1

def search(list, k):
    start = 0
    end = len(list)-1

    while start <= end:
        
        mid = (start + end)//2
        
        if list[mid]==k:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < k:
                start = mid+1
            else:
                end = mid-1
                
    return False
        


list = [4,7,8,12,45,99]
k = 45

if search(list, k):
    print("Found at index", pos)
else:
    print("Not Found")
