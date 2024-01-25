import random
from tkinter import Tk, Button, Label, StringVar, Entry, Toplevel, PhotoImage

def get_user_choice():
    user_choice = user_input.get().lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        result_var.set("Invalid choice. Please enter Rock, Paper, or Scissors.")
    else:
        result_var.set("")
        play_game(user_choice)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        show_popup("It's a tie!")
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        show_popup("You win!")
    else:
        show_popup("You lose!")

def show_popup(message):
    popup = Toplevel(root)
    popup.title("Game Result")
    popup.geometry("250x100")
    result_label = Label(popup, text=message)
    result_label.pack()
    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

def play_game(user_choice):
    computer_choice = get_computer_choice()
    determine_winner(user_choice, computer_choice)
    result_var.set(f"You chose {user_choice}\nThe computer chose {computer_choice}")
    user_entry.config(state="disabled")
    submit_button.config(state="disabled")

def clear_result_label():
    result_var.set("")
    user_entry.config(state="normal")
    submit_button.config(state="normal")
    user_input.set("")

root = Tk()
root.title("Rock, Paper, Scissors Game")

user_input = StringVar()
user_label = Label(root, text="Enter your choice (Rock, Paper, or Scissors):")
user_label.pack()
user_entry = Entry(root, textvariable=user_input)
user_entry.pack()

submit_button = Button(root, text="Submit", command=get_user_choice)
submit_button.pack()

clear_button = Button(root, text="Play Again", command=clear_result_label)
clear_button.pack()

result_var = StringVar()
result_label = Label(root, textvariable=result_var, font=("Helvetica", 12))
result_label.pack()

root.mainloop()
