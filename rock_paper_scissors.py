rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Welcome to Francine's Rock, Paper, and Scissors game!")
user_option = int(input("To compete with Francine, enter 0 for rock, 1 for paper, and 2 for scissors!\n"))

if user_option == 0:
    print(f"You chose: {rock}")
elif user_option == 1:
    print(f"You chose: {paper}")
elif user_option == 2:
    print(f"You chose: {scissors}")
else:
    print("Please pick from the choices.")

computer_choice = [rock, paper, scissors]
computer_option = random.randint(0,2)
print(f"Francine chose: {computer_choice[computer_option]}")

if user_option == computer_option:
    print("It's a draw!")
elif user_option == 0 and computer_option == 2:
    print("You win! You beat Francine.")
elif user_option == 2 and computer_option == 1:
    print("You win! You beat Francine.")
elif user_option == 1 and computer_option == 0:
    print("You win! You beat Francine.")
else:
    print("You lost. Francine wins.")
