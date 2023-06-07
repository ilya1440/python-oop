from random import choice


class Cell:
    def __init__(self, value: int = 0):
        self.value = value

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    DRAW = 100

    def __init__(self):
        self.pole = tuple(tuple(Cell(0) for i in range(3)) for j in range(3))

    @staticmethod
    def check(key):
        for index in key:
            if not isinstance(index, int) or not 0 <= index <= 2:
                raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.check(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.check(key)
        self.pole[key[0]][key[1]].value = value

    def init(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = self.FREE_CELL

    def show(self):
        table = ['\n']
        for row in self.pole:
            for cell in row:
                if cell.value == self.FREE_CELL:
                    table.append(" ")
                elif cell.value == self.HUMAN_X:
                    table.append("X")
                elif cell.value == self.COMPUTER_O:
                    table.append("0")
            table.append('\n')
        print(" ".join(table))

    def human_go(self):
        if self.is_finished():
            print('Game is finished')
        else:
            key_1, key_2 = [*map(int, input().split(','))]
            if self.pole[key_1][key_2]:
                self.pole[key_1][key_2].value = self.HUMAN_X
            else:
                print('Cell Used')

    def computer_go(self):
        if self.is_finished():
            print('Game is finished')
        else:
            open_cells = []
            for i in range(3):
                for j in range(3):
                    if self.pole[i][j]:
                        open_cells.append((i, j))
            key_1, key_2 = choice(open_cells)
            if self.pole[key_1][key_2]:
                self.pole[key_1][key_2].value = self.COMPUTER_O
            else:
                print('Cell Used')

    def is_finished_linear(self, direction):
        # check rows
        draw_flag_general = [False] * 3
        for i in range(3):
            row_result = [0, 'NAN']
            draw_flag = True
            for j in range(3):
                if direction == 'rows':
                    cell = self.pole[i][j]
                else:
                    cell = self.pole[j][i]
                if cell:
                    draw_flag = False
                    break
                if cell.value == self.HUMAN_X:
                    if row_result[1] in ['NAN', self.HUMAN_X]:
                        row_result[0] += 1
                        row_result[1] = self.HUMAN_X
                    else:
                        break
                if cell.value == self.COMPUTER_O:
                    if row_result[1] in ['NAN', self.COMPUTER_O]:
                        row_result[0] += 1
                        row_result[1] = self.COMPUTER_O
                    else:
                        break
            draw_flag_general[i] = draw_flag
            if row_result[0] == 3:
                return row_result[1]
        if all(draw_flag_general):
            return self.DRAW
        else:
            return False

    def is_finished(self):
        diag_result = [0, 'NAN']
        for i in range(3):
            cell = self.pole[i][i]
            if cell:
                break
            if diag_result[1] == 'NAN' or cell.value == diag_result[1]:
                diag_result[0] += 1
                diag_result[1] = cell.value
            else:
                break
        if diag_result[0] == 3:
            return diag_result[1]

        row_result = self.is_finished_linear('rows')
        if row_result:
            return row_result
        else:
            return self.is_finished_linear('cols')

    @property
    def is_human_win(self):
        result = self.is_finished()
        if result and result == self.HUMAN_X:
            return True
        return False

    @property
    def is_computer_win(self):
        result = self.is_finished()
        if result and result == self.COMPUTER_O:
            return True
        return False

    @property
    def is_draw(self):
        result = self.is_finished()
        if result and result == self.DRAW:
            return True
        return False

    def __bool__(self):
        if not self.is_finished():
            return True
        return False


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"



