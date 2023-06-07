from random import sample
from itertools import product


class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

    def open(self):
        self.fl_open = True

    def update_around_mines(self):
        self.around_mines += 1

    def update_mine(self):
        self.mine = True


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        # corner columns and rows for correct count of around mines
        self.pole = [[Cell(0, False) for i in range(N + 2)] for i in range(N + 2)]
        self.init()

    def init(self):
        # locate mines
        columns = [i for i in range(1, self.N + 1)]
        rows = [i for i in range(1, self.N + 1)]
        mines = sample([*product(rows, columns)], self.M)
        for loc in mines:
            self.pole[loc[0]][loc[1]].update_mine()
        # update around mines
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                check_box = [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                    (i - 1, j - 1),
                    (i - 1, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j + 1)
                ]
                for loc in check_box:
                    if self.pole[loc[0]][loc[1]].mine:
                        self.pole[i][j].update_around_mines()
        # clean pole
        self.pole = self.pole[1:-1]
        for row in self.pole:
            del row[0]
            del row[-1]

    def select_cell(self, loc):
        self.pole[loc[0]][loc[1]].open()
        if self.pole[loc[0]][loc[1]].mine:
            print("This cell is a mine. Game lost.")
            self.show_answers()
        else:
            self.show()

    def show(self):
        table = ['\n']
        for row in self.pole:
            for cell in row:
                if cell.fl_open:
                    table.append(str(cell.around_mines))
                else:
                    table.append('#')
            table.append('\n')
        print(" ".join(table))

    def show_answers(self):
        table = ['\n']
        for row in self.pole:
            for cell in row:
                if not cell.mine:
                    table.append(str(cell.around_mines))
                else:
                    table.append('*')
            table.append('\n')
        print(" ".join(table))


gm = GamePole(4, 8)
gm.show()


def main():
    print('Session started')


if __name__ == '__main__':
    main()