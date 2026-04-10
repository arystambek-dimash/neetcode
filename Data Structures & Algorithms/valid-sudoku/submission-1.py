class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #box checker
        boxes = [[[] for _ in range(3)] for _ in range(9)]
        for i in range(0,9):
            box_row = 0
            for j in range(0, 9):
                if j != 0 and j % 3 == 0:
                    box_row+=1
                box_col= i // 3
                if board[i][j] in boxes[box_col][box_row]:
                    return False
                if board[i][j].isdigit():
                    boxes[box_col][box_row].append(board[i][j])
        formatted = [[] for _ in range(9)]
        for col in range(0,9):
            for row in range(0,9):
                if board[col][row] in formatted[col]:
                    return False
                if board[col][row].isdigit():
                    formatted[col].append(board[col][row])
        
        formatted = [[] for _ in range(9)]
        for col in range(0,9):
            for row in range(0,9):
                print(board[row][col], formatted[col])
                if board[row][col] in formatted[col]:
                    return False
                if board[row][col].isdigit():
                    formatted[col].append(board[row][col])
        return True
        