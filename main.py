import tkinter
import random
import notes_dict

white_key_dim = {"width":8, "height": 10, "bg": "#f6f6f6", "activebackground":"#dfdfdf"}
black_key_dim = {"width":6, "height": 10, "bg": "#3e3e3e", "activebackground":"#101010"}
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
note_names = notes_dict.note_names_dict

total = 0				#Track total number of guesses made
right_guesses = 0		#Track total correct guesses
current_note = ''		#Track current piano note randomly picked by random module
start_clicked = False 	#start_clicked is used to keep piano keys disabled unless start is pressed

def update_note():
    """Randomly select one note and update the note label and score"""
    global current_note
    current_note = random.choice(list(note_names.keys()))
    note_lbl.config(text = current_note)
    score_lbl.config(text = f'{right_guesses}/{total}')

def start_game():
    """Starts/Restarts the game by resetting the score values"""
    global total
    global right_guesses
    global current_note
    global start_clicked
    total = 0
    start_clicked = True
    right_guesses = 0
    start_btn.config(text = 'Restart')
    update_note()

def button_click(key_pressed):
    global total
    global right_guesses
    global current_note
    #start_clicked is used to keep piano keys disabled unless start is pressed
    if(start_clicked):
        total += 1
        #if(current_note == key_pressed):
        if(current_note in note_names[key_pressed]):
            right_guesses += 1
            score_lbl.config(bg = '#749F82')
        else:
            score_lbl.config(bg = '#FF7D7D')
        score_lbl.config(text = f'{right_guesses}/{total}')
        update_note()

win = tkinter.Tk()
win.config(padx = 50, pady = 50, bg = '#F8FFDB')
win.title("Piano Notes Trainer")
win.resizable(False, False)

start_btn = tkinter.Button()
start_btn.config(text = 'Start', command = start_game, font = ('Arial', 16), pady = 10, bg = '#9F8772', fg = '#F8FFDB',  highlightthickness = 0, bd = 0)
start_btn.grid(row = 0, column = 0, columnspan = 14, sticky = 'ewsn', pady = 1)

note_lbl = tkinter.Label()
note_lbl.config(text = 'Welcome', font = ('Arial', 20), pady = 10, bg = '#9F8772', fg = '#F8FFDB')
note_lbl.grid(row = 1, column = 0, columnspan = 11, sticky = 'ewsn', padx = 1, pady = (0, 5))

score_lbl = tkinter.Label()
score_lbl.config(text = '0/0', font = ('Arial', 20), pady = 10, bg = '#749F82', fg = '#F8FFDB')
score_lbl.grid(row = 1, column = 11, columnspan = 3, sticky = 'ewsn', pady = (0, 5))

btn_c = tkinter.Button()
btn_c.config(white_key_dim, command = lambda: button_click("C"))
btn_c.grid(row = 3, column = 0, columnspan = 2)

btn_d = tkinter.Button()
btn_d.config(white_key_dim, command = lambda: button_click("D"))
btn_d.grid(row = 3, column = 2, columnspan = 2)

btn_e = tkinter.Button()
btn_e.config(white_key_dim, command = lambda: button_click("E"))
btn_e.grid(row = 3, column = 4, columnspan = 2)

btn_f = tkinter.Button()
btn_f.config(white_key_dim, command = lambda: button_click("F"))
btn_f.grid(row = 3, column = 6, columnspan = 2)

btn_g = tkinter.Button()
btn_g.config(white_key_dim, command = lambda: button_click("G"))
btn_g.grid(row = 3, column = 8, columnspan = 2)

btn_a = tkinter.Button()
btn_a.config(white_key_dim, command = lambda: button_click("A"))
btn_a.grid(row = 3, column = 10, columnspan = 2)

btn_b = tkinter.Button()
btn_b.config(white_key_dim, command = lambda: button_click("B"))
btn_b.grid(row = 3, column = 12, columnspan = 2)

btn_c_s = tkinter.Button()
btn_c_s.config(black_key_dim, command = lambda: button_click("C#"))
btn_c_s.grid(row = 2, column = 1, columnspan = 2)

btn_d_s = tkinter.Button()
btn_d_s.config(black_key_dim, command = lambda: button_click("D#"))
btn_d_s.grid(row = 2, column = 3, columnspan = 2)

btn_f_s = tkinter.Button()
btn_f_s.config(black_key_dim, command = lambda: button_click("F#"))
btn_f_s.grid(row = 2, column = 7, columnspan = 2)

btn_g_s = tkinter.Button()
btn_g_s.config(black_key_dim, command = lambda: button_click("G#"))
btn_g_s.grid(row = 2, column = 9, columnspan = 2)

btn_a_s = tkinter.Button()
btn_a_s.config(black_key_dim, command = lambda: button_click("A#"))
btn_a_s.grid(row = 2, column = 11, columnspan = 2)

win.mainloop()