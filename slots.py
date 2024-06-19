import random

class SlotMachine:
    def __init__(self):
        self.symbols = ['🍒', '🍋', '🍉', '🍇', '⭐', '🔔']
        self.num_reels = 3
        self.num_rows = 3
        self.balance = 100

    def spin(self):
        result = []
        for _ in range(self.num_rows):
            row = []
            available_symbols = self.symbols[:]
            for _ in range(self.num_reels):
                symbol = random.choice(available_symbols)
                row.append(symbol)
                available_symbols.remove(symbol)
            result.append(row)
        return result

    def check_win(self, result):
        win_multiplier = 0

        # Check rows for horizontal win
        for row in result:
            if row[0] == row[1] == row[2]:
                win_multiplier += 10  # Major win for 3 same symbols

        # Check diagonals for win
        if result[0][0] == result[1][1] == result[2][2]:
            win_multiplier += 10
        if result[0][2] == result[1][1] == result[2][0]:
            win_multiplier += 10

        return win_multiplier

    def play(self, bet):
        if bet > self.balance:
            print("Insufficient balance. Your current balance is:", self.balance)
            return

        result = self.spin()
        print("Result:")
        for row in result:
            print(" | ".join(row))

        multiplier = self.check_win(result)
        winnings = bet * multiplier
        self.balance += winnings - bet

        if multiplier > 0:
            print(f"Congratulations! You've won {winnings} units!")
        else:
            print("Sorry, you didn't win this time. Try again!")

        print("Current balance:", self.balance)

if __name__ == "__main__":
    machine = SlotMachine()
    while machine.balance > 0:
        print("\nCurrent balance:", machine.balance)
        try:
            bet = int(input("Enter your bet amount: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        machine.play(bet)
        if machine.balance <= 0:
            print("You've run out of balance. Game over!")
            break
        continue_playing = input("Do you want to play again? (yes/no): ").strip().lower()
        if continue_playing != "yes":
            print("Thanks for playing! Your final balance is:", machine.balance)
            break
