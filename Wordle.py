
########################################
# Name:Reagan
# Collaborators (if any): Pen, Jimmy, Jace, the Quad, Kara
# Estimated time spent (hr): 7.5 AT LEAST
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import CAPITAL_ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random

gw=WordleGWindow()

def wordle():
    """ The main function to play the Wordle game. """   
    gw = WordleGWindow()

    bl = []
    for i in CAPITAL_ENGLISH_WORDS: 
        if len(i) == 5:
            bl.append(i)
    wordleword = random.choice(bl)  
    print(wordleword) 

    def enter_action():
        """ What should happen when the RETURN or ENTER key is pressed. """
        word = ""
        for i in range(N_COLS):
            L1 = gw.get_square_letter(gw.get_current_row(),i)
            word = word + L1
        
        if word in bl:
            gw.show_message(word, color = "Green") 
            color_letters(word, wordleword)
        else:
            gw.show_message("Not in word list", color = "Red")
    
    def color_letters(word, wordleword):
        available_letters = list(wordleword) 
        yellow_counter = [0] * 5
        answer_counter = [] 
        row = gw.get_current_row()
        for i in available_letters:
            answer_counter += [available_letters.count(i)]
        print(answer_counter)
        row = gw.get_current_row()
        for col in range(N_COLS):
            if word[col] == available_letters[col]:
                gw.set_square_color(row, col, color = CORRECT_COLOR)
                key_color(word[col], CORRECT_COLOR)
                available_letters[col] = ""
            else:
                gw.set_square_color(row, col, color = MISSING_COLOR)
                key_color(word[col], MISSING_COLOR)
        for col in range(N_COLS):
            if word[col] in available_letters and yellow_counter[available_letters.index(word[col])] < answer_counter[available_letters.index(word[col])]:
                gw.set_square_color(row, col, color = PRESENT_COLOR)
                key_color(word[col], PRESENT_COLOR)
                index = available_letters.index(word[col])
                yellow_counter[index] += 1 
        
    def key_color(letter, color):
        if((color == PRESENT_COLOR or color == MISSING_COLOR) and gw.get_key_color(letter) == CORRECT_COLOR):
            return
        gw.set_key_color(letter,color)

    def move_next_row(): 
        word = ""
        for i in range(len(wordleword)):
            word += str(gw.get_square_letter(gw.get_current_row(), i))
        if word not in bl:
            return
        elif word == wordleword:
            gw.show_message("You guessed it!!", color = "Purple")
        elif gw.get_current_row() >= N_ROWS - 1:
            gw.show_message("You lost.", color = "Red")
        else:
            gw.set_current_row(gw.get_current_row() + 1)

 

    gw.show_message("Welcome to Wordle!", color = "White")
    gw.add_enter_listener(enter_action)
    gw.add_enter_listener(move_next_row)



# Startup boilerplate
if __name__ == "__main__":
    wordle()
