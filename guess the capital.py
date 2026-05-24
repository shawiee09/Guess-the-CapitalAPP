import random

# A dictionary mapping countries to their capitals
CAPITAL_POOL = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Egypt": "Cairo",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "India": "New Delhi",
    "Italy": "Rome",
    "Mexico": "Mexico City",
    "South Africa": "Pretoria",
    "Germany": "Berlin",
    "United Kingdom": "London",
    "South Korea": "Seoul",
    "Argentina": "Buenos Aires",
    "Spain": "Madrid"
}

def play_game():
    print("=" * 50)
    print("🌍 WELCOME TO THE GUESS THE CAPITAL GAME! 🌍")
    print("=" * 50)
    print("Type 'quit' at any time to exit the game.\n")

    # Convert dictionary items to a list and shuffle them
    countries = list(CAPITAL_POOL.keys())
    random.shuffle(countries)
    
    score = 0
    streak = 0
    highest_streak = 0
    total_played = 0

    for country in countries:
        correct_capital = CAPITAL_POOL[country]
        total_played += 1
        
        print(f"📍 Question {total_played}: What is the capital of {country}?")
        user_guess = input("Your answer: ").strip()

        # Check if the player wants to quit
        if user_guess.lower() == 'quit':
            total_played -= 1  # Don't count the quit round
            print("\nExiting the game... Thanks for playing!")
            break

        # Validate answer (case-insensitive comparison)
        if user_guess.lower() == correct_capital.lower():
            score += 1
            streak += 1
            if streak > highest_streak:
                highest_streak = streak
            print(f"🎉 Correct! The capital of {country} is {correct_capital}.")
            print(f"🔥 Current Streak: {streak}\n")
        else:
            print(f"❌ Incorrect. The correct capital of {country} is {correct_capital}.")
            print(f"💔 Streak broken!\n")
            streak = 0
            
        print("-" * 40)

    # Game Over Summary Screen
    print("\n🏁 GAME OVER 🏁")
    if total_played > 0:
        print(f"🏆 Final Score: {score}/{total_played}")
        print(f"🔥 Highest Streak Achieved: {highest_streak}")
        success_rate = (score / total_played) * 100
        print(f"📊 Accuracy: {success_rate:.1f}%")
    else:
        print("You didn't answer any questions!")

if __name__ == "__main__":
    play_game()


