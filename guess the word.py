import random

words_with_hints = {
    'python': 'A programming language 🐍',
    'banana': 'A yellow fruit 🍌',
    'dragon': 'A mythical creature 🐉',
    'yaso': 'Your awesome name 😎',
    'cyber': 'Related to tech and hacking 💻',
    'keyboard': 'You type on it ⌨️'
}

def play_game():
    print("🔥 Welcome to the Word Guessing Challenge 🔥")
    print("You have 3 tries for each word.\n")

    score = 0
    total = len(words_with_hints)

    words = list(words_with_hints.items())
    random.shuffle(words)  # Shuffle the words for extra challenge

    for index, (word, hint) in enumerate(words, start=1):
        tries = 3
        print(f"\n🧠 Word {index} of {total}")
        print("Hint:", hint)

        while tries > 0:
            guess = input("Your guess: ").lower()

            if guess == word:
                print("✅ Correct!")
                score += 1
                break
            else:
                tries -= 1
                print("❌ Wrong! Tries left:", tries)

        if tries == 0:
            print("😢 You failed! The word was:", word)

    print("\n🏁 Game Over!")
    print(f"✨ Your score: {score} out of {total}")

# Start the game
play_game()
