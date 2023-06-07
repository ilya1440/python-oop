class MaxPooling:
    def __call__(self, matrix):
        self.validate_matrix(matrix)
        self.valid_boundary(matrix)

        result = [[False for i in range(self.row_boundary)] for i in range(self.column_boundary)]
        current_window = []
        for i in range(self.column_boundary):
            for j in range(self.row_boundary):
                for r in range(self.size[0]):
                    for c in range(self.size[1]):
                        current_window.append(matrix[i * self.step[1] + r][j * self.step[0] + c])

                value = max(current_window)
                current_window = []
                result[i][j] = value

        return result

    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def valid_boundary(self, matrix):
        # number of columns in result (number of movements inside initial row)
        row_boundary = (self.rows - self.size[0]) // self.step[0] + 1
        # number of rows in result (number of movements inside initial column)
        column_boundary = (self.columns - self.size[1]) // self.step[1] + 1
        setattr(self, 'row_boundary', row_boundary)
        setattr(self, 'column_boundary', column_boundary)

    def validate_matrix(self, matrix):
        columns = tmp = len(matrix[0])
        rows = 0

        if columns == 0:
            raise ValueError("Неверный формат для первого параметра matrix.")

        for lst in matrix:
            rows += 1
            tmp = 0
            for value in lst:
                tmp += 1
                if not type(value) in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")
            if tmp != columns:
                raise ValueError("Неверный формат для первого параметра matrix.")

        if rows < self.size[0] or columns < self.size[1]:
            raise ValueError("Неверный формат для первого параметра matrix.")

        setattr(self, 'columns', columns)
        setattr(self, 'rows', rows)



