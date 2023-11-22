from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        truth_check = PhotoImage(file='./images/true.png')
        false_x = PhotoImage(file='./images/false.png')

        self.q_score = Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Ariel', 10, 'normal'))
        self.q_score.grid(column=1, row=0)

        self.q_canvas = Canvas(height=250, width=300)
        self.q_canvas.create_text(125, 150, text='', font=('Ariel', 20, 'italic'))
        self.q_canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)

        self.true_button = Button(image=truth_check, pady=20, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_x, pady=20, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()
