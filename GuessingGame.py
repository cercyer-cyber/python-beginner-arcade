import random
secret = random.randint(0,20)
tries = 0
guess = -1
while guess != secret:
    guess = int(input("Enter your guess: "))
    tries += 1
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")

print(f"Congratulations! You guessed the number in {tries} tries.")