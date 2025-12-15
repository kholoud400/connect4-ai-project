import tkinter as tk
from game import ConnectFourGame
from constants import ROWS, COLS, PLAYER, AI, EMPTY

CELL_SIZE = 80
PADDING = 5

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.game = ConnectFourGame()

        self.canvas_width = COLS * CELL_SIZE
        self.canvas_height = ROWS * CELL_SIZE

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="blue")
        self.canvas.pack(padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.click)

        # Frame للأزرار
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        # زرار Restart باللون الأخضر
        restart_btn = tk.Button(btn_frame, text="Restart", bg="green", fg="white",
                                font=("Arial", 12, "bold"), command=self.restart_game)
        restart_btn.pack(side="left", padx=5)

        # زرار Play Again باللون برتقالي
        play_btn = tk.Button(btn_frame, text="Play Again", bg="purple", fg="white",
                            font=("Arial", 12, "bold"), command=self.play_again)
        play_btn.pack(side="left", padx=5)

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x1 = c * CELL_SIZE + PADDING
                y1 = r * CELL_SIZE + PADDING
                x2 = (c+1) * CELL_SIZE - PADDING
                y2 = (r+1) * CELL_SIZE - PADDING
                piece = self.game.board.board[r][c]
                color = "white"
                if piece == PLAYER:
                    color = "red"
                elif piece == AI:
                    color = "yellow"
                self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

    def click(self, event):
        if self.game.game_over:
            return
        col = event.x // CELL_SIZE
        if self.game.player_move(col):
            self.draw_board()
            if self.game.game_over:
                self.show_message("You Win!" if self.game.winner == PLAYER else "AI Wins!" if self.game.winner == AI else "Draw")
                return
            self.root.after(300, self.ai_turn)

    def ai_turn(self):
        self.game.ai_move()
        self.draw_board()
        if self.game.game_over:
            self.show_message("You Win!" if self.game.winner == PLAYER else "You Lose!" if self.game.winner == AI else "Draw")

    def restart_game(self):
        self.game.restart()
        self.draw_board()

    def play_again(self):
        self.restart_game()

    def show_message(self, msg):
        top = tk.Toplevel(self.root)
        top.title("Game Over")
        tk.Label(top, text=msg, font=("Arial", 16)).pack(padx=20, pady=20)
        tk.Button(top, text="OK", bg="purple", fg="white", font=("Arial", 12, "bold"),
                command=top.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ConnectFourGUI(root)
    root.mainloop()