def bubble_sort(arr):
      """Sort a list in ascending order using the bubble sort algorithm.

          Args:
                  arr: List of comparable elements.

                      Returns:
                              Sorted list in ascending order.
                                  """
      n = len(arr)
      arr = arr.copy()
      for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                              if arr[j] > arr[j + 1]:
                                                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                                                swapped = True
                                        if not swapped:
                                                      break
                                              return arr


if __name__ == "__main__":
      raw = input("Enter numbers separated by spaces: ")
      numbers = list(map(float, raw.split()))
      print(f"Original : {numbers}")
      print(f"Sorted   : {bubble_sort(numbers)}")
