import tkinter as tk  # 导入 tkinter 库，提供基本的 GUI 组件
from tkinter import messagebox  # 导入 tkinter 的 messagebox，用于显示消息框
import random

def check_winner(board, player):
    # 检查是否有玩家获胜（player = 'X' 或 'O'）
    # 检查行和列
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # 检查对角线
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # 检查棋盘是否已满
    return all(all(cell != ' ' for cell in row) for row in board)

def minimax(board, depth, is_maximizing):
    # 使用 Minimax 算法计算最优移动
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing:
        # AI（'O'）的回合，尝试最大化评估值
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        # 玩家（'X'）的回合，尝试最小化评估值
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    # 查找 AI 的最佳移动
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def make_move(row, col):
    # 玩家落子
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X')
        if check_winner(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            root.quit()
        elif is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            root.quit()
        else:
            ai_move()  # AI 落子
    else:
        messagebox.showerror("Error", "Invalid move")

def ai_move():
    # AI 落子
    row, col = best_move(board)
    board[row][col] = 'O'
    buttons[row][col].config(text='O')
    if check_winner(board, 'O'):
        messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
        root.quit()
    elif is_board_full(board):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        root.quit()

# 创建 tkinter 应用程序
root = tk.Tk()
root.title("Tic-Tac-Toe")

# 初始化棋盘
board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = []

# 创建棋盘按钮
for i in range(3):
    row_buttons = []
    for j in range(3):
        # 创建按钮，并绑定落子事件
        button = tk.Button(root, text=' ', font=('normal', 30), width=5, height=2, command=lambda row=i, col=j: make_move(row, col))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

# 运行 tkinter 应用程序的主循环
root.mainloop()
