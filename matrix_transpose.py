def transpose(matrix):
      """Return the transpose of a 2-D matrix.

          Args:
                  matrix: List of lists (rows x cols).

                      Returns:
                              Transposed matrix as a list of lists (cols x rows).
                                  """
      if not matrix or not matrix[0]:
                return []
            rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def print_matrix(matrix, label=""):
      """Pretty-print a 2-D matrix.

          Args:
                  matrix: List of lists.
                          label:  Optional label to print above the matrix.
                              """
    if label:
              print(label)
          for row in matrix:
                    print("  " + "  ".join(f"{v:>4}" for v in row))
                print()


if __name__ == "__main__":
      rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
              row = list(map(int, input(f"Row {i + 1} ({cols} values): ").split()))
              matrix.append(row)
          print_matrix(matrix, "Original matrix:")
    print_matrix(transpose(matrix), "Transposed matrix:")
