import math

# Get user input
car_name = input("Enter car make and model: ")
original_price = float(input("Enter original car price: $"))
depreciation_rate = float(input("Enter annual depreciation rate %: "))
years = int(input("Enter car age in years: "))

# Calculate depreciation
current_value = original_price * math.pow((1 - depreciation_rate / 100), years)

# Create report
report = (
    f"Car Value Report\n"
    f"----------------\n"
    f"Car: {car_name}\n"
    f"Original Price: ${original_price:,.2f}\n"
    f"Depreciation Rate: {depreciation_rate}%\n"
    f"Age: {years} years\n"
    f"Estimated Current Value: ${current_value:,.2f}\n"
)

# Save report to a file
with open("car_report.txt", "w") as file:
    file.write(report)

print("\nReport saved to car_report.txt")
print(report)
