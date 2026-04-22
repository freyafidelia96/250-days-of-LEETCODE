def mergeSort(nums):
  if len(nums) <= 1:
    return nums
  
  mid = len(nums) // 2
  
  leftHalf = mergeSort(nums[:mid])
  rightHalf = mergeSort(nums[mid:])
  
  return merge(leftHalf, rightHalf)

def merge(left, right):
  merged = []
  i,j = 0,0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  
  while i < len(left):
    merged.append(left[i])
    i += 1
    
  while j < len(right):
    merged.append(right[j])
    j += 1
  
  return merged

def quickSort(arr, low, high):
  if low < high: 
    pi = partition(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)
    
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  
  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1
  


if __name__ == "__main__":
  nums = [38, 27, 43, 3, 9, 82, 10]
  sortedNums = mergeSort(nums)
  print("Unsorted:", nums)
  print("Sorted:", sortedNums)
  
  quickSort(nums, 0, len(nums) - 1)
  print("QuickSorted:", nums)