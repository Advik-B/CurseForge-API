from testMatrix import Matrix

m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
n = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 3, 3)

m *= 2
print(m)