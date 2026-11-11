
import random

words = ["oh oui oui oui, it is Paris"]

word = random.choice(words)

guessed = ["_" if letter != " " and letter != "," else letter for letter in word]
attempts = 5

while attempts > 0 and "_" in guessed:
    print("Word:", "".join(guessed))
    guess = input("What's the capital of France? ").lower()

    if guess in word.lower():
        for i in range(len(word)):
            if word[i].lower() == guess:
                guessed[i] = word[i]
        print("YOU GOT IT RIGHT!!!")
        break
    else:
        attempts -= 1
        print(f"WRONG WRONG WRONG!!! {attempts} guesses left...")
        hidden = [i for i in range(len(word)) if guessed[1] == "_"]
        if hidden:
                reveal = random.choice(hidden)
                guesed
# poo butt