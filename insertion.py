def insert(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j] > key:
      arr[j+1] = arr[j]
      j-=1
      arr[j+1]=key
  return arr

if __name__ == "__main__":
  arr = [3, 55, 66, 78, 10]
  print("Original array: ", arr)
  print("Sorted array: ", insert(arr))
