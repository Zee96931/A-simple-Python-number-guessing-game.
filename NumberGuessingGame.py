import random

print("🎮 Welcome to Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("Can you guess it in 7 tries? 🤔")

# Step 1: Computer chooses random number
secret_number = random.randint(1, 100)

# Step 2: Give user 7 attempts
attempts = 7

for i in range(attempts):
    guess = int(input(f"\nAttempt {i+1}/{attempts} - Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try a bigger number.")
    else:
        print("📈 Too high! Try a smaller number.")

# Step 3: If user fails after all attempts
else:
    print(f"❌ Sorry, you ran out of attempts. The number was {secret_number}.")
