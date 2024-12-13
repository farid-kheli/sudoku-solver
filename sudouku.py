from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.sudoku.name/")


# a function that get ID of a cell
def GetID(i,j):
    n = (i-1)*9 +j
    return "cell" + str(n)


# a function that get ID of a input cell
def getIDinput(i,j):
    n = (i-1)*9 +j
    return "c" + str(n)



# a function that get value of a cell
def getValue(ID):
    n = driver.find_element(By.ID, ID).find_element(By.TAG_NAME, "input").get_attribute("value")
    if not n:
        n = 0 
    return int(n)


# a function that check if a number n is in a 3x3 square
def exist9x9(n,startI,startJ):
    for i in range(startI,startI+3):
        for j in range(startJ,startJ+3):
            if(getValue(GetID(i,j))==n):
                return True
    return False


# a function that check if a number n is in a row
def existline(n,startI,j):
    for i in range(startI,startI+3):
        if(getValue(GetID(i,j))==n):
            return True
    return False


def extract_sudoku():
    grid = []
    for i in range(1, 10):
        row = []
        for j in range(1, 10):
            value = getValue(GetID(i, j))
            row.append(value)
        grid.append(row)
    return grid

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True
# a function that solve the sudoku
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def fill_sudoku(board):
    for i in range(1, 10):
        for j in range(1, 10):
            if getValue(GetID(i, j)) == 0:
                input_id = getIDinput(i, j)
                driver.find_element(By.ID, input_id).send_keys(str(board[i-1][j-1]))


grid = extract_sudoku()
if solve_sudoku(grid):
    fill_sudoku(grid)
else:
    print("No solution exists")


time.sleep(20)