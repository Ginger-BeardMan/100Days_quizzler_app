from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        truth_check = PhotoImage(file='./images/true.png')
        false_x = PhotoImage(file='./images/false.png')

        self.q_score = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=('Ariel', 10, 'normal'))
        self.q_score.grid(column=1, row=0)

        self.q_canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.q_canvas.create_text(150, 125, text='Some Text', font=('Ariel', 20, 'italic'),
                                                       fill=THEME_COLOR, width=280)
        self.q_canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)

        self.true_button = Button(image=truth_check, pady=20, highlightthickness=0, command=self.answer_is_true)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_x, pady=20, highlightthickness=0, command=self.answer_is_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.q_canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.q_canvas.itemconfig(self.question_text, text=q_text)
            self.q_score.config(text=f'Score: {self.quiz.score}')
        else:
            self.q_canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def answer_is_true(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def answer_is_false(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.q_canvas.configure(bg='green')
        else:
            self.q_canvas.configure(bg='red')
        self.window.after(1000, self.get_next_question)
