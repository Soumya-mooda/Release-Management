from collections import Counter


def is_anagram(s1, s2):
      """Check if two strings are anagrams (case-insensitive, ignores spaces).

          Args:
                  s1: First string.
                          s2: Second string.

                              Returns:
                                      True if s1 and s2 are anagrams, False otherwise.
                                          """
      clean = lambda s: Counter(ch.lower() for ch in s if ch.isalpha())
      return clean(s1) == clean(s2)


def find_anagram_groups(words):
      """Group a list of words by their anagram signature.

          Args:
                  words: List of strings.

                      Returns:
                              List of groups, each group being a list of anagrams.
                                  """
      groups = {}
      for word in words:
                key = "".join(sorted(word.lower()))
                groups.setdefault(key, []).append(word)
            return [g for g in groups.values() if len(g) > 1]


if __name__ == "__main__":
      s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    if is_anagram(s1, s2):
              print(f"'{s1}' and '{s2}' ARE anagrams.")
else:
        print(f"'{s1}' and '{s2}' are NOT anagrams.")
