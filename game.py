#Task 3 
#ROCK,PAPER,SCISSORS GAME
import tkinter as tk
from random import choice
class RockPaperScissors:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("300x200")
        self.player_score=0
        self.computer_score=0
        self.player_score_label=tk.Label(self.window,text="Player Score: 0",font=("Arial", 12))
        self.player_score_label.pack()
        self.computer_score_label=tk.Label(self.window,text="Computer Score: 0",font=("Arial", 12))
        self.computer_score_label.pack()
        self.result_label=tk.Label(self.window,text="",font=("Arial", 12))
        self.result_label.pack()
        self.rock_button=tk.Button(self.window,text="Rock",command=self.rock,font=("Arial", 12))
        self.rock_button.pack()
        self.paper_button=tk.Button(self.window,text="Paper",command=self.paper,font=("Arial", 12))
        self.paper_button.pack()
        self.scissors_button=tk.Button(self.window,text="Scissors",command=self.scissors,font=("Arial", 12))
        self.scissors_button.pack()
    def computer_choice(self):
        return choice(["rock", "paper", "scissors"])
    def rock(self):
        computer=self.computer_choice()
        if computer=="rock":
            self.result_label['text']="Tie!!"
        elif computer=="paper":
            self.computer_score+=1
            self.computer_score_label['text']=f"Computer Score: {self.computer_score}"
            self.result_label['text']="Paper covers rock! Computer wins!"
        else:
            self.player_score+=1
            self.player_score_label['text']=f"Player Score: {self.player_score}"
            self.result_label['text']="Rock smashes scissors! Player wins!"
    def paper(self):
        computer=self.computer_choice()
        if computer=="paper":
            self.result_label['text']="Tie!!"
        elif computer=="rock":
            self.player_score+=1
            self.player_score_label['text']=f"Player Score: {self.player_score}"
            self.result_label['text']="Paper covers rock! Player wins!"
        else:
            self.computer_score+=1
            self.computer_score_label['text']=f"Computer Score: {self.computer_score}"
            self.result_label['text']="Scissors cuts paper! Computer wins!"
    def scissors(self):
        computer=self.computer_choice()
        if computer=="scissors":
            self.result_label['text']="Tie!!"
        elif computer=="paper":
            self.player_score+=1
            self.player_score_label['text']=f"Player Score: {self.player_score}"
            self.result_label['text']="Scissors cuts paper! Player wins!"
        else:
            self.computer_score+=1
            self.computer_score_label['text']=f"Computer Score: {self.computer_score}"
            self.result_label['text']="Rock smashes scissors! Computer wins!"
    def run(self):
        self.window.mainloop()
if __name__=="__main__":
    game = RockPaperScissors()
    game.run()
