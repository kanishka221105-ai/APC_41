#17.	Create two 3 × 3 matrices using nested lists and perform matrix addition.
mat1 = [[1, 2, 3],
        [5, 6, 7],
        [8, 9, 10]]

mat2 = [[2, 3, 4],
        [6, 7, 3],
        [7, 5, 3]]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

print("Matrix Addition:")
for row in result:
    print(row)

    