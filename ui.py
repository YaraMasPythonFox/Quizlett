from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score:0", font=("Arial", 10, "italic"), background=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150, 125,
            width=280,
            text="Some question here.",
            font=("Arial", 20, "italic"),fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image_false = PhotoImage(file="images/false.png")
        image_true = PhotoImage(file="images/true.png")

        self.right_button = Button(image=image_true, command=self.press_true_button)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=image_false, command=self.press_false_button)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"Game over. Count of correct answers: {self.quiz.score}/10.")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def press_true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def press_false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)




