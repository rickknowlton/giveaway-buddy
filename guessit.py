import random

def get_guess(strategy="random"):
    # Read the remaining numbers from the file
    try:
        with open("remaining_numbers.txt", "r") as f:
            remaining_numbers = [int(line.strip()) for line in f.readlines()]
    except FileNotFoundError:
        print("Error: 'remaining_numbers.txt' not found. Run the main script first.")
        return
    except ValueError:
        print("Error: Invalid data in 'remaining_numbers.txt'. Ensure it contains only numbers.")
        return

    if not remaining_numbers:
        print("No numbers left to guess!")
        return

    # Guessing strategies
    if strategy == "random":
        guess = random.choice(remaining_numbers)
    elif strategy == "median":
        guess = remaining_numbers[len(remaining_numbers) // 2]
    elif strategy == "lowest":
        guess = min(remaining_numbers)
    elif strategy == "highest":
        guess = max(remaining_numbers)
    else:
        print(f"Error: Unknown strategy '{strategy}'. Use 'random', 'median', 'lowest', or 'highest'.")
        return

    print(f"Suggested guess ({strategy} strategy): {guess}")
    return guess

if __name__ == "__main__":
    # Change the strategy here if desired
    chosen_strategy = "random"  # Options: 'random', 'median', 'lowest', 'highest'
    get_guess(strategy=chosen_strategy)
