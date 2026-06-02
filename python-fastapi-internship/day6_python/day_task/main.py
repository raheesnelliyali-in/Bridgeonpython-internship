from expense_tracker import add_expense, get_summary, view_all

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Summary")
    print("3. View All")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        add_expense(category, amount)

    elif choice == "2":
        summary = get_summary()

        if not summary:
            print("No expenses found.")
        else:
            print("\n--- Summary ---")
            for category, total in summary.items():
                print(f"{category}: ₹{total}")

    elif choice == "3":
        print("\n--- All Expenses ---")
        view_all()

    elif choice == "4":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
        
        
        
        
        