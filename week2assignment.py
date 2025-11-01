name = str(input("Enter your name:"))
income = int(input("Enter your monthly net income:"))
fexpenses = int(input("Enter your fixed expenses: rent, utilities, internet, phone bill"))
vexpenses = int(input("Enter your variable expenses: groceries, transportation, entertainment"))
current_savings = int(input("Enter your current savings amount"))
down_payment = int(input("Enter your apartment down payment goal"))
months = int(input("Enter your months until desired purchase"))
savings = int(input("How much do you save monthly?"))
needed = int(input("How much do you need more?"))

total_monthly_expenses = fexpenses + vexpenses
monthly_savings = income - total_monthly_expenses
savings_rate_percentage = savings / (income * 100)
projected_savings_after_target_months = monthly_savings * months
total_projected_amount = current_savings + projected_savings_after_target_months
monthly_savings_needed_to_reach_goal = needed / months
additional_monthly_savings_needed = savings_rate_percentage < 0
shortfall_or_surplus = total_projected_amount - down_payment

critical_warning = total_monthly_expenses >= income
below_recommended = savings_rate_percentage < 20
good_position = savings_rate_percentage >= 20 and savings_rate_percentage < 30
excellent_position = savings_rate_percentage >= 30
goal_achievable = total_projected_amount >= down_payment

print("\n")
print("=" * 40)
print("Young Professional Budget")
print("=" * 40)

print("\n")
print(f"Name: {name}")
print(f"Income: {income}")
print("Expense breakdown:")
print(f"Total fixed expenses: {fexpenses}")
print(f"Total variable expenses: {vexpenses}")
print(f"Total monthly expenses: {total_monthly_expenses}")

print("\n")
print("-" * 40)
print("Savings analysis:")

print(f"Monthly savings amount: {monthly_savings} ")
print(f"Savings rate percentage: {savings_rate_percentage}")
print(f"Current savings: {current_savings}")
print(f"Projected savings in {months} months: {projected_savings_after_target_months} ")
print(f"Total projected: {total_projected_amount}")

print("-" * 40)
print("\n")
print("Goal analysis:")
print(f"Target amount: {down_payment}")
print(f"Monthly savings needed for goal: {monthly_savings}")
print(f"Additional monthly savings needed: {additional_monthly_savings_needed}")



