import random
import time

def roll_dice():
    input("\U0001F3B2 Press Enter to roll the dice...")
    print("Rolling", end="", flush=True)

    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

    result = random.randint(1, 6)
    print(f"\U0001F389 You rolled a {result}!")

if __name__ == "__main__":
    roll_dice()
