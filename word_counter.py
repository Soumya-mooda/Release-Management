def count_words(text):
      """Count the frequency of each word in a text (case-insensitive).

          Args:
                  text: Input string.

                      Returns:
                              Dictionary mapping word -> frequency, sorted by frequency descending.
                                  """
      words = text.lower().split()
      freq = {}
      for word in words:
                word = word.strip(".,!?;:\"'")
                if word:
                              freq[word] = freq.get(word, 0) + 1
                      return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


def display_word_count(freq):
      """Display word frequency table.

          Args:
                  freq: Dictionary of word frequencies.
                      """
      print(f"{'Word':<20} {'Count':>5}")
      print("-" * 26)
      for word, count in freq.items():
                print(f"{word:<20} {count:>5}")


if __name__ == "__main__":
      text = input("Enter text: ")
      freq = count_words(text)
      print(f"\nTotal unique words: {len(freq)}")
      display_word_count(freq)
