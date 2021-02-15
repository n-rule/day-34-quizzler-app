from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"




class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title('Quizzler')

        self.score_label = Label(text='Score: ', bg=THEME_COLOR, fg='white', font=20)
        self.score_label.grid(column='1', row='0', padx='10', pady='10')

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column='0', row='1', columnspan='2')

        self.question_text = self.canvas.create_text(150, 125, text="Some stupid text", width=250,
                                                     font=("Arial", 20, "italic"))


        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column='0', row='3', padx='20', pady='20')

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column='1', row='3', padx='20', pady='20')

        self.get_next_question()

        self.window.mainloop()



    def get_next_question(self):

        self.canvas.config(bg='white')
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='THE END')


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, right_answer):
        if right_answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1111, func=self.get_next_question)






