import random
import os

# Define symbols and multipliers using emojis
symbols = ['🍒', '🍋', '🍊', '🍉', '🍇', '🍓', '🍍', '🍏']  # Added new symbol 🍏
multipliers = {'🍒': 1.0, '🍋': 1.1, '🍊': 1.25, '🍉': 1.5, '🍇': 2.5, '🍓': 3, '🍍': 1.75, '🍏': 0.8}  # Added new multiplier for 🍏

def initialize_money_file():
    """Initialize the money file with $100 if it doesn't exist or if it contains $0.00"""
    if not os.path.isfile('money.txt'):
        with open('money.txt', 'w') as file:
            file.write('100')
    else:
        with open('money.txt', 'r') as file:
            content = file.read().strip()
            if content == '0.00':
                with open('money.txt', 'w') as file:
                    file.write('100')

def read_money():
    """Read the available amount from the money file"""
    try:
        with open('money.txt', 'r') as file:
            return float(file.read().strip())
    except (ValueError, IOError) as e:
        print(f"Error reading the money file: {e}")
        return 0.0

def write_money(amount):
    """Write the available amount to the money file"""
    try:
        with open('money.txt', 'w') as file:
            file.write(f'{amount:.2f}')
    except IOError as e:
        print(f"Error writing to the money file: {e}")

def generate_slots():
    """Generate a 3x3 matrix of slots with random symbols"""
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]

def print_slots(slots):
    """Display the matrix of slots"""
    for row in slots:
        print(' '.join(row))
    print()

def find_connected_symbols(symbol, slots):
    """Find all connected symbols (in any direction) and return the count"""
    def dfs(x, y, visited):
        """Perform depth-first search to find connected symbols"""
        stack = [(x, y)]
        connected_count = 0
        
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            connected_count += 1
            # Check neighbors (up, down, left, right, and diagonals)
            for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1),
                           (cx - 1, cy - 1), (cx + 1, cy + 1), (cx - 1, cy + 1), (cx + 1, cy - 1)]:
                if 0 <= nx < 3 and 0 <= ny < 3 and (nx, ny) not in visited and slots[nx][ny] == symbol:
                    stack.append((nx, ny))
        
        return connected_count
    
    visited = set()
    max_count = 0
    
    for i in range(3):
        for j in range(3):
            if (i, j) not in visited and slots[i][j] == symbol:
                max_count = max(max_count, dfs(i, j, visited))
    
    return max_count

def is_symbol_in_all_columns(symbol, slots):
    """Check if a symbol is in every column"""
    return all(symbol in [slots[row][col] for row in range(3)] for col in range(3))

def calculate_payout(slots, bet):
    """Calculate the payout based on symbols present in all columns and their connected count"""
    total_payout = 0
    payout_details = []

    for symbol in symbols:
        if is_symbol_in_all_columns(symbol, slots):
            connected_count = find_connected_symbols(symbol, slots)
            if connected_count >= 3:
                base_multiplier = multipliers[symbol]
                if symbol == '🍏':  # No additional multiplier for 🍏
                    additional_multiplier = 1.0
                else:
                    additional_multiplier = base_multiplier if connected_count == 3 else base_multiplier + (connected_count - 3) * 0.33
                total_win = base_multiplier * additional_multiplier * bet
                total_payout += total_win
                payout_details.append((symbol, connected_count, base_multiplier, additional_multiplier, total_win))

    return total_payout, payout_details

def main():
    """Main function to run the slot game"""
    initialize_money_file()
    money = read_money()
    
    print("🎰 Welcome to the 3x3 Slot Game!")
    
    while True:
        if money <= 0:
            print("No more money left. Game over!")
            break
        
        print(f"💵 Available Money: ${money:.2f}")
        try:
            bet = float(input("Enter your bet (0 to exit): "))
            if bet == 0:
                break
            if bet <= 0 or bet > money:
                print("Invalid bet amount. Please try again.")
                continue
            
            slots = generate_slots()
            print("Spinning...")
            print_slots(slots)
            
            payout, payout_details = calculate_payout(slots, bet)
            net_gain = payout - bet
            money += net_gain
            
            if net_gain > 0:
                print(f"🏆 You won ${net_gain:.2f}!")
                for detail in payout_details:
                    symbol, count, base_multiplier, additional_multiplier, total_win = detail
                    print(f"   {symbol} x{count} = ${total_win:.2f} ({base_multiplier} base x ${bet})")
            else:
                print("Sorry, you didn't win this time.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    write_money(money)
    print(f"Thank you for playing! Final balance: ${money:.2f}")

if __name__ == '__main__':
    main()
