########################################
# Name: Reagan
# Collaborators (if any): Pen!! and Jimmy
# GenAI Transcript (if any): 
# Estimated time spent (hr): 2
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import  ENGLISH_WORDS, is_english_word, CAPITAL_ENGLISH_WORDS
import random

def wordle():
    # The main function to play the Wordle game.
    gw = WordleGWindow()
    bl = []
    for i in CAPITAL_ENGLISH_WORDS:
        if len(i) == 5:
            bl.append(i)
    word = random.choice(bl)
    print(word)

#Milestone 1
    

    def enter_action():
        entry = assemble_word()
        check_word(entry)
    
    def check_word(word):
        if word in bl:
            gw.show_message("correct", color = "black")
        else:
            gw.show_message("Not in word list", color = "black")

    def assemble_word():
        guess = ""
        for i in range(N_COLS):
            L1 = gw.get_square_letter(gw.get_current_row(), i)
            guess = guess + L1
        return(guess)
    
    gw.add_enter_listener(enter_action)

    check_word(enter_action())




# Startup boilerplate
if __name__ == "__main__":
    wordle()
