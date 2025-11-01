print("=" * 40)
print("Grade Eligibility Checker")
print("=" * 40)

name = input("Enter your name")
gpa = float(input("Enter your GPA (0.0-4.0)"))
hour = float(input("Enter your total credit hours"))

list = gpa >= 3.5 and hour >= 12
gpa1 = gpa < 3.5 
hour1 = hour < 12 

print("\n")
print("=" * 40)
print("Grade Eligibility Checker")
print("=" * 40)
print(f"Student information: {name}")
print(f"Dean's list: {list}")
print(f"GPA points: {gpa1}")
print(f"Credit hours: {hour1}")
