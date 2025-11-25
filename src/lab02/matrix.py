def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    if (
        isinstance(mat, list)
        and all(isinstance(row, list) for row in mat)
        and all(isinstance(item, (int, float)) for row in mat for item in row)
    ):
        row_lengths = [len(str(row)) for row in mat]
        if len(set(row_lengths)) != 1:
            return "ValueError"

        return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    if (
        isinstance(mat, list)
        and all(isinstance(row, list) for row in mat)
        and all(isinstance(item, (int, float)) for row in mat for item in row)
    ):
        row_lengths = [len(row) for row in mat]
        if len(set(row_lengths)) != 1:
            return "ValueError"
        return [sum(item) for item in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    if (
        isinstance(mat, list)
        and all(isinstance(row, list) for row in mat)
        and all(isinstance(item, (int, float)) for row in mat for item in row)
    ):
        row_lengths = [len(row) for row in mat]
        if len(set(row_lengths)) != 1:
            return "ValueError"
    result = []
    for col_index in range(len(mat[0])):
        sum_col = 0
        for row in mat:
            sum_col += row[col_index]
        result.append(sum_col)
    return result


print(("transpose"))
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print()
print("row_sums")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print()
print("col_sums")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
