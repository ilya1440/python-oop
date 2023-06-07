from random import randint, choice


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        if type(length) != int or length <= 0:
            raise ValueError('Ship length must be positive integer')
        self._length = length
        # 1 - horizontal; 2 - vertical
        # TODO: check for correctness
        self._tp = tp
        self._x = x
        self._y = y
        # ship is movable (if any unit is damaged set to False)
        self._is_move = True
        # 1 - operational unit; 2 - damaged unit
        self._cells = [1] * self._length

    def set_start_coords(self, x, y):
        # TODO: check for type and range
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    # TODO: use this method in the gamepole class
    def move(self, go_flag):
        # TODO: check for flag correctness
        # TODO: check for collision
        # TODO: check for game pole boundaries
        if self._is_move:
            if go_flag == 1:
                if self._tp == 1:
                    self._x += 1
                else:
                    self._y += 1
            else:
                if self._tp == 1:
                    self._x -= 1
                else:
                    self._y -= 1

    @staticmethod
    def get_ship_loc(ship):
        ship_loc = [
            (ship._x + delta, ship._y) if ship._tp == 1
            else (ship._x, ship._y + delta) for delta in range(ship._length)
        ]

        return ship_loc

    def is_collide(self, ship):
        # area occupied by the current ship
        not_valid_area = set()
        ship_loc = self.get_ship_loc(self)
        for loc in ship_loc:
            for i in range(2):
                for j in range(2):
                    not_valid_area.add((loc[0] + i, loc[1] + j))
                    not_valid_area.add((loc[0] - i, loc[1] - j))
                    not_valid_area.add((loc[0] - i, loc[1] + j))
                    not_valid_area.add((loc[0] + i, loc[1] - j))

        # area occupied by another ship
        ship_loc = set(self.get_ship_loc(ship))
        if not not_valid_area.intersection(ship_loc):
            return False
        return True

    def is_out_pole(self, size):
        ship_loc = self.get_ship_loc(self)
        for unit_loc in ship_loc:
            for coord in unit_loc:
                if coord > size - 1:
                    return True
        return False

    def check_index(self, index):
        if type(index) != int or not (0 <= index <= self._length -1):
            raise IndexError('Invalid index for a ship unit')

    def __getitem__(self, item):
        self.check_index(item)
        return self._cells[item]

    def __setitem__(self, key, value):
        self.check_index(key)
        self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        # create ships
        ships = []
        for i in range(3, -1, -1):
            ships.extend(
                [
                    Ship(i + 1, randint(1, 2)) for j in range(4 - i)
                ]
            )
        self._ships = ships

        # locate ships on the gamepole
        # TODO: corner case when there is no space for the current ship
        ships_on_field = []
        available_cells = set((i, j) for i in range(self._size) for j in range(self._size))
        for ship in self._ships:
            finish_flag = False
            # attempt to find right place for a ship on the gamepole
            while not finish_flag:
                cell = choice(list(available_cells))
                ship.set_start_coords(cell[0], cell[1])
                # check for boundaries
                if ship.is_out_pole(self._size):
                    continue

                # check for collision
                collision_flag = False
                for other_ship in ships_on_field:
                    if ship.is_collide(other_ship):
                        collision_flag = True
                        break
                if collision_flag:
                    continue

                # at this point the right cell for the ship is found
                finish_flag = True

            # append current ship to ships on field and update available cells
            ships_on_field.append(ship)
            ship_loc = ship.get_ship_loc(ship)
            for loc in ship_loc:
                for i in range(2):
                    for j in range(2):
                        available_cells.discard((loc[0] + i, loc[1] + j))

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            if ship._is_move:
                x, y = ship.get_start_coords()
                if ship._tp == 1:
                    new_cells = ((x + 1, y), (x - 1, y))
                else:
                    new_cells = ((x, y + 1), (x, y - 1))
                for cell in new_cells:
                    ship.set_start_coords(cell[0], cell[1])
                    if ship.is_out_pole(self._size):
                        ship.set_start_coords(x, y)
                        break

                    for other_ship in self._ships:
                        if other_ship != ship:
                            if ship.is_collide(other_ship):
                                ship.set_start_coords(x, y)
                                break

                    # at this point new cell is found
                    break

    def get_pole(self):
        game_pole = [
            [
                0 for i in range(self._size)
            ] for j in range(self._size)
        ]

        for ship in self._ships:
            ship_loc = [*zip(ship.get_ship_loc(ship), ship._cells)]
            for loc in ship_loc:
                game_pole[loc[0][1]][loc[0][0]] = loc[1]

        return tuple(tuple(row) for row in game_pole)

    def show(self):
        game_pole = self.get_pole()
        table = ['\n']
        for row in game_pole:
            for cell in row:
                table.append(str(cell))
            table.append('\n')
        print(" ".join(table))


ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"


pole_size_8 = GamePole(10)
pole_size_8.init()



















