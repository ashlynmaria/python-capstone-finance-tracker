#!/usr/bin/env python3
import sys

def display_menu():
    """Prints the main menu."""
    print("""
What would you like to do?
1. ➕ Add Expense
2. 📋 View All Expenses
3. 📊 View Summary
4. ❌ Exit
""")

def get_non_empty_input(prompt: str) -> str:
    """
    Prompt the user until they enter a non-empty string.
    Exits cleanly on EOF (Ctrl+D) or KeyboardInterrupt (Ctrl+C).
    """
    while True:
        try:
            value = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Goodbye!")
            sys.exit(0)
        if not value:
            print("❌ Input cannot be empty. Please try again.")
        else:
            return value

def get_amount(prompt: str) -> float:
    """
    Prompt the user until they enter a valid, non-negative float.
    """
    while True:
        s = get_non_empty_input(prompt)
        try:
            amount = float(s)
            if amount < 0:
                print("❌ Amount cannot be negative. Please enter a positive number.")
                continue
            return amount
        except ValueError:
            print("❌ Invalid amount. Please enter a valid number.")

def add_expense(expenses: dict):
    """
    Prompts the user for an expense description, category, and amount,
    then stores it in the expenses dict.
    """
    desc = get_non_empty_input("📝 Enter expense description: ")
    cat  = get_non_empty_input("📂 Enter expense category: ")
    amt  = get_amount("💵 Enter expense amount: ")
    expenses.setdefault(cat, []).append((desc, amt))
    print("✅ Expense added successfully.\n")

def view_expenses(expenses: dict):
    """
    Prints all recorded expenses grouped by category.
    """
    if not expenses:
        print("⚠️  No expenses recorded yet.\n")
        return
    for cat, items in expenses.items():
        print(f"Category: {cat}")
        for desc, amt in items:
            print(f"  - {desc}: ${amt:.2f}")
    print()

def view_summary(expenses: dict):
    """
    Prints a summary of total spending per category.
    """
    if not expenses:
        print("⚠️  No expenses to summarize.\n")
        return
    print("Summary:")
    for cat, items in expenses.items():
        total = sum(amt for _, amt in items)
        print(f"{cat}: ${total:.2f}")
    print()

def main():
    """Main program loop."""
    expenses = {}
    print("👋 Welcome to the Personal Finance Tracker!")
    while True:
        display_menu()
        choice = get_non_empty_input("Choose an option (1–4): ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_summary(expenses)
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
        sys.exit(1)
