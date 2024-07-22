import random

MAX_LINES = 3
MAX_BETS = 300
MIN_BETS = 1

ROWS = 3
COLS = 3

symbols_count = {
     'A' : 3 ,
     'B' : 6 ,
     'C' : 9 ,
     'D' : 12
}

symbols_value = {
     'A' : 5 ,
     'B' : 4 ,
     'C' : 3 ,
     'D' : 2
}

def check_win (columns, bet, lines, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            current_symbol = column[line]
            if current_symbol != symbol:
                break

        else :
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    

    return winnings, winning_lines

def get_slots (rows, cols, symbols):
    all_symbols = []
    for symbol , symbols_count in symbols.items():
         for _ in range (symbols_count):
              all_symbols.append(symbol)
    
    columns = []
    for col in range(cols) :
        column = []
        new_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            new_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    

    return columns

def print_slot(columns):
    for i in range(len(columns[0])):
        for _ , row in enumerate(columns):
            if _ != len(columns) - 1:
                print(row[i], end = " | ")
            else : 
                print(row[i])      
              
def deposit ():
    amount = input('Enter your deposit amount: ')
    while True:
        if amount.isdigit():
            amount = int(amount)  
            if amount >= 0 :
                break
            else :
                amount = ("Value must be greater than zero: ")
        else :
                amount = input("Please enter a valid number: ")
                
    return amount

def get_lines ():
    lines = input('Enter your lines amount to bet on (1 - ' + str(MAX_LINES) + '): ')
    while True:
        if lines.isdigit():
            lines = int(lines)  
            if 1 <= lines <= MAX_LINES :
                break
            else :
                lines = ("Lines must be greater than 1: ")
        else :
                lines = input("Please enter a valid number: ")
                
    return lines

def get_bet ():
    bets = input('Enter your bets amount: ')
    while True:
        if bets.isdigit():
            bets = int(bets)  
            if MIN_BETS <= bets <= MAX_BETS :
                break
            else :
                bets = (f"Amount must between ${MIN_BETS} and ${MAX_BETS}")
        else :
                bets = input("Please enter a valid number: ")
                
    return bets

def spin(balance):
    lines = get_lines()
    while True : 
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
             print(f"You don't have enough for that bet. You currently have ${balance}") 
             continue
        
        break

    print(f"You're betting ${bet} on {lines} lines, your total bet is: ${total_bet} ")
    
    slots = get_slots(ROWS,COLS,symbols_count)
    print_slot(slots)
    winnings, winning_lines = check_win(slots , bet , lines , symbols_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:" , *winning_lines)
    return winnings - total_bet


def main():  
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        choice = input("Press Enter to spin ( 'q' to quit ).")
        if choice == 'q':
            break
        balance += spin(balance)
    
    print(f"Total balance after 3wlaqa: ${balance}")

main()