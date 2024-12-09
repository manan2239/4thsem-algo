def quick(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[0]
  left = [x for x in arr[1:] if pivot <= x]
  right = [x for x in arr[1:] if pivot > x]
  return quick(left) + [pivot] + quick(right)

if __name__ == "__main__":
  arr = [23,34, 10, 5, 2]
  print("Original: ", arr)
  print("Sorted: ", quick(arr))
