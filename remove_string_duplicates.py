def remove_duplicates(s):
      """Remove duplicate characters from a string, preserving order.

          Args:
                  s: Input string.

                      Returns:
                              A new string with duplicate characters removed.
                                  """
      seen = set()
      result = []
      for char in s:
                if char not in seen:
                              seen.add(char)
                              result.append(char)
                      return "".join(result)


def remove_duplicates_sorted(s):
      """Remove duplicate characters and return the result sorted.

          Args:
                  s: Input string.

                      Returns:
                              A sorted string with duplicates removed.
                                  """
      return "".join(sorted(set(s)))


if __name__ == "__main__":
      text = input("Enter a string: ")
      print(f"Original string       : {text}")
      print(f"Duplicates removed    : {remove_duplicates(text)}")
      print(f"Duplicates removed (sorted): {remove_duplicates_sorted(text)}")
