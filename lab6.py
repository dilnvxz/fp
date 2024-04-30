import tkinter as tk
import random
from rx import Observable
from rx.subject import BehaviorSubject

#diko
def get_computer_choice():
    return random.choice(['к', 'н', 'б'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'к' and computer_choice == 'н') or (user_choice == 'н' and computer_choice == 'б') or (user_choice == 'б' and computer_choice == 'к'):
        return "Поздравляем! Вы выиграли!"
    else:
        return "К сожалению, вы проиграли."

def play_game(user_choice, result_text, computer_choice_label):
    computer_choice = get_computer_choice()
    result_text.set(determine_winner(user_choice, computer_choice))
    computer_choice_label.config(text="Компьютер выбрал: " + computer_choice.upper())

def update_user_choice(choice, user_choice_text):
    user_choice_text.on_next(choice)

root = tk.Tk()
root.title("Камень, ножницы, бумага")

user_choice_text = BehaviorSubject("")
result_text = tk.StringVar()

user_choice_label = tk.Label(root, textvariable=user_choice_text, font=('Helvetica', 16))
user_choice_label.pack()

choices_frame = tk.Frame(root)
choices_frame.pack(pady=10)

rock_button = tk.Button(choices_frame, text="Камень", command=lambda: update_user_choice("к", user_choice_text))
rock_button.grid(row=0, column=0, padx=10)

scissors_button = tk.Button(choices_frame, text="Ножницы", command=lambda: update_user_choice("н", user_choice_text))
scissors_button.grid(row=0, column=1, padx=10)

paper_button = tk.Button(choices_frame, text="Бумага", command=lambda: update_user_choice("б", user_choice_text))
paper_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, textvariable=result_text, font=('Helvetica', 16))
result_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="", font=('Helvetica', 16))
computer_choice_label.pack()

user_choice_text.subscribe(lambda choice: play_game(choice, result_text, computer_choice_label))

root.mainloop()
