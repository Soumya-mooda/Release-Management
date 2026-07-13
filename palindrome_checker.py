def is_palindrome(s):
      """Check if a string is a palindrome (case-insensitive, ignores spaces).

          Args:
                  s: Input string.

                      Returns:
                              True if palindrome, False otherwise.
                                  """
      cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
      return cleaned == cleaned[::-1]


def check_palindromes(words):
      """Check and print palindrome status for a list of strings.

          Args:
                  words: List of strings to check.
                      """
      for word in words:
                status = "Palindrome" if is_palindrome(word) else "Not a palindrome"
                print(f"  '{word}' -> {status}")


if __name__ == "__main__":
      raw = input("Enter words/phrases separated by comma: ")
      items = [item.strip() for item in raw.split(",")]
      check_palindromes(items)
