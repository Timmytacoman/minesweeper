import pyautogui
import numpy as np

NUM_COLS = 30
NUM_ROWS = 16
BOARD = np.full((NUM_ROWS, NUM_COLS), -1, dtype=np.int)
print(BOARD)
exit()

BOARD_LOC = pyautogui.locateOnScreen('assets/board.png')
SMILE_LOC = pyautogui.locateCenterOnScreen('assets/smile.png')
FIRST_TILE_LOC = pyautogui.locateOnScreen('assets/tile.png')

pyautogui.moveTo(FIRST_TILE_LOC[0], FIRST_TILE_LOC[1])


def determine_tile(tile):
    pass


def write_array(board):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            pass
