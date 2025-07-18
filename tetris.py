

class cell:

    def __init__(self, name, xcord, ycord, TAB, RAB, DAB, LAB, TRAB, DRAB, DLAB, TLAB, current_block):
        self.name = name
        self.xcord = xcord
        self.ycord = ycord
        self.tab = TAB
        self.rab = RAB
        self.dab = DAB
        self.lab = LAB
        self.trab =TRAB
        self.drab = DRAB
        self.dlab = DLAB
        self.tlab = TLAB
        self.current_block = current_block

    def change_current(self):
        if self.current_block == '_':
            self.current_block = '#'
        else:
            self.current_block = '_'

class blockseg:

    def __init__(self, xcord, ycord, center, name):
        self.xcord = xcord
        self.ycord = ycord
        self.center = center
        self.name = name

class block:

    def __init__(self, xcord, ycord, shape):
        self.center = blockseg(xcord, ycord, True, "CENTER")
        self.xcord = xcord
        self.ycord = ycord
        if shape == '2X2':
            self.block1 = blockseg(xcord, ycord -1,  False, "BLOCK1")
            self.block2 = blockseg(xcord + 1, ycord, False, "BLOCK2")
            self.block3 = blockseg(xcord + 1, ycord - 1 , False, "BLOCK3")

    def add_block(self):
        for space in test_board_state:
            if space.xcord == self.center.xcord and space.ycord == self.center.ycord:
                space.change_current()
            elif space.xcord == self.block1.xcord and space.ycord == self.block1.ycord:
                space.change_current()
            elif space.xcord == self.block2.xcord and space.ycord == self.block2.ycord:
                space.change_current()
            elif space.xcord == self.block3.xcord and space.ycord == self.block3.ycord:
                space.change_current()

top_left = cell('top_left', 1, 2, 'NONE', 'top_right', 'bottom_left', 'NONE', 'NONE', 'bottom_right', 'NONE', 'NONE', '_')
top_right = cell('top_right', 2, 2, 'NONE', 'NONE', 'bottom_right', 'top_left', 'NONE', 'NONE', 'bottom_left', 'NONE', '_')
bottom_left = cell('bottom_left', 1, 1, 'top_left', 'bottom_right', 'NONE', 'NONE', 'top_right' ,'NONE', 'NONE', 'NONE', '_')
bottom_right = cell('bottom_right', 1, 2, 'top_right', 'NONE', 'NONE', 'bottem_left', 'NONR', 'NONE', 'NONE', 'top_left', '_')

test_board_state = [top_left, top_right, bottom_left, bottom_right]

test_board = f"""
 _ _
|{top_left.current_block}|{top_right.current_block}|
|{bottom_left.current_block}|{bottom_right.current_block}|"""

test_block = block(2, 1, '2X2')

print(test_board)

test_block.add_block()

test_board = f"""
 _ _
|{top_left.current_block}|{top_right.current_block}|
|{bottom_left.current_block}|{bottom_right.current_block}|"""

print(test_board)