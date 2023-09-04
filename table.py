# Define the employee data

print("\nE22CSEU1235")
print("Prince Mohit")
employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000},
]

# Function to sort the employee data based on the chosen parameter
def sort_employee_data(parameter):
    sorted_data = sorted(employee_data, key=lambda x: x[parameter])
    return sorted_data

# Function to print the employee data
def print_employee_data(data):
    print("Employee ID\tName\tAge\tSalary (PM)")
    for employee in data:
        print(f"{employee['Employee ID']}\t\t{employee['Name']}\t{employee['Age']}\t{employee['Salary (PM)']}")

# Main program
while True:
    print("\nChoose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        sorted_data = sort_employee_data("Age")
        print_employee_data(sorted_data)
    elif choice == '2':
        sorted_data = sort_employee_data("Name")
        print_employee_data(sorted_data)
    elif choice == '3':
        sorted_data = sort_employee_data("Salary (PM)")
        print_employee_data(sorted_data)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")

print("Thank you for using the program!")
