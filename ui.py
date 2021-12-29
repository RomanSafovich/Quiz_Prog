from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="here will appear text",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))

        true_img = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)
        false_img = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the queiz.")
            self.button_false.configure(state="disabled")
            self.button_true.configure(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
