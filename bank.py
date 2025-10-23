initial_balance = float(input("enter initial balance"))
deposit = float(input("enter deposit amount"))

new_balance = initial_balance + deposit

print(f"initial balance:{initial_balance}")
print(f"deposit:{deposit}")
print(f"new balance after deposit:{new_balance}")

withdraw=float(input("enter withdrawal amount"))
new_balance-=withdraw
print(f"withdraw",withdraw)
print(f"new_balance",balance)