from dataclasses import dataclass
@dataclass
class Matrix:
    matrix: list
    rows: int
    columns: int

    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __iter__(self):
        return iter(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __str__(self):
        return f"{self.matrix}"

    def __repr__(self):
        return f"{self.matrix}"

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.columns != other.columns:
                raise ValueError("Matrices must have the same dimensions")
            return Matrix(
                [
                    [
                        self.matrix[i][j] + other.matrix[i][j]
                        for j in range(self.columns)
                    ]
                    for i in range(self.rows)
                ],
                self.rows,
                self.columns,
            )
        else:
            return Matrix(
                [
                    [self.matrix[i][j] + other for j in range(self.columns)]
                    for i in range(self.rows)
                ],
                self.rows,
                self.columns,
            )

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.columns != other.columns:
                raise ValueError("Matrices must have the same dimensions")
            return Matrix(
                [
                    [
                        self.matrix[i][j] - other.matrix[i][j]
                        for j in range(self.columns)
                    ]
                    for i in range(self.rows)
                ],
                self.rows,
                self.columns,
            )
        else:
            return Matrix(
                [
                    [self.matrix[i][j] - other for j in range(self.columns)]
                    for i in range(self.rows)
                ],
                self.rows,
                self.columns,
            )

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError(
                    "The number of columns of the first matrix must be equal to the number of rows of the second matrix"
                )
            return Matrix([[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)) for j in range(other.columns)] for i in range(self.rows)], self.rows, other.columns)

    # Support the @ operator for matrix multiplication
    __matmul__ = __mul__