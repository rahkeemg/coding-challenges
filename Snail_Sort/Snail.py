class Snail:

    def __init__(self, n_array=None):
        self.__snail_map = n_array

    def set_map(self, snail_map=None):
        self.__snail_map = snail_map

    def travel_map(self, n_array=None):

        if self.__snail_map == None or n_array:
            self.__snail_map = n_array

        row, col, mov = 0, 0, 0
        list, n = [], len(self.__snail_map)
        direction = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}

        if len(self.__snail_map) <= 1:
            return self.__snail_map[0]

        while len(list) < n**2:
            if mov % len(direction) == 0:  # Right
                if (row, col) not in list:
                    list.append((row, col))
                col += 1
                if col >= n or (row, col) in list:
                    mov += 1
                    col -= 1
                    row += 1
            elif mov % len(direction) == 1:  # Down
                if (row, col) not in list:
                    list.append((row, col))
                row += 1
                if row >= n or (row, col) in list:
                    mov += 1
                    row -= 1
                    col -= 1
            elif mov % len(direction) == 2:  # Left
                if (row, col) not in list:
                    list.append((row, col))
                col -= 1
                if col < 0 or (row, col) in list:
                    mov += 1
                    col += 1
                    row -= 1
            else:  # Up
                if (row, col) not in list:
                    list.append((row, col))
                row -= 1
                if row < 0 or (row, col) in list:
                    mov += 1
                    row += 1
                    col += 1
        return [self.__snail_map[item[0]][item[1]] for item in list]