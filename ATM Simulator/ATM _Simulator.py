""" 
Applied Computational Thinking (CSE 1401) 
Major Assignment 1: Simple ATM Simulator 
Name  : M.CHANDRASEKHAR 
Reg No: 26E119D15 
Course: Applied Computational Thinking (CSE 1401) 
Only simple variables (int, float, str) are used. 
Demonstrates functions, conditionals, loops, compound interest, PIN 
validation, 
and optional cash-note breakdown. Uses no lists, tuples, sets, or 
dictionaries. 
"""

# Bank rules
OPENING_BALANCE = 20000
CORRECT_PIN = "4821"
MAX_ATTEMPTS = 3
MIN_BALANCE = 500
MAX_WITHDRAWAL = 10000
WITHDRAWAL_FEE = 10 

# ---------- Task 1: Functions ----------

def is_valid_amount(amount):
    """Return True when amount is a positive multiple of 100 up to Rs. 10,000."""
    if amount > 0 and amount % 100 == 0 and amount <= MAX_WITHDRAWAL:
        return True
    return False

def deposit(balance, amount):
    """Return updated balance after a positive deposit; otherwise keep balance."""
    if amount > 0:
        balance = balance + amount
    return balance

def withdraw(balance, amount):
    """Return updated balance when withdrawal rules and minimum balance are met."""
    if is_valid_amount(amount) and balance - amount - WITHDRAWAL_FEE >= MIN_BALANCE:
        balance = balance - amount - WITHDRAWAL_FEE
    return balance

# ---------- Task 2: Conditionals ----------

def check_pin(entered, attempts_used):
    """Return Accepted, Wrong PIN, or Card Blocked."""
    if entered == CORRECT_PIN:
        return "Accepted"
    if attempts_used < MAX_ATTEMPTS:
        return "Wrong PIN"
    return "Card Blocked"

def transaction_status(balance, amount):
    """Return the correct status for a withdrawal request."""
    if not is_valid_amount(amount):
        return "Invalid amount"
    elif balance - amount - WITHDRAWAL_FEE < MIN_BALANCE:
        return "Insufficient balance"
    else:
        return "Approved"

# ---------- Task 3: Loops ----------

def print_compound_interest_table(principal, rate, years):
    """Print yearly closing balance for Rs. 10,000 at 6% for three years."""
    balance = principal
    for year in range(1, years + 1):
        balance = balance * (1 + rate / 100)
        print(f"Year {year}: Rs. {balance:.2f}")

def is_4_digit_pin(entered):
    """Return True for a valid 4-digit PIN."""
    if len(entered) == 4 and entered.isdigit():
        return True
    return False

def pin_entry_screen():
    print("ATM PIN ENTRY")
    attempts = 0
    authorised = False

    while attempts < MAX_ATTEMPTS:
        entered = input("Enter your 4-digit PIN: ").strip()
        attempts = attempts + 1

        if not is_4_digit_pin(entered):
            print("Invalid PIN: PIN must be exactly 4 digits")
            continue

        status = check_pin(entered, attempts)
        if status == "Accepted":
            print("PIN accepted. Welcome!")
            authorised = True
            break
        elif status == "Wrong PIN":
            print("Wrong PIN")

    if not authorised:
        print("Card Blocked")
        print("Your card has been blocked after 3 incorrect attempts.")
        print("Program finished.")
    return authorised

# ---------- Task 4 (Optional): Cash dispensing ----------

def note_breakdown(amount):
    """Print counts of Rs. 500 and Rs. 100 notes, using larger notes first."""
    if amount % 100 != 0:
        print(f"Amount: Rs. {amount} cannot be paid with Rs.100 and Rs.500 notes")
        return
    fives = amount // 500
    hundreds = (amount % 500) // 100
    print(f"Amount: Rs. {amount}")
    print("Rs.500 notes :", fives)
    print("Rs.100 notes :", hundreds)
    print("Program finished.")

# ---------- TEST ----------
# ---------- Main program ----------

def main():
    print("=" * 50)
    print("TASK 1: FUNCTIONS")
    print("=" * 50)
    for amount in [100, 5000, 10000, 10100, 0, -300, 250, 1500.0]:
        print(f"is_valid_amount({amount}) -> {is_valid_amount(amount)}")

    balance = OPENING_BALANCE
    print(f"Opening balance: {balance}")
    balance = deposit(balance, 5000)
    print(f"After deposit 5000: {balance}")
    balance = deposit(balance, 250.5)
    print(f"After deposit 250.5: {balance}")
    balance = deposit(balance, -100)
    print(f"After deposit -100 (rejected): {balance}")
    balance = withdraw(balance, 1000)
    print(f"After withdraw 1000: {balance}")
    balance = withdraw(balance, 250)
    print(f"After withdraw 250 (rejected): {balance}")
    balance = withdraw(balance, 30000)
    print(f"After withdraw 30000 (rejected): {balance}")
    balance = withdraw(balance, 10000)
    print(f"After withdraw 10000: {balance}")
    print(f"withdraw(600, 100) (rejected): {withdraw(600, 100)}")

    print("=" * 50)
    print("TASK 2: CONDITIONALS")
    print("=" * 50)
    print(f"check_pin('4821', 1) -> {check_pin('4821', 1)}")
    print(f"check_pin('1234', 1) -> {check_pin('1234', 1)}")
    print(f"check_pin('1234', 2) -> {check_pin('1234', 2)}")
    print(f"check_pin('1234', 3) -> {check_pin('1234', 3)}")
    print(f"check_pin('4821', 3) -> {check_pin('4821', 3)}")
    print(f"transaction_status(20000, 1000) = {transaction_status(20000, 1000)}")
    print(f"transaction_status(20000, 10000) = {transaction_status(20000, 10000)}")
    print(f"transaction_status(20000, 250) = {transaction_status(20000, 250)}")
    print(f"transaction_status(20000, 20000) = {transaction_status(20000, 20000)}")
    print(f"transaction_status(600, 100) = {transaction_status(600, 100)}")
    print(f"transaction_status(10000, 10000) = {transaction_status(10000, 10000)}")

    print("=" * 50)
    print("TASK 3a: COMPOUND INTEREST (Rs. 10000, 6%, 3 years)")
    print("=" * 50)
    print_compound_interest_table(10000, 6, 3)

    print("=" * 50)
    print("TASK 3b: PIN ENTRY")
    print("=" * 50)
    pin_accepted = pin_entry_screen()

    # Cash dispensing is only available after the PIN is accepted
    if pin_accepted:
        print("=" * 50)
        print("TASK 4: CASH DISPENSING")
        print("=" * 50)
        note_breakdown(3700)
        note_breakdown(800)

if __name__ == "__main__":
    main()
