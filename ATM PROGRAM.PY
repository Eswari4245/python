balance = 5000

while True:
    print("\n1.Deposit  2.Withdraw  3.Balance  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        amount = int(input("Enter deposit amount: "))
        balance += amount
    elif ch == 2:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient balance")
    elif ch == 3:
        print("Balance:", balance)
    elif ch == 4:
        break
