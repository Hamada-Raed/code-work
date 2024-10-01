import tkinter as tk 
import random 

BALL_SiZE = 30 
SCORE_INCREMENT = 10 
GAME_DURATION = 30 

class BallClikerGame: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("BALL CLICK GAME")
        self.canva = tk.Canvas(self.root, width = 500, height = 400, bg = "white")
        self.canva.pack()
        self.score = 0
        self.time_remaining = GAME_DURATION 
        self.score_label = tk.Label(self.root, text =f"Score: {self.score}")
        self.score_label.pack() 
        self.game_runnung = True
        self.update_game() 
        self.root.after(GAME_DURATION * 1000, self.end_game)
        
    def create_ball(self): 
        x1 = random.randint(0, 470)
        y1 = random.randint(0, 370)
        x2 = x1 + BALL_SiZE 
        y2 = y1 + BALL_SiZE 
        ball = self.canva.create_oval(x1,y1,x2,y2, fill = 'blue', outline = 'black', tags = 'ball')
        self.canva.tag_bind(ball, "<Button-1>", self.on_ball_click)
        
    def on_ball_click(self, event): 
        self.canva,delete("current")
        self.score  += SCORE_INCREMENT
        self.score_label.config(text=f"Score: {self.score}")
        
    def update_game(self): 
        if self.game_runnung: 
            self.time_remaining -= 1
            self.timer_label.config(text = f" Time Left: {self.time_remaining} s")
            self.create_ball()
            self.root.after(1000, self.update_game)
            
    def end_game(self):
        self.game_runnung = False
        self.canva.delete('all')
        self.canva.create_text (250, 200, text=f"Game Over! Final Score: {self.score}, font =('Helvetica', 16)" )
        
if __name__ == "__main__": 
    root = tk.Tk()
    game = BallClikerGame(root) 
    root.mainloop()
        
        
        