import random

def guess_the_number():
    """A fun number guessing game"""
    secret = random.randint(1, 100)
    attempts = 0
    
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("I'm thinking of a number between 1 and 100...")
    
    while True:
        try:
            guess = int(input("\nTake a guess: "))
            attempts += 1
            
            if guess < secret:
                print("📈 Too low! Try higher.")
            elif guess > secret:
                print("📉 Too high! Try lower.")
            else:
                print(f"🎉 You got it! The number was {secret}")
                print(f"⭐ You found it in {attempts} attempts!")
                break
        except ValueError:
            print("❌ Please enter a valid number!")

if __name__ == "__main__":
    guess_the_number()