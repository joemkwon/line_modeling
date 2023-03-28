# ======================= World State =======================
# As of now: DO NOT ALLOW DROPPING ITEMS INFRONT OF TASK_PERFORMING CELL
MAP = 'new_maybe_5_0cut'

CACTUS = [(9,11),(9,10)]
PALM_TREES = [(6,7),(6,8),(6,9),(6,10),(6,11),(5,11),(5,10),(5,9),(8,7),(8,8),(8,9),(8,10),(8,11)]
ROCKS = [(9,9)]
RIVER_WATER = []
STILL_WATER = [(7,8),(7,9),(7,10),(7,11),(7,12),(7,13)]
WELL = []
BARREL = [(4,0),(5,0),(6,0),(7,0),(8,0),(9,0)]

all_possible_cells = [
    (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9), (0,10), (0,11), (0,12), (0,13),
    (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12), (1,13),
    (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9), (2,10), (2,11), (2,12), (2,13),
    (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9), (3,10), (3,11), (3,12), (3,13),
    (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9), (4,10), (4,11), (4,12), (4,13),
    (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,10), (5,11), (5,12), (5,13),
    (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9), (6,10), (6,11), (6,12), (6,13),
    (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9), (7,10), (7,11), (7,12), (7,13),
    (8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9), (8,10), (8,11), (8,12), (8,13),
    (9,0), (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9), (9,10), (9,11), (9,12), (9,13),
    (10,0), (10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7), (10,8), (10,9), (10,10), (10,11), (10,12), (10,13),
    (11,0), (11,1), (11,2), (11,3), (11,4), (11,5), (11,6), (11,7), (11,8), (11,9), (11,10), (11,11), (11,12), (11,13),
    (12,0), (12,1), (12,2), (12,3), (12,4), (12,5), (12,6), (12,7), (12,8), (12,9), (12,10), (12,11), (12,12), (12,13),
    (13,0), (13,1), (13,2), (13,3), (13,4), (13,5), (13,6), (13,7), (13,8), (13,9), (13,10), (13,11), (13,12), (13,13)
]


invalid_movement_cells = CACTUS + PALM_TREES + ROCKS + RIVER_WATER + STILL_WATER + WELL + BARREL
    #these are all possible cells minus all the objects listed above
valid_movement_cells = [x for x in all_possible_cells if x not in invalid_movement_cells]

#customize, or randomize spawn between all the valid movement cells, checking to make sure it's 
#not a duplicated location

HOLDING_TIMES = [
    [7,8,9,15],
    [13,14,15,21],
    [19,20,21,27],
    [25,26,27,33],
    [31,32,33,39],
    [37,38,39,45],
    [43,44,45,51], 
    [49,50,51,57]
]

EP_DATA = {1:{1:{'coords': (3,5),'holding': False,'orientation':'L','completed': False},2:{'coords': (3,6),'holding': False,'orientation':'L','completed': False},3:{'coords': (3,7),'holding': False,'orientation':'L','completed': False},4:{'coords': (3,8),'holding': False,'orientation':'L','completed': False},5:{'coords': (3,9),'holding': False,'orientation':'L','completed': False},6:{'coords': (3,10),'holding': False,'orientation':'L','completed': False},7:{'coords': (3,11),'holding': False,'orientation':'L','completed': False},8:{'coords': (3,12),'holding': False,'orientation':'L','completed': False},},2:{1:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},2:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},5:{'coords': (3,8),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,9),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,10),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,11),'holding': False,'orientation':'D','completed': False},},3:{1:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},2:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,8),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,9),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,10),'holding': False,'orientation':'D','completed': False},},4:{1:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},2:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},3:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,8),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,9),'holding': False,'orientation':'D','completed': False},},5:{1:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},2:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},3:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,8),'holding': False,'orientation':'D','completed': False},},6:{1:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},2:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},},7:{1:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},2:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},},8:{1:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},2:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},},9:{1:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},2:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},},10:{1:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},2:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},},11:{1:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},2:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,7),'holding': False,'orientation':'D','completed': False},},12:{1:{'coords': (7,5),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},},13:{1:{'coords': (7,4),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},},14:{1:{'coords': (7,3),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},},15:{1:{'coords': (7,2),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},},16:{1:{'coords': (7,1),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},},17:{1:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,6),'holding': False,'orientation':'D','completed': False},},18:{1:{'coords': (9,1),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,5),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},},19:{1:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,4),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},},20:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,3),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},},21:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,2),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},},22:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (7,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},},23:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (3,5),'holding': False,'orientation':'D','completed': False},},24:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (9,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,5),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},},25:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,4),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},},26:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,3),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},},27:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,2),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},},28:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (7,1),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},},29:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (4,5),'holding': False,'orientation':'D','completed': False},},30:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,5),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},},31:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,4),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},},32:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,1),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,3),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},},33:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,2),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},},34:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (7,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},},35:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},6:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (5,5),'holding': False,'orientation':'D','completed': False},},36:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,5),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},},37:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,4),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},},38:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,3),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},},39:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,2),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},},40:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (7,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},},41:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,5),'holding': False,'orientation':'D','completed': False},},42:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,5),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},},43:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,4),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},},44:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,3),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},},45:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,2),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},},46:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (7,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},},47:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},8:{'coords': (6,6),'holding': False,'orientation':'D','completed': False},},48:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,5),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},},49:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,4),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},},50:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,3),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},},51:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,2),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},},52:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (7,1),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,7),'holding': False,'orientation':'D','completed': False},},53:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,6),'holding': False,'orientation':'D','completed': False},},54:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,5),'holding': False,'orientation':'D','completed': False},},55:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,4),'holding': False,'orientation':'D','completed': False},},56:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,3),'holding': False,'orientation':'D','completed': False},},57:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,2),'holding': False,'orientation':'D','completed': False},},58:{1:{'coords': (10,0),'holding': False,'orientation':'D','completed': False},2:{'coords': (10,1),'holding': False,'orientation':'D','completed': False},3:{'coords': (3,0),'holding': False,'orientation':'D','completed': False},4:{'coords': (4,1),'holding': False,'orientation':'D','completed': False},5:{'coords': (5,1),'holding': False,'orientation':'D','completed': False},6:{'coords': (8,1),'holding': False,'orientation':'D','completed': False},7:{'coords': (6,1),'holding': False,'orientation':'D','completed': False},8:{'coords': (7,1),'holding': False,'orientation':'D','completed': False}}}


import random
#shuffle players
mapping = random.sample(range(1, 9), 8)
for episode in EP_DATA:
    newDict = {}
    for i in range(1,9):
        newKey = mapping[i-1]
        newDict[newKey] = EP_DATA[episode][i]
    EP_DATA[episode] = newDict
# #shuffle holding times
NEW_HOLDING = []
for i in range(8):
    NEW_HOLDING.append([])
for idx, num in enumerate(mapping):
    NEW_HOLDING[num-1] = HOLDING_TIMES[idx]
HOLDING_TIMES = NEW_HOLDING