import random

def play_game():
    # 1. Introducing the List
    options = ["rock", "paper", "scissors"]
    
    # 2. Setting up the Score Tracker (State Management)
    user_score = 0
    computer_score = 0
    winning_score = 3

    print("--- Welcome to the RPS Classroom Arena ---")
    print(f"First to {winning_score} points wins!")

    # 3. The Game Loop
    while user_score < winning_score and computer_score < winning_score:
        print(f"\nScore: Your score: {user_score} - Computer score: {computer_score}")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
        # Validation
        if user_choice not in options:
            print("Invalid choice! That turn didn't count.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # 4. Logic Implementation
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print(f"You win this round! {user_choice.capitalize()} beats {computer_choice}.")
            user_score += 1
        else:
            print(f"You lose this round! {computer_choice.capitalize()} beats {user_choice}.")
            computer_score += 1

    # 5. Final Result
    if user_score == winning_score:
        print("\nCONGRATULATIONS! You won the tournament!")
    else:
        print("\nGAME OVER. The computer won this time.")

play_game()
